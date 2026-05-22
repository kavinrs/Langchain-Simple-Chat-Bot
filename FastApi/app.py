from fastapi import APIRouter,Request,Response
from LangchainAgent.ChatBot.chatbot import run_agent,email_agent
from FastApi.models import Query
from LangchainAgent.Memory.memory import add_history,chat_history
import uuid

router=APIRouter()


async def token_generator(content: str, streamer: QueueCallbackHandler):
    task = asyncio.create_task(agent_executor.invoke(
        input=content,
        streamer=streamer,
        verbose=True  # set to True to see verbose output in console
    ))
    # initialize various components to stream
    async for token in streamer:
        try:
            if token == "<<STEP_END>>":
                # send end of step token
                yield "</step>"
            elif tool_calls := token.message.additional_kwargs.get("tool_calls"):
                if tool_name := tool_calls[0]["function"]["name"]:
                    # send start of step token followed by step name tokens
                    yield f"<step><step_name>{tool_name}</step_name>"
                if tool_args := tool_calls[0]["function"]["arguments"]:
                    # tool args are streamed directly, ensure it's properly encoded
                    yield tool_args
        except Exception as e:
            print(f"Error streaming token: {e}")
            continue
    await task

    
@router.post("/chat")
def chat_revoke(query:Query,request:Request,response:Response):
    try:
        session_id=request.cookies.get("session_id")

        if not session_id:
            session_id=str(uuid.uuid4())
            response.set_cookie(
                key="session_id",
                value=session_id,
                httponly=True
            )
        
        history=chat_history(session_id)

        answer=run_agent(query.question,history)

        add_history(session_id,query.question,answer)

        return {
            "answer":answer,
            "session_id":session_id
        }
    except Exception as e:
        import traceback
        print("ERROR IN CHAT ENDPOINT:")
        print(traceback.format_exc())
        raise

@router.post("/email")
def email(query:Query):
    
    answer=email_agent(query.question)

    return {
        "answer":answer
    }