import unittest

from concourse import testutil

from model import Model, Request
import payloads


class TestModel(unittest.TestCase):
    def setUpGetterTest(self, payload, request):
        testutil.put_stdin(payload)
        self.model = Model(request)

    def test_get_access_key(self):
        self.setUpGetterTest(payloads.check_payload, Request.CHECK)
        api_key = self.model.get_access_key()
        self.assertEqual(api_key, "apiKey123")

    def test_get_secret_key(self):
        self.setUpGetterTest(payloads.check_payload, Request.CHECK)
        secret_key = self.model.get_secret()
        self.assertEqual(secret_key, "secretKey321")

    def test_get_bucket(self):
        self.setUpGetterTest(payloads.check_payload, Request.CHECK)
        bucket = self.model.get_bucket()
        self.assertEqual(bucket, "bucketName")

    def test_get_region_name(self):
        self.setUpGetterTest(payloads.check_payload, Request.CHECK)
        region_name = self.model.get_region_name()
        self.assertEqual(region_name, "eu-west-1")

    def test_get_filename(self):
        self.setUpGetterTest(payloads.check_payload, Request.CHECK)
        file = self.model.get_filename()
        self.assertEqual(file, "release-")

    def test_get_version_file(self):
        self.setUpGetterTest(payloads.out_payload, Request.OUT)
        version = self.model.get_version_file()
        self.assertEqual(version, "version/name")

    def test_get_folderpath(self):
        self.setUpGetterTest(payloads.out_payload, Request.OUT)
        folderpath = self.model.get_folderpath()
        self.assertEqual(folderpath, "artifact/")

    def test_get_version(self):
        self.setUpGetterTest(payloads.check_payload, Request.CHECK)
        version = self.model.get_version()
        self.assertEqual(version, "release-1.0.0.tar.gz")


if __name__ == '__main__':
    unittest.main()
