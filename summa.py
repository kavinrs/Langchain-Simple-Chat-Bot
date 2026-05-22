import os 
from  langchain_openai import ChatOpenAI
import asyncio


api_key=os.environ.get("OPENAI_API_KEY")
llm_openai=ChatOpenAI(model="gpt-4o-mini",
                      api_key=api_key,
                      temperature=0)

res=llm_openai.invoke("Hi this is kavin").content
# tokens=[]

async def main():

    async for token in llm_openai.astream(
        "Tell about Albert Einstein"
    ):
        print(token.content, end="|", flush=True)

asyncio.run(main())