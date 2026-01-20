"""
Read unread messages inside a specific group thread and surface suspects.

Usage:
  prompt = message_reader_prompt(thread)

Input:
  - thread: GroupThread representing an unread group chat.

Output:
  - Prompt string instructing the agent to open the thread, scroll through unread messages, and return JSON with suspects: [{sender_id, sender_name, evidence_text}].
"""

from __future__ import annotations

from modules.task_types import GroupThread


def message_reader_prompt(thread: GroupThread) -> str:
    return (
        f"打开群聊 {thread.name} (id={thread.thread_id})。进入后跳转到第一条未读消息，"
        "向下滚动直到所有未读消息标记为已读，同时截图关键画面。"
        "如果发现包含“代写”的信息，记录发送者头像和ID，并给出消息摘要。"
        "结束时返回 JSON，对象包含 thread_id 和 suspects 数组，字段 sender_id, sender_name, evidence_text。"
        "不要输出额外文本。"
    )
