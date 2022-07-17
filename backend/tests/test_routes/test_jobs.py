import json


def test_create_job(client):
    data = {
        "title": "Project Manager",
        "description": "Level E position",
        "company": "Yahoo Inc",
        "company_url": "https://www.yahoo.com",
        "location": "USA, NY",
        "date_posted": "2022-07-17",
    }
    response = client.post("/jobs/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["title"] == "Project Manager"
