import unittest

from concourse_common import common_tests

from model import Model


class ModelTest(unittest.TestCase):
    check_payload = ('{"source":{'
                     '"bucket":"bucketName",'
                     '"access_key_id":"apiKey123",'
                     '"secret_access_key":"secretKey321",'
                     '"region_name":"eu-west-1",'
                     '"filename":"release-'
                     '"},'
                     '"version":{"version":"version-v1-dev"}}')
    out_payload = ('{"params":{'
                   '"version":"version/name",'
                   '"folderpath":"artifact/'
                   '"},'
                   '"source":{'
                   '"bucket":"bucketName",'
                   '"access_key_id":"apiKey123",'
                   '"filename":"release-",'
                   '"secret_access_key":"secretKey321",'
                   '"region_name":"eu-west-1'
                   '"},'
                   '"version":{"version":"version-v1-dev"}}')

    def setUpGetterTest(self, payload):
        common_tests.put_stdin(payload)
        self.model = Model()

    def test_get_access_key(self):
        self.setUpGetterTest(self.check_payload)
        api_key = self.model.get_access_key()
        self.assertEqual(api_key, "apiKey123")

    def test_get_secret_key(self):
        self.setUpGetterTest(self.check_payload)
        secret_key = self.model.get_secret()
        self.assertEqual(secret_key, "secretKey321")

    def test_get_bucket(self):
        self.setUpGetterTest(self.check_payload)
        bucket = self.model.get_bucket()
        self.assertEqual(bucket, "bucketName")

    def test_get_region_name(self):
        self.setUpGetterTest(self.check_payload)
        region_name = self.model.get_region_name()
        self.assertEqual(region_name, "eu-west-1")

    def test_get_filename(self):
        self.setUpGetterTest(self.check_payload)
        file = self.model.get_filename()
        self.assertEqual(file, "release-")

    def test_get_version_file(self):
        self.setUpGetterTest(self.out_payload)
        version = self.model.get_version_file()
        self.assertEqual(version, "version/name")

    def test_get_folderpath(self):
        self.setUpGetterTest(self.out_payload)
        folderpath = self.model.get_folderpath()
        self.assertEqual(folderpath, "artifact/")

    def test_get_version(self):
        self.setUpGetterTest(self.check_payload)
        version = self.model.get_version()
        self.assertEqual(version, "version-v1-dev")


if __name__ == '__main__':
    unittest.main()
