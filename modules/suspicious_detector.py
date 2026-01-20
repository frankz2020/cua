"""
Extract suspects flagged by the agent for a given thread.

Usage:
  suspects = extract_suspects(thread, text_output, screenshot_paths)

Input:
  - thread: GroupThread in context.
  - text_output: JSON string returned by the agent with suspects array.
  - screenshot_paths: list of Paths captured during this thread run.

Output:
  - List[Suspect] with avatar_path bound to the last screenshot when available.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List

from modules.task_types import GroupThread, Suspect


def extract_suspects(
    thread: GroupThread, text_output: str, screenshot_paths: List[Path]
) -> List[Suspect]:
    payload = json.loads(text_output)
    entries = payload.get("suspects", [])
    avatar_path = screenshot_paths[-1] if screenshot_paths else Path()
    return [
        Suspect(
            sender_id=str(item.get("sender_id", "")),
            sender_name=str(item.get("sender_name", "")),
            avatar_path=avatar_path,
            evidence_text=str(item.get("evidence_text", "")),
            thread_id=thread.thread_id,
        )
        for item in entries
    ]
