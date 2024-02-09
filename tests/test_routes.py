def test_get_regions_status_code(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /regions
    THEN the status code should be 200
    """
    response = client.get("/regions")
    assert response.status_code == 200

def test_get_events_status_code(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /regions
    THEN the status code should be 200
    """
    response = client.get("/events")
    assert response.status_code == 200

def test_get_regions_json(client):
    """
    GIVEN a Flask test client
    AND the database contains data of the regions
    WHEN a request is made to /regions
    THEN the response should contain json
    AND a JSON object for Tonga should be in the json
    """
    response = client.get("/regions")
    assert response.headers["Content-Type"] == "application/json"
    tonga = {'NOC': 'TGA', 'notes': '', 'region': 'Tonga'}
    assert tonga in response.json

def test_get_events_json(client):
    """
    GIVEN a Flask test client
    AND the database contains data of the regions
    WHEN a request is made to /regions
    THEN the response should contain json
    AND a JSON object for Tonga should be in the json
    """
    response = client.get("/events")
    assert response.headers["Content-Type"] == "application/json"
    italy = {'NOC': 'ITA', 'countries': '23', 'country': 'Italy', 'disabilities_included': 'Spinal injury', 'duration': 7, 'end': '25/09/1960', 'events': 113, 'highlights': 'First Games with a disability held in same venues as Olympic Games', 'host': 'Rome', 'id': 1, 'participants': 209, 'participants_f': None, 'participants_m': None, 'region': 'ITA', 'sports': 8, 'start': '18/09/1960', 'type': 'summer', 'year': 1960}
    assert italy in response.json

def test_get_specified_region(client):
    """
    GIVEN a Flask test client
    AND the 5th entry is AND,Andorra,
    WHEN a request is made to /regions/AND
    THEN the response json should match that for Andorra
    AND the response status_code should be 200
    """
    and_json = {'NOC': 'AND', 'notes': '', 'region': 'Andorra'}
    response = client.get("/regions/AND")
    assert response.headers["Content-Type"] == "application/json"
    assert response.status_code == 200
    assert response.json == and_json

def test_get_specified_event(client):
    """
    GIVEN a Flask test client
    AND the 5th entry is AND,Andorra,
    WHEN a request is made to /regions/AND
    THEN the response json should match that for Andorra
    AND the response status_code should be 200
    """
    ita_json = {'NOC': 'ITA', 'countries': '23', 'country': 'Italy', 'disabilities_included': 'Spinal injury', 'duration': 7, 'end': '25/09/1960', 'events': 113, 'highlights': 'First Games with a disability held in same venues as Olympic Games', 'host': 'Rome', 'id': 1, 'participants': 209, 'participants_f': None, 'participants_m': None, 'region': 'ITA', 'sports': 8, 'start': '18/09/1960', 'type': 'summer', 'year': 1960}
    response = client.get("/events/1")
    assert response.headers["Content-Type"] == "application/json"
    assert response.status_code == 200
    assert response.json == ita_json

def test_get_region_not_exists(client):
    """
    GIVEN a Flask test client
    WHEN a request is made for a region code that does not exist
    THEN the response status_code should be 404 Not Found
    """
    response = client.get("/regions/AAA")
    assert response.status_code == 404

def test_get_event_not_exists(client):
    """
    GIVEN a Flask test client
    WHEN a request is made for a region code that does not exist
    THEN the response status_code should be 404 Not Found
    """
    response = client.get("/events/121")
    assert response.status_code == 404

def test_post_region(client):
    """
    GIVEN a Flask test client
    AND valid JSON for a new region
    WHEN a POST request is made to /regions
    THEN the response status_code should be 201
    """
    # JSON to create a new region
    region_json = {
        "NOC": "ZZZ",
        "region": "ZedZedZed"
    }
    # pass the JSON in the HTTP POST request
    response = client.post(
        "/regions",
        json=region_json,
        content_type="application/json",
    )
    # 201 is the HTTP status code for a successful POST or PUT request
    assert response.status_code == 200

def test_post_event(client):
    """
    GIVEN a Flask test client
    AND valid JSON for a new region
    WHEN a POST request is made to /regions
    THEN the response status_code should be 201
    """
    # JSON to create a new region
    event_json = {'NOC': 'ITA', 'countries': '23', 'country': 'Italy', 'disabilities_included': 'Spinal injury', 'duration': 7, 'end': '25/09/1960', 'events': 113, 'highlights': 'First Games with a disability held in same venues as Olympic Games', 'host': 'Rome', 'id': 33, 'participants': 209, 'participants_f': None, 'participants_m': None, 'region': 'ITA', 'sports': 8, 'start': '18/09/1960', 'type': 'summer', 'year': 1960}
    # pass the JSON in the HTTP POST request
    response = client.post(
        "/events",
        json=event_json,
        content_type="application/json",
    )
    # 201 is the HTTP status code for a successful POST or PUT request
    assert response.status_code == 200

def test_region_post_error(client):
    """
        GIVEN a Flask test client
        AND JSON for a new region that is missing a required field ("region")
        WHEN a POST request is made to /regions
        THEN the response status_code should be 400
        """
    missing_region_json = {"NOC": "ZZY"}
    response = client.post("/regions", json=missing_region_json)
    assert response.status_code == 400

def test_event_post_error(client):
    """
        GIVEN a Flask test client
        AND JSON for a new region that is missing a required field ("region")
        WHEN a POST request is made to /regions
        THEN the response status_code should be 400
        """
    missing_NOC_json = {'countries': '23', 'country': 'Italy', 'disabilities_included': 'Spinal injury', 'duration': 7, 'end': '25/09/1960', 'events': 113, 'highlights': 'First Games with a disability held in same venues as Olympic Games', 'host': 'Rome', 'id': 33, 'participants': 209, 'participants_f': None, 'participants_m': None, 'region': 'ITA', 'sports': 8, 'start': '18/09/1960', 'type': 'summer', 'year': 1960}
    response = client.post("/events", json=missing_NOC_json)
    assert response.status_code == 400

def test_patch_region(client, new_region):
    """
        GIVEN an existing region
        AND a Flask test client
        WHEN an UPDATE request is made to /regions/<noc-code> with notes json
        THEN the response status code should be 200
        AND the response content should include the message 'Region <NOC_code> updated'
    """
    new_region_notes = {'notes': 'An updated note'}
    code = new_region['NOC']
    response = client.patch(f"/regions/{code}", json=new_region_notes)
    assert response.json['message'] == 'Region NEW updated'
    assert response.status_code == 200

def test_patch_event(client, new_event):
    """
        GIVEN an existing event
        AND a Flask test client
        WHEN an UPDATE request is made to /events/<id-code> with highlights json
        THEN the response status code should be 200
        AND the response content should include the message 'Event <id> updated'
    """
    new_event_highlights = {'highlights': 'An updated highlight'}
    code = new_event['id']
    response = client.patch(f"/events/{code}", json=new_event_highlights)
    assert response.json['message'] == 'Event 33 updated'
    assert response.status_code == 200

def test_delete_region(client, new_region):
    """
    GIVEN an existing region in JSON format
    AND a Flask test client
    WHEN a DELETE request is made to /regions/<noc-code>
    THEN the response status code should be 200
    AND the response content should include the message 'Region {noc_code} deleted.'
    """
    # Get the NOC code from the JSON which is returned in the new_region fixture
    code = new_region['NOC']
    response = client.delete(f"/regions/{code}")
    assert response.status_code == 200
    assert response.json['message'] == 'Region NEW deleted'

def test_delete_event(client, new_event):
    """
    GIVEN an existing region in JSON format
    AND a Flask test client
    WHEN a DELETE request is made to /regions/<noc-code>
    THEN the response status code should be 200
    AND the response content should include the message 'Region {noc_code} deleted.'
    """
    # Get the NOC code from the JSON which is returned in the new_region fixture
    code = new_event['id']
    response = client.delete(f"/events/{code}")
    assert response.status_code == 200
    assert response.json['message'] == 'Event 33 deleted'