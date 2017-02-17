import unittest

import out
from concourse import testutil


class TestInput(unittest.TestCase):

    def test_invalid_json(self):
        testutil.put_stdin('{"sourcez":{'
                               '"apiKey":"apiKey123",'
                               '"secretKey":"secretKey321'
                               '"},'
                               '"version":{"version":"version-v1-dev"}}')

        self.assertEqual(out.execute(""), -1)


if __name__ == '__main__':
    unittest.main()
