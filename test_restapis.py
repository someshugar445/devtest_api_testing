import requests


def test_api_get_page2():
    resp = requests.get("https://reqres.in/api/users?page=2")
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
    for record in resp.json()['data']:
        if record['id'] == 7:
            assert record['first_name'] == "Michael", \
                "Data not matched! Expected : Michael, but found : " + str(record['first_name'])
            assert record['last_name'] == "Lawson", \
                "Data not matched! Expected : Lawson, but found : " + str(record['last_name'])


def test_api_get_single_user():
    resp = requests.get("https://reqres.in/api/users/2")
    assert (resp.status_code == 200), \
        "Status code is not 200. Rather found : " + str(resp.status_code)
    assert resp.json()['data']['id'] == 2, \
        "Data not matched! Expected : 2, but found : " + str(resp.json()['data']['id'])


def test_api_post():
    data = {
        "name": "morpheus",
        "job": "leader"
    }
    resp = requests.post(url="https://reqres.in/api/users", data=data)
    data = resp.json()
    assert (resp.status_code == 201), "Status code is not 201. Rather found : " \
                                      + str(resp.status_code)
    assert data['name'] == "morpheus", "User created with wrong name. \
        Expected : morpheus, but found : " + str(data['name'])
    assert data['job'] == "leader", "User created with wrong job. \
        Expected : leader, but found : " + str(data['name'])


def test_api_put():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    resp = requests.put(url="https://reqres.in/api/users", data=data)
    data = resp.json()
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " \
                                      + str(resp.status_code)
    assert data['name'] == "morpheus", "User created with wrong name. \
        Expected : morpheus, but found : " + str(data['name'])
    assert data['job'] == "zion resident", "User created with wrong job. \
        Expected : zion resident, but found : " + str(data['name'])
