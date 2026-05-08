from fastapi import APIRouter,Request,Response
from ChatBot.chatbot import run_agent,email_agent
from FastApi.models import Query
from Memory.memory import add_history,chat_history
import uuid

router=APIRouter()

@router.post("/chat")
def chat_revoke(query:Query,request:Request,response:Response):

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

@router.post("/email")
def email(query:Query):
    
    answer=email_agent(query.question)

    return {
        "answer":answer
    }