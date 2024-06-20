from requests import RequestException


class RobogramException(Exception):

    def __init__(self, msg: str, e: RequestException = None):
        self.msg = msg

        if e:
            self.request = e.request
            self.response = e.response
        else:
            self.request = self.response = None
