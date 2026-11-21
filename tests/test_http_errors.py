import unittest

import requests

from sb_cli.utils import verify_response


class ResponseTests(unittest.TestCase):
    def test_bad_gateway_preserves_status_without_json_message(self):
        for body in (b"", b"Bad Gateway", b"[]"):
            with self.subTest(body=body):
                response = requests.Response()
                response.status_code = 502
                response.reason = "Bad Gateway"
                response._content = body
                with self.assertRaisesRegex(requests.RequestException, "502: Bad Gateway"):
                    verify_response(response)
