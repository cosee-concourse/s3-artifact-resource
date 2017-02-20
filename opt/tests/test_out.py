import unittest
from unittest.mock import patch

import out
import payloads
from concourse import testutil


class TestOut(unittest.TestCase):
    def test_invalid_json(self):
        testutil.put_stdin('{"sourcez":{'
                           '"apiKey":"apiKey123",'
                           '"secretKey":"secretKey321'
                           '"},'
                           '"version":{"version":"version-v1-dev"}}')

        self.assertEqual(out.execute(""), -1)

    @patch('out.S3Client')
    def test_valid_json_invalid_credentials_or_bucket_does_not_exist(self, mock_s3client):
        # Mock Setup
        mock_returned_s3client = mock_s3client()
        mock_returned_s3client.does_bucket_exist.return_value = False

        testutil.put_stdin(payloads.out_payload)
        self.assertEqual(-1, out.execute(""))

    @patch('out.os.remove')
    @patch('out.io_util')
    @patch('out.archive_util')
    @patch('out.S3Client')
    def test_valid_json(self, mock_s3client, mock_archive_util, mock_io_util, mock_os_remove):
        # Mock Setup
        mock_returned_s3client = mock_s3client()
        mock_returned_s3client.does_bucket_exist.return_value = True
        mock_io_util.read_file.return_value = "1.0.1"

        testutil.put_stdin(payloads.out_payload)

        io = testutil.mock_stdout()
        self.assertEqual(0, out.execute("some/directory"))

        # Mock Assertions
        mock_io_util.read_file.assert_called_once_with("some/directory/version/name")
        mock_archive_util.compress_folder.assert_called_once_with("release-1.0.1.tar.gz", "some/directory/artifact/")
        mock_returned_s3client.upload_file.assert_called_once_with("bucketName", "release-1.0.1.tar.gz", "some/directory/artifact/release-1.0.1.tar.gz")
        mock_os_remove.assert_called_once_with("some/directory/artifact/release-1.0.1.tar.gz")

        self.assertEqual('{"version": {"version": "release-1.0.1.tar.gz"}}', testutil.read_from_io(io))


if __name__ == '__main__':
    unittest.main()
