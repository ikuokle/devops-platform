def test_create_user(client, db):
    response = client.post(
        "/users",
        json={
            "username": "test_user",
            "email": "test@example.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "test_user"
    assert data["email"] == "test@example.com"
    assert "id" in data