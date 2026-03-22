"""CrewAI v1+: Task.execute() was removed; use aexecute_sync / execute_sync and read TaskOutput.raw."""
from __future__ import annotations

from typing import Any


def _patch_crewai_task_execute_alias() -> None:
    """Map legacy Task.execute() -> execute_sync() for CrewAI v1+ (tutorials / stale code)."""
    try:
        from crewai import Task as CrewTask
    except ImportError:
        return
    if getattr(CrewTask, "execute", None) is not None:
        return
    if not hasattr(CrewTask, "execute_sync"):
        return

    def execute(self, *args: Any, **kwargs: Any):  # type: ignore[no-untyped-def]
        return self.execute_sync(*args, **kwargs)

    CrewTask.execute = execute  # type: ignore[assignment]


_patch_crewai_task_execute_alias()


def task_output_to_str(output: Any) -> str:
    if output is None:
        return ""
    if isinstance(output, str):
        return output
    raw = getattr(output, "raw", None)
    if raw is not None and str(raw).strip() != "":
        return str(raw)
    return str(output) if output is not None else ""
