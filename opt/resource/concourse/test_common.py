import unittest

import schemas
from concourse import common
from concourse import testutil


class TestCommon(unittest.TestCase):
    check_payload = ('{"source":{'
                     '"bucket":"bucketName",'
                     '"access_key_id":"apiKey123",'
                     '"secret_access_key":"secretKey321",'
                     '"region_name":"eu-west-1",'
                     '"filename":"release-'
                     '"},'
                     '"version":{"version":"version-v1-dev"}}')
    check_payload_without_version = ('{"source":{'
                                     '"bucket":"bucketName",'
                                     '"access_key_id":"apiKey123",'
                                     '"secret_access_key":"secretKey321",'
                                     '"region_name":"eu-west-1",'
                                     '"filename":"release-'
                                     '"}}')
    invalid_payload = ('{"sourcez":{'
                       '"bucket":"bucketName",'
                       '"access_key_id":"apiKey123",'
                       '"secret_access_key":"secretKey321",'
                       '"region_name":"eu-west-1",'
                       '"filename":"release-'
                       '"},'
                       '"version":{"version":"version-v1-dev"}}')

    def test_get_payload(self):
        testutil.put_stdin(self.check_payload)
        result = common.load_payload()
        self.assertEqual(result['source']['access_key_id'], "apiKey123")
        self.assertEqual(result['source']['secret_access_key'], "secretKey321")
        self.assertEqual(result['source']['region_name'], "eu-west-1")
        self.assertEqual(result['source']['filename'], "release-")
        self.assertEqual(result['version']['version'], "version-v1-dev")

    def test_validates_json_valid_result(self):
        testutil.put_stdin(self.check_payload)
        payload = common.load_payload()

        try:
            common.validate_payload(payload, schemas.checkSchema)
        except TypeError:
            self.fail("Valid JSON detected as invalid")

    def test_validates_json_valid_result_without_version(self):
        testutil.put_stdin(self.check_payload_without_version)
        payload = common.load_payload()

        try:
            common.validate_payload(payload, schemas.checkSchema)
        except TypeError:
            self.fail("Valid JSON detected as invalid")

    def test_validates_json_invalid_result(self):
        testutil.put_stdin(self.invalid_payload)
        payload = common.load_payload()

        with self.assertRaises(TypeError):
            common.validate_payload(payload, schemas.checkSchema)

    def test_log_on_stderr(self):
        io = testutil.mock_stderr()
        common.log("Some Test Log")
        self.assertEqual("Some Test Log", testutil.read_from_io(io))


if __name__ == '__main__':
    unittest.main()
