import unittest

import input
from concourse_common import common_tests


class InputTests(unittest.TestCase):
    def test_invalid_json(self):
        common_tests.put_stdin('{"sourcez":{'
                               '"apiKey":"apiKey123",'
                               '"secretKey":"secretKey321'
                               '"},'
                               '"version":{"version":"version-v1-dev"}}')

        self.assertEqual(input.execute(""), -1)

if __name__ == '__main__':
    unittest.main()
