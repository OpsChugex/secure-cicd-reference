import json
import unittest
from threading import Thread
from urllib.request import urlopen

from app import Handler, ThreadingHTTPServer


class HealthTest(unittest.TestCase):
    def test_health_endpoint(self):
        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        port = server.server_address[1]
        Thread(target=server.serve_forever, daemon=True).start()
        try:
            with urlopen(f"http://127.0.0.1:{port}/health", timeout=5) as response:
                self.assertEqual(response.status, 200)
                payload = json.loads(response.read().decode("utf-8"))
            self.assertEqual(payload["status"], "ok")
            self.assertEqual(payload["service"], "ocx-cicd-reference")
        finally:
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
    unittest.main()
