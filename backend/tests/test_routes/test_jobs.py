import json

test_data = {
    "title": "Project Manager",
    "description": "Level E position",
    "company": "Yahoo Inc",
    "company_url": "https://www.yahoo.com",
    "location": "USA, NY",
    "date_posted": "2022-07-17",
}


def test_create_job(client, normal_user_token_headers):
    data = test_data
    response = client.post(
        "/jobs/", json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Project Manager"
    assert response.json()["company"] == "Yahoo Inc"


def test_get_job_by_id(client, normal_user_token_headers):
    data = test_data
    client.post("/jobs/", json.dumps(data), headers=normal_user_token_headers)
    response = client.get("/jobs/1")
    assert response.status_code == 200
    assert response.json()["company"] == "Yahoo Inc"


def test_get_all_jobs(client, normal_user_token_headers):
    data = test_data
    client.post("/jobs/", json.dumps(data), headers=normal_user_token_headers)
    data = {
        "title": "Software Engineer",
        "description": "Senior Level",
        "company": "Microsoft Inc",
        "company_url": "https://www.yahoo.com",
        "location": "USA, San Fransisco",
        "date_posted": "2022-07-23",
    }
    client.post("/jobs/", json.dumps(data), headers=normal_user_token_headers)
    data = {
        "title": "Web Developer",
        "description": "Level E position",
        "company": "Yahoo Inc",
        "company_url": "https://www.yahoo.com",
        "location": "USA, NY",
        "date_posted": "2022-07-24",
    }
    client.post("/jobs/", json.dumps(data), headers=normal_user_token_headers)
    response = client.get("/jobs/")
    print(response.json())
    assert response.status_code == 200
    # assert len(response.json()) == 3


def test_delete_job_by_id(client, normal_user_token_headers):
    data = test_data
    client.post("/jobs/", json.dumps(data), headers=normal_user_token_headers)
    response = client.delete("/jobs/1", headers=normal_user_token_headers)
    assert response.status_code == 200
    assert response.json()["detail"] == "Successfully deleted"


def test_update_job_by_id(client, normal_user_token_headers):
    data = test_data
    print(data)
    response = client.post(
        "/jobs/", data=json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Project Manager"
    response = client.put(
        "/jobs/1", json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 200
    # assert response.json()["detail"] == "Successfully updated data"
