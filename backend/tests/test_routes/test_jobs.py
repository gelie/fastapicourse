import json

test_data = {
    "title": "Project Manager",
    "description": "Level E position",
    "company": "Yahoo Inc",
    "company_url": "https://www.yahoo.com",
    "location": "USA, NY",
    "date_posted": "2022-07-17",
}


def test_create_job(client):
    data = test_data
    response = client.post("/jobs/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["title"] == "Project Manager"


def test_get_job_by_id(client):
    data = test_data
    client.post("/jobs/", json.dumps(data))
    response = client.get("/jobs/1")
    assert response.status_code == 200
    assert response.json()["company"] == "Yahoo Inc"


def test_get_all_jobs(client):
    data = test_data
    client.post("/jobs/", json.dumps(data))
    data = {
        "title": "Software Engineer",
        "description": "Senior Level",
        "company": "Microsoft Inc",
        "company_url": "https://www.yahoo.com",
        "location": "USA, San Fransisco",
        "date_posted": "2022-07-23",
    }
    client.post("/jobs/", json.dumps(data))
    data = {
        "title": "Web Developer",
        "description": "Level E position",
        "company": "Yahoo Inc",
        "company_url": "https://www.yahoo.com",
        "location": "USA, NY",
        "date_posted": "2022-07-24",
    }
    client.post("/jobs/", json.dumps(data))
    response = client.get("/jobs/")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_delete_job_by_id(client):
    data = test_data
    client.post("/jobs/", json.dumps(data))
    response = client.delete("/jobs/1")
    # assert response.status_code == 200
    assert response.json()["detail"] == "Successfully deleted"


def test_update_job_by_id(client):
    data = test_data
    client.post("/jobs/", json.dumps(data))
    response = client.put("/jobs/1", json.dumps(data))
    assert response.json()["detail"] == "Successfully updated data"
