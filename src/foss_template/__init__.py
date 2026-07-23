"""foss-template: placeholder module proving the pipeline. Replace in real projects."""

__version__ = "0.1.0"


def is_pinned(requirement: str) -> bool:
    """True if a requirement string is pinned to an exact version (contains '==')."""
    return "==" in requirement
