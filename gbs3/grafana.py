import requests

from gbs3.settings import *

HTTP_GET_HEADERS = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + GRAFANA_TOKEN
}

HTTP_POST_HEADERS = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + GRAFANA_TOKEN,
    'Content-Type': 'application/json'
}


def get(url):
    return requests.get(GRAFANA_URL + url, headers=HTTP_GET_HEADERS)


def post(url, json_payload):
    return requests.post(GRAFANA_URL + url, headers=HTTP_POST_HEADERS,
                         data=json_payload)


def all_dashboards():
    r = get('/api/search')
    r.raise_for_status()
    return r.json()


def get_dashboard(dashboard_uri):
    r = get('/api/dashboards/{}'.format(dashboard_uri))
    r.raise_for_status()
    return r.json()


def create_or_update_dashboard(json_payload):
    r = post("/api/dashboards/db", json_payload)
    r.raise_for_status()
    return r.json()


def datasources():
    r = get('/api/datasources')
    r.raise_for_status()
    return r.json()


def create_datasource(json_payload):
    r = post("/api/datasources", json_payload)
    r.raise_for_status()
    return r.json()
