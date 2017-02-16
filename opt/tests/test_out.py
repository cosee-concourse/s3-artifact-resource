import unittest

import out
from concourse_common import common_tests


class InputTests(unittest.TestCase):

    def test_invalid_json(self):
        common_tests.put_stdin('{"sourcez":{'
                               '"apiKey":"apiKey123",'
                               '"secretKey":"secretKey321'
                               '"},'
                               '"version":{"version":"version-v1-dev"}}')

        self.assertEqual(out.execute(""), -1)


if __name__ == '__main__':
    unittest.main()
