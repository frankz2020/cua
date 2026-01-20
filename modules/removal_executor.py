"""
Build removal instructions for the agent.

Usage:
  prompt = removal_prompt(plan)

Input:
  - plan: RemovalPlan with confirmed flag and suspects list.

Output:
  - Prompt string directing the agent to open group management and remove listed users using IDs and avatars.
"""

from __future__ import annotations

from modules.task_types import RemovalPlan


def removal_prompt(plan: RemovalPlan) -> str:
    suspects = [
        f"{suspect.sender_name} (ID: {suspect.sender_id})" for suspect in plan.suspects
    ]
    suspect_list = "; ".join(suspects)
    return (
        "打开微信群右上角的管理入口，选择“移出”。"
        f"目标用户: {suspect_list}。"
        "通过头像和ID核对后批量选择并确认移出。"
        "完成后回复 JSON，键 removal_status，值为 done 或 failed，并附原因。"
        "不要输出额外文字。"
    )
