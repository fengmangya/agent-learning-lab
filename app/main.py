from app.agent import ask_agent

def main():
    question = input("请输入问题：")
    
    try:
        answer = ask_agent(question)
        print(answer)

    except ValueError as error:
        print(f"输入错误：{error}")
    

if __name__ == "__main__":
    main()