# /// script
# requires-python = ">=3.10"
# dependencies = ["mcp>=1.2,<2", "google-genai>=1.0"]
# ///
"""Local MCP server that lets Claude use Google Gemini.

Tools:
  generate_image  - make a new image from a text prompt (diagrams, illustrations, slide art)
  edit_image      - change an existing image with a text instruction
  ask_gemini      - second opinion from Gemini, optionally grounded in Google Search
  list_gemini_models - show which models this API key can use

API key: set GEMINI_API_KEY in the environment, or put the key alone in
~/.config/gemini/api_key (chmod 600). It is never written to the project.

Optional env overrides:
  GEMINI_IMAGE_MODEL      default gemini-3.1-flash-image   (Nano Banana 2)
  GEMINI_IMAGE_PRO_MODEL  default gemini-3-pro-image       (Nano Banana Pro, used when quality="pro")
  GEMINI_TEXT_MODEL       default gemini-pro-latest
  GEMINI_OUTPUT_DIR       default <project>/generated_images
"""

from __future__ import annotations

import mimetypes
import os
import re
from datetime import datetime
from pathlib import Path

from google import genai
from google.genai import types
from mcp.server.fastmcp import FastMCP, Image

PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = Path(os.environ.get("GEMINI_OUTPUT_DIR", PROJECT_DIR / "generated_images"))
IMAGE_MODEL = os.environ.get("GEMINI_IMAGE_MODEL", "gemini-3.1-flash-image")
IMAGE_PRO_MODEL = os.environ.get("GEMINI_IMAGE_PRO_MODEL", "gemini-3-pro-image")
TEXT_MODEL = os.environ.get("GEMINI_TEXT_MODEL", "gemini-pro-latest")
KEY_FILE = Path.home() / ".config" / "gemini" / "api_key"

ASPECT_RATIOS = {"1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"}

mcp = FastMCP("gemini")
_client: genai.Client | None = None


def client() -> genai.Client:
    global _client
    if _client is None:
        key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        if not key and KEY_FILE.exists():
            key = KEY_FILE.read_text().strip()
        if not key:
            raise RuntimeError(
                "No Gemini API key. Create one at https://aistudio.google.com/apikey and save it "
                f"in {KEY_FILE} (or set GEMINI_API_KEY)."
            )
        _client = genai.Client(api_key=key)
    return _client


def _slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:50] or "image"


def _save_images(response, prompt: str, filename: str | None):
    """Save every image part in a response; return (paths, MCP images, any text)."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    paths, images, texts = [], [], []
    candidates = response.candidates or []
    parts = candidates[0].content.parts if candidates and candidates[0].content else []
    for part in parts or []:
        if getattr(part, "text", None):
            texts.append(part.text)
        blob = getattr(part, "inline_data", None)
        if blob and blob.data:
            ext = mimetypes.guess_extension(blob.mime_type or "image/png") or ".png"
            stem = _slug(filename) if filename else f"{datetime.now():%Y%m%d-%H%M%S}-{_slug(prompt)}"
            path = OUTPUT_DIR / f"{stem}{'' if not paths else f'-{len(paths) + 1}'}{ext}"
            path.write_bytes(blob.data)
            paths.append(path)
            images.append(Image(data=blob.data, format=ext.lstrip(".")))
    if not paths:
        reason = ""
        if candidates and getattr(candidates[0], "finish_reason", None):
            reason = f" (finish reason: {candidates[0].finish_reason})"
        raise RuntimeError(f"Gemini returned no image{reason}. Text: {' '.join(texts) or 'none'}")
    return paths, images, "\n".join(texts)


def _image_config(aspect_ratio: str) -> types.GenerateContentConfig:
    if aspect_ratio not in ASPECT_RATIOS:
        raise ValueError(f"aspect_ratio must be one of {sorted(ASPECT_RATIOS)}")
    return types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        image_config=types.ImageConfig(aspect_ratio=aspect_ratio),
    )


@mcp.tool()
def generate_image(
    prompt: str,
    aspect_ratio: str = "16:9",
    quality: str = "standard",
    filename: str | None = None,
) -> list:
    """Generate an image with Gemini and save it under generated_images/.

    prompt: detailed description. For teaching diagrams, name every label you want
        and say 'clean flat medical illustration, white background, legible labels'.
    aspect_ratio: 1:1, 4:3, 3:4, 16:9 (slides), 9:16, 3:2, 2:3, 4:5, 5:4, 21:9.
    quality: 'standard' (fast, cheap) or 'pro' (better text rendering and detail).
    filename: optional file name without extension.
    Returns the saved path(s) and the image so you can check it.
    """
    model = IMAGE_PRO_MODEL if quality == "pro" else IMAGE_MODEL
    response = client().models.generate_content(
        model=model, contents=[prompt], config=_image_config(aspect_ratio)
    )
    paths, images, text = _save_images(response, prompt, filename)
    summary = f"Saved ({model}): " + ", ".join(str(p) for p in paths)
    if text:
        summary += f"\nGemini note: {text}"
    return [summary, *images]


@mcp.tool()
def edit_image(
    image_path: str,
    instruction: str,
    aspect_ratio: str = "16:9",
    quality: str = "standard",
    filename: str | None = None,
) -> list:
    """Edit an existing image (a PNG/JPG on disk) with a plain-language instruction,
    e.g. 'add the label Odontoblast layer with a leader line' or 'make the background white'.
    The original file is left untouched; the result is saved as a new file."""
    src = Path(image_path).expanduser()
    if not src.is_absolute():
        src = PROJECT_DIR / src
    mime = mimetypes.guess_type(src.name)[0] or "image/png"
    model = IMAGE_PRO_MODEL if quality == "pro" else IMAGE_MODEL
    response = client().models.generate_content(
        model=model,
        contents=[types.Part.from_bytes(data=src.read_bytes(), mime_type=mime), instruction],
        config=_image_config(aspect_ratio),
    )
    paths, images, text = _save_images(response, instruction, filename or f"{src.stem}-edited")
    summary = f"Saved ({model}): " + ", ".join(str(p) for p in paths)
    if text:
        summary += f"\nGemini note: {text}"
    return [summary, *images]


@mcp.tool()
def ask_gemini(prompt: str, use_google_search: bool = False, model: str | None = None) -> str:
    """Ask Gemini a question for a second opinion or cross-check.
    Set use_google_search=True to ground the answer in live Google Search results;
    the sources are listed at the end."""
    config = None
    if use_google_search:
        config = types.GenerateContentConfig(tools=[types.Tool(google_search=types.GoogleSearch())])
    response = client().models.generate_content(
        model=model or TEXT_MODEL, contents=[prompt], config=config
    )
    answer = response.text or "(no text returned)"
    meta = getattr(response.candidates[0], "grounding_metadata", None) if response.candidates else None
    chunks = getattr(meta, "grounding_chunks", None) or []
    sources = [f"- {c.web.title}: {c.web.uri}" for c in chunks if getattr(c, "web", None)]
    if sources:
        answer += "\n\nSources:\n" + "\n".join(sources)
    return answer


@mcp.tool()
def list_gemini_models(contains: str = "") -> str:
    """List Gemini models available to this API key (filter by substring, e.g. 'image')."""
    names = [m.name.removeprefix("models/") for m in client().models.list()]
    names = [n for n in names if contains.lower() in n.lower()]
    return "\n".join(sorted(names)) or "No matching models."


if __name__ == "__main__":
    mcp.run()
