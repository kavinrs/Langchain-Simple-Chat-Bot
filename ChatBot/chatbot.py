import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add parent directory to path BEFORE importing tools
sys.path.insert(0, str(Path(__file__).parent.parent))

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import ToolMessage,HumanMessage,AIMessage
from langchain_google_community import GmailToolkit
from langchain_google_community.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)
from tools.tools import *
import logging

# Load environment variables first
load_dotenv()

#LangSmith Configurations
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "aurelioai-langchain-course-langsmith-openai"

# Only set if the key exists
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
if langchain_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

key=os.environ.get("OPENAI_API_KEY")


llm_openai=ChatOpenAI(model="gpt-4o-mini",
                    temperature=0,api_key=key)
# res=llm_openai.invoke("Hi,Hello this is kavin").content
# print(res)
prompt_temp=ChatPromptTemplate.from_messages([
    ("system","You are a helpful math assistant.\n"
     "Use the available tools to solve math problems step by step.\n"
     "Call one tool at a time and wait for the result before proceeding.\n"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# Use absolute path for credentials file
credentials_path = Path(__file__).parent / "credentials.json"
token_path = Path(__file__).parent.parent / "token.json"

credentials = get_gmail_credentials(
    token_file=str(token_path),
    scopes=["https://mail.google.com/"],
    client_sercret_file=str(credentials_path),
)
api_resource = build_resource_service(credentials=credentials)
gmail_toolkit = GmailToolkit(api_resource=api_resource)
gmail_tools = gmail_toolkit.get_tools()

toolkit=[add,multiply,divide,subtract,exponent,final_answer,weather,web_search,differentiate,integrate_expr,scientific_calculator,python_execution,churn_csvtool] + gmail_tools

llm_with_tools = llm_openai.bind_tools(toolkit, tool_choice="any")

agent = (
    {
        "input": lambda x: x["input"],
        "chat_history": lambda x: x.get("chat_history", []),
        "agent_scratchpad": lambda x: x.get("agent_scratchpad", [])
    }
    | prompt_temp
    | llm_with_tools
)

# response=agent.invoke({
#     "input":"tell the answer for 2+2",
#     "chat_history":[],
#     "agent_scratchpad":[]
# }).content
# print(response)
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

format=logging.Formatter( "%(asctime)s - %(levelname)s - %(message)s")
stream_handler=logging.StreamHandler()
stream_handler.setFormatter(format)
logger.addHandler(stream_handler)

def formmated_history(history):
    formmated=[]
    for role,content in history:
        if role=="human":
            formmated.append(HumanMessage(content=content))
        else:
            formmated.append(AIMessage(content=content))
    return formmated

def run_agent(query,history):
    scratchpad = []
    tool_dict = {t.name: t for t in toolkit}
    history=formmated_history(history)

    for _ in range(5):  # limit steps
        response = agent.invoke({
            "input": query,
            "chat_history": history,
            "agent_scratchpad": scratchpad
        })

        
        logger.debug(
                    f"MODEL RESPONSE → tool_calls: {response.tool_calls}, content: {response.content}")
        if response.tool_calls:
            tool_call = response.tool_calls[0]
            tool_name = tool_call["name"]
            args = tool_call["args"]

            logger.info(f"TOOL: {tool_name} | args: {args}")

            if tool_name == "final_answer":
                return  args.get("answer") or str(args)
            
            if tool_name not in tool_dict:
                return f"Unknown tool: {tool_name}"

            result = tool_dict[tool_name].invoke(args)

            scratchpad.append(response)
            scratchpad.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=tool_call["id"]
                )
            )

        else:
            return response.content

    return "Stopped after max steps"

def email_agent(query: str):
    """Send email-related commands to the agent"""
    scratchpad = []
    tool_dict = {t.name: t for t in toolkit}
    history = []

    for _ in range(5):  
        response = agent.invoke({
            "input": query,
            "chat_history": history,
            "agent_scratchpad": scratchpad
        })

        logger.debug(
            f"EMAIL RESPONSE → tool_calls: {response.tool_calls}, content: {response.content}")
        
        if response.tool_calls:
            tool_call = response.tool_calls[0]
            tool_name = tool_call["name"]
            args = tool_call["args"]

            logger.info(f"EMAIL TOOL: {tool_name} | args: {args}")

            if tool_name == "final_answer":
                return args.get("answer") or str(args)
            
            if tool_name not in tool_dict:
                return f"Unknown tool: {tool_name}"

            result = tool_dict[tool_name].invoke(args)

            scratchpad.append(response)
            scratchpad.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=tool_call["id"]
                )
            )
        else:
            return response.content

    return "Email operation completed or stopped after max steps"

# print(run_agent("What is 2 + 2?"))

print(run_agent("""Write a formal email. To: kavinventhan12@gmail.com  Subject: Placement Update – Sudhakar  Body:
- State that Sudhakar has been placed in Vasi's Company
- Keep tone professional
- 5–6 lines maximum
- Include greeting and closing

Return only the final email.""",[]))


