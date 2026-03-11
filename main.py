from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch


tavily = TavilyClient()







llm = ChatOpenAI()
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="What are some jobs in Budapest that require langraph and langchain and are close to intern positions")})
    # Agent always ends with the final AI message
    print(result["messages"][-1].content)

if __name__ == "__main__":
    main()

