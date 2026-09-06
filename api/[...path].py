"""Vercel serverless entrypoint (catch-all for /api/*).

Vercel serves functions under api/ at /api/*; this catch-all hands every
/api/... request to the FastAPI app with the ORIGINAL path preserved
(native function routing, no rewrite), so the app's /api/route,
/api/results, ... routes match exactly as they do locally.

The built React SPA is served statically from public/ (populated by the
buildCommand in vercel.json), so / and /assets/* never reach this function.
"""
import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from webapp.server import app  # noqa: E402  (sys.path must be set first)
