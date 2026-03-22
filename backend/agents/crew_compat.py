"""CrewAI v1+: Task.execute() was removed; use aexecute_sync / execute_sync and read TaskOutput.raw."""
from __future__ import annotations

from typing import Any


def task_output_to_str(output: Any) -> str:
    if output is None:
        return ""
    if isinstance(output, str):
        return output
    raw = getattr(output, "raw", None)
    if raw is not None and str(raw).strip() != "":
        return str(raw)
    return str(output) if output is not None else ""
