#It is server's mock for test
import requests


class MockServer:
    def Get200Code(self):
        return requests.get("http://httpstat.us/200")

    def Get400Code(self):
        return requests.get("http://httpstat.us/400")

    def Get500Code(self):
        return requests.get("http://httpstat.us/500")
