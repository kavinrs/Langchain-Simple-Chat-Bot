import redis
import json

r=redis.Redis(host="localhost",port=6379,decode_responses=True)

def chat_history(session_id:str):
    data=r.get(session_id)
    if not data:
        return []
    return json.loads(data)

def add_history(session_id:str,human_msg:str,ai_msg:str):
    history=chat_history(session_id)

    history.append(("human",human_msg))
    history.append(("ai",ai_msg))

    r.set(session_id,json.dumps(history))