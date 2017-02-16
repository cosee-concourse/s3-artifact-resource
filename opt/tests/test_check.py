import unittest

import check
from concourse_common import common_tests


class CheckTests(unittest.TestCase):
    def test_invalid_json(self):
        common_tests.put_stdin('{"sourcez":{'
                               '"apiKey":"apiKey123",'
                               '"secretKey":"secretKey321'
                               '"},'
                               '"version":{"version":"version-v1-dev"}}')

        self.assertEqual(check.execute(), -1)

if __name__ == '__main__':
    unittest.main()
