import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

SERVER= client ={
    "my_server": {
        "url": "http://localhost:8001/mcp",
        "transport": "streamable_http",
    }
}


async def main():

    client = MultiServerMCPClient(SERVER)
    tools = await client.get_tools()
    named_tools={}
    for tool in tools:
        named_tools[tool.name]=tool
    print(named_tools)
    llm = ChatAnthropic(model='anthropic:claude-haiku-4-5-20251001')
    llm_with_tools=llm.bind_tools(tools)

    prompt="what is the product of 12 nd 13"
    response = await llm_with_tools.ainvoke(prompt)

    print("Response:"response)





if __name__=="__main__":
    asyncio.run(main())