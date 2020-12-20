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


def test_api_get_user_positive():
    resp = requests.get("https://reqres.in/api/users/2")
    assert (resp.status_code == 200), \
        "Status code is not 200. Rather found : " + str(resp.status_code)
    assert resp.json()['data']['id'] == 2, \
        "Data not matched! Expected : 2, but found : " + str(resp.json()['data']['id'])

def test_api_get_user_negative():
    resp = requests.get("https://reqres.in/api/users/23")
    assert (resp.status_code == 404), \
        "Status code is not 404. Rather found : " + str(resp.status_code)

def test_api_get_list():
    resp = requests.get("https://reqres.in/api/unknown")
    assert (resp.status_code == 200), \
        "Status code is not 200. Rather found : " + str(resp.status_code)
    for record in resp.json()['data']:
        if record['id'] == 7:
            assert record['first_name'] == "Michael", \
                "Data not matched! Expected : Michael, but found : " + str(record['first_name'])
            assert record['last_name'] == "Lawson", \
                "Data not matched! Expected : Lawson, but found : " + str(record['last_name'])

def test_api_get_single_positive():
    resp = requests.get("https://reqres.in/api/unknown/2")
    assert (resp.status_code == 200), \
        "Status code is not 200. Rather found : " + str(resp.status_code)
    if resp.json()['data']['id'] == 2:
        assert resp.json()['data']['name'] == "fuchsia rose", \
            "Data not matched! Expected : fuchsia rose, but found : " + str(resp.json()['data']['name'])

def test_api_get_single_negative():
    resp = requests.get("https://reqres.in/api/unknown/23")
    assert (resp.status_code == 404), \
        "Status code is not 404. Rather found : " + str(resp.status_code)


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


def test_api_patch():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    resp = requests.patch(url="https://reqres.in/api/users", data=data)
    data = resp.json()
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " \
                                      + str(resp.status_code)
    assert data['name'] == "morpheus", "User created with wrong name. \
        Expected : morpheus, but found : " + str(data['name'])
    assert data['job'] == "zion resident", "User created with wrong job. \
        Expected : zion resident, but found : " + str(data['name'])


def test_api_delete():
    resp = requests.delete(url="https://reqres.in/api/users/2")
    assert (resp.status_code == 204), "Status code is not 200. Rather found : " \
                                      + str(resp.status_code)


def test_api_register_positive():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    resp = requests.post(url="https://reqres.in/api/register", data=data)
    data = resp.json()
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " \
                                      + str(resp.status_code)

def test_api_register_negative():
    data = {
        "email": "sydney@fife",
    }
    resp = requests.post(url="https://reqres.in/api/register", data=data)
    data = resp.json()
    assert (resp.status_code == 400), "Status code is not 400. Rather found : " \
                                      + str(resp.status_code)


def test_api_login_positive():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    resp = requests.post(url="https://reqres.in/api/login", data=data)
    data = resp.json()
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " \
                                      + str(resp.status_code)

def test_api_login_negative():
    data = {
        "email": "peter@klaven",
    }
    resp = requests.post(url="https://reqres.in/api/login", data=data)
    data = resp.json()
    assert (resp.status_code == 400), "Status code is not 400. Rather found : " \
                                      + str(resp.status_code)



def test_api_get_delay():
    resp = requests.get("https://reqres.in/api/users?delay=3")
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
    for record in resp.json()['data']:
        if record['id'] == 1:
            assert record['first_name'] == "George", \
                "Data not matched! Expected : George, but found : " + str(record['first_name'])
            assert record['last_name'] == "Bluth", \
                "Data not matched! Expected : Bluth, but found : " + str(record['last_name'])
