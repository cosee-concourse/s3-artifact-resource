import sys
import unittest
from io import StringIO

from concourse_common import common


class CommonTest(unittest.TestCase):
    check_payload = ('{"source":{'
                     '"bucket":"bucketName",'
                     '"access_key":"apiKey123",'
                     '"secret_access_key":"secretKey321",'
                     '"region_name":"eu-west-1",'
                     '"regexp":"directory_on_s3/release-(.*).tar.gz'
                     '"},'
                     '"version":{"version":"version-v1-dev"}}')

    def test_getPayload(self):
        put_stdin(self.check_payload)
        result = common.get_payload()
        self.assertEqual(result['source']['access_key'], "apiKey123")
        self.assertEqual(result['source']['secret_access_key'], "secretKey321")
        self.assertEqual(result['source']['region_name'], "eu-west-1")
        self.assertEqual(result['source']['regexp'], "directory_on_s3/release-(.*).tar.gz")
        self.assertEqual(result['version']['version'], "version-v1-dev")


def put_stdin(content):
    sys.stdin = StringIO(content)

if __name__ == '__main__':
    unittest.main()
