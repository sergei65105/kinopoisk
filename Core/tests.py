
class HTTPRequest:
    def __init__(self, request_text: str):
        self.headers = None
        self.body = None
        self.parse_request(request_text)
    def parse_request(self, request_text):
        request_text = request_text.split('\n')
        print(request_text)
        self.headers = request_text[2]
        self.body = request_text[4]

request = HTTPRequest('''
HEADER
123
BODY
321
''')
if True:
    pass
else:
    pass
print(1 == 2)