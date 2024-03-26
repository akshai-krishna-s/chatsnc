from app import schemas


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


def test_get_one_chat(authorized_client, test_chats):
    res = authorized_client.get(f"/chat/{test_chats[0].id}")
    assert res.status_code == 200
    assert str(res.json()) == test_chats[0].history


def test_create_chat(authorized_client, test_user):
    res = authorized_client.post("/chat/")
    created_chat = schemas.ChatCreateOut(**res.json())
    assert res.status_code == 201


def test_unauthorized_user_create_chat(client):
    res = client.post("/chat/")
    assert res.status_code == 401


def test_unauthorized_user_update_chat(client, test_chats):
    res = client.put(f"/chat/{test_chats[0].id}", json={"history": []})
    assert res.status_code == 401


def test_update_chat(authorized_client, test_chats):
    new_history = [{"role": "user", "content": "Updated message"}]
    res = authorized_client.put(f"/chat/{test_chats[0].id}", json=new_history)
    assert res.status_code == 200
    assert res.json()["message"] == "Chat updated successfully"


def test_update_chat_not_found(authorized_client):
    new_history = [{"role": "user", "content": "Updated message"}]
    res = authorized_client.put("/chat/999", json=new_history)

    assert res.status_code == 404
