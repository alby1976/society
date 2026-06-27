"""Public package interface for the content generator.

Exports
-------
Generator
    Main build orchestrator for Obsidian, PDF, and DOCX outputs.
"""

__all__ = ["Generator"]

from .generator import Generator
