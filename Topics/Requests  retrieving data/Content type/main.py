import requests


def get_content_type(url):
    response = requests.get(url)
    return response.headers['Content-Type']
