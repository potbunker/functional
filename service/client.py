import requests


class Client(object):
    def __init__(self, name, url, version):
        self._name = name
        self._url = url
        self._version = version

    def invoke(self, request):
        with requests.Session() as session:
            response = session.post(url=self._url, data=request)
            return response.text

