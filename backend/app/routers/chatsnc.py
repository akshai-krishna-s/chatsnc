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
import json
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix="/chat",
    tags=["ChatSNC"],
)


async def astreamer(generator):
    try:
        for i in generator:
            yield (i)
            await asyncio.sleep(0.1)
    except asyncio.CancelledError as e:
        print("cancelled")


@router.post("/generate", status_code=status.HTTP_201_CREATED)
def generate_chat(
    query: str,
    history: List[schemas.History],
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


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.ChatCreateOut
)
def create_chat(
    db: Session = Depends(get_db),
    user: schemas.UserOut = Depends(oauth2.get_current_user),
):
    new_chat = models.Chat(
        user_id=user.id,
    )
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return new_chat


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_chat(
    id: int,
    history: List[schemas.HistoryOut],
    db: Session = Depends(get_db),
    user: schemas.UserOut = Depends(oauth2.get_current_user),
):
    chat_str = json.dumps(jsonable_encoder(history))

    chat_query = db.query(models.Chat).filter(models.Chat.id == id)
    chat = chat_query.first()
    if not chat:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )
    if chat.user_id != user.id:  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authorized",
        )
    chat_query.update({"history": chat_str}, synchronize_session=False)
    db.commit()

    return {"message": "Chat updated successfully"}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_chat(
    id: int,
    db: Session = Depends(get_db),
    user: schemas.UserOut = Depends(oauth2.get_current_user),
):
    chat_query = db.query(models.Chat).filter(models.Chat.id == id)
    chat = chat_query.first()
    if not chat:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )
    if chat.user_id != user.id:  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authorized",
        )
    chat_str = chat.history
    chat_history = json.loads(chat_str)  # type: ignore
    return chat_history


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ChatOut])
def get_chats(
    db: Session = Depends(get_db),
    user: schemas.UserOut = Depends(oauth2.get_current_user),
):
    chats = (
        db.query(models.Chat)
        .filter(models.Chat.user_id == user.id)
        .order_by(models.Chat.created_at.desc())
        .all()
    )

    for chat in chats:
        if chat.history:  # type: ignore
            chat.history = json.loads(chat.history)  # type: ignore
    return chats
