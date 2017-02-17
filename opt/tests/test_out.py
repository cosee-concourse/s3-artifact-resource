import unittest

import out
from concourse import test_common


class TestInput(unittest.TestCase):

    def test_invalid_json(self):
        test_common.put_stdin('{"sourcez":{'
                               '"apiKey":"apiKey123",'
                               '"secretKey":"secretKey321'
                               '"},'
                               '"version":{"version":"version-v1-dev"}}')

        self.assertEqual(out.execute(""), -1)


if __name__ == '__main__':
    unittest.main()
