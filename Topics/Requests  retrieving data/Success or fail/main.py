import requests


def check_success(url):
    r = requests.get(url)
    if r:
        return 'Success'
    return 'Fail'
