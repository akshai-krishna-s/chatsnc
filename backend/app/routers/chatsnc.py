from .. import models, schemas
from ..database import get_db
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List
from fastapi import status, HTTPException, Depends, Response, APIRouter
from .. import oauth2
from typing import List, Optional
from ..engine.chatsnc import snc_chat
from pydantic import BaseModel
import asyncio
from fastapi.responses import StreamingResponse
from llama_index.llms import ChatMessage, MessageRole


router = APIRouter(
    prefix="/chatsnc",
    tags=["ChatSNC"],
)


async def astreamer(generator):
    try:
        for i in generator:
            yield (i)
            await asyncio.sleep(0.1)
    except asyncio.CancelledError as e:
        print("cancelled")


class History(BaseModel):
    role: MessageRole
    content: str


@router.post("/generate", status_code=status.HTTP_201_CREATED)
def generate_chat(
    query: str,
    history: List[History],
    db: Session = Depends(get_db),
    user: schemas.UserOut = Depends(oauth2.get_current_user),
):
    chat_history = [
        ChatMessage(
            role=MessageRole.USER,
            content="Hello assistant, we are having a insightful discussion about Rules of SN College today.",
        ),
        ChatMessage(role=MessageRole.ASSISTANT, content="Okay, sounds good."),
    ]
    for h in history:
        chat_history.append(ChatMessage(role=h.role, content=h.content))
    response = snc_chat.chat(query, chat_history)
    return StreamingResponse(astreamer(response.response_gen), media_type="text/plain")
