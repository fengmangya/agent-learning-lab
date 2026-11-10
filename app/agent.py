def ask_agent(question: str) -> str:
    """
    接收用户问题，返回 Agent 的回答。
    """
    if not question.strip():
        raise ValueError("问题不能为空")

    return f"我收到了你的问题：{question}"

# Git change tracking experiment