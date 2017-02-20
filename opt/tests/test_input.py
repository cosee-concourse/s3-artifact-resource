import unittest
from unittest.mock import patch

import input
import payloads
from concourse import testutil


class TestInput(unittest.TestCase):
    def test_invalid_json(self):
        testutil.put_stdin('{"sourcez":{'
                           '"apiKey":"apiKey123",'
                           '"secretKey":"secretKey321'
                           '"},'
                           '"version":{"version":"version-v1-dev"}}')

        self.assertEqual(input.execute(""), -1)

    def test_without_version(self):
        testutil.put_stdin(payloads.in_payload_without_version)
        io = testutil.mock_stderr()
        self.assertEqual(-1, input.execute(""))
        self.assertRegex(testutil.read_from_io(io), "JSON Validation ERROR: 'version' is a required property")

    @patch('input.S3Client')
    def test_valid_json_invalid_credentials_or_bucket_does_not_exist(self, mock_s3client):
        # Mock Setup
        mock_returned_s3client = mock_s3client()
        mock_returned_s3client.does_bucket_exist.return_value = False

        testutil.put_stdin(payloads.in_payload)
        self.assertEqual(-1, input.execute(""))

    @patch('input.os.remove')
    @patch('input.archive_util')
    @patch('input.S3Client')
    def test_valid_json(self, mock_s3client, mock_archive_util, mock_os_remove):
        # Mock Setup
        mock_returned_s3client = mock_s3client()
        mock_returned_s3client.does_bucket_exist.return_value = True

        io = testutil.mock_stdout()
        testutil.put_stdin(payloads.in_payload)
        self.assertEqual(0, input.execute("some/destination"))

        filename = "some/destination/release-1.0.0.tar.gz"

        # Mock Assertions
        mock_returned_s3client.download_file.assert_called_once_with("bucketName", "release-1.0.0.tar.gz", filename)
        mock_archive_util.uncompress_file.assert_called_once_with(filename, "some/destination")
        mock_os_remove.assert_called_once_with(filename)

        self.assertEqual('{"version": {"version": "release-1.0.0.tar.gz"}}', testutil.read_from_io(io))

if __name__ == '__main__':
    unittest.main()
