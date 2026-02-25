"""Top-level package for the Scientific Book Builder system."""

try:
    from importlib import metadata as _metadata  # Python 3.8+
except ImportError:  # pragma: no cover
    import importlib_metadata as _metadata  # type: ignore

try:
    __version__: str = _metadata.version(__name__)
except Exception:  # pragma: no cover
    __version__ = "0.0.0"

# Re-export the orchestrator for convenience
from .agents.orchestrator import orchestrator  # noqa: E402  pylint: disable=wrong-import-position

__all__ = ["orchestrator", "__version__"] 