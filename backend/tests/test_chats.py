from app import schemas
import pytest


def test_get_all_chats(authorized_client, test_chats):
    res = authorized_client.get("/chat/")

    posts_list = [schemas.ChatOut(**chat) for chat in res.json()]
    assert len(res.json()) == len(test_chats)
    assert res.status_code == 200


def test_unauthorized_user_get_all_chats(client, test_chats):
    res = client.get("/chat/")
    assert res.status_code == 401


def test_unauthorized_user_get_one_chat(client, test_chats):
    res = client.get(f"/chat/{test_chats[0].id}")
    assert res.status_code == 401


def test_get_one_chat_not_found(authorized_client, test_chats):
    res = authorized_client.get("/chat/999")
    assert res.status_code == 404
