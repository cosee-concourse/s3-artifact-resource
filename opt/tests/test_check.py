import unittest
from unittest.mock import patch, call, MagicMock

import check
import payloads
from concourse import testutil


class TestCheck(unittest.TestCase):
    def test_invalid_json(self):
        testutil.put_stdin('{"sourcez":{'
                           '"apiKey":"apiKey123",'
                           '"secretKey":"secretKey321'
                           '"},'
                           '"version":{"version":"version-v1-dev"}}')

        self.assertEqual(-1, check.execute())

    @patch('check.S3Client')
    def test_valid_json_without_version(self, mock_class):
        mock_class.does_bucket_exist.return_value = True
        io = testutil.mock_stdout()
        testutil.put_stdin(payloads.check_payload_without_version)
        self.assertEqual(0, check.execute())
        self.assertEqual("[]\n", testutil.read_from_io(io))

    @patch('check.matcher')
    @patch('check.S3Client')
    def test_valid_json(self, mock_s3client, mock_matcher):
        mock_returned_s3client = mock_s3client()
        mock_s3client.does_bucket_exist.return_value = True
        mock_matcher.match_versions.return_value = ['release-1.0.0.tar.gz', 'release-1.0.1.tar.gz']

        io = testutil.mock_stdout()
        testutil.put_stdin(payloads.check_payload)

        self.assertEqual(0, check.execute())

        mock_s3client.assert_called_with("apiKey123", "secretKey321", "eu-west-1")

        mock_returned_s3client.does_bucket_exist.assert_called_with('bucketName')
        mock_returned_s3client.list_files.assert_called_with('bucketName')

        mock_matcher.match_versions.assert_called_once_with("release-(.*).tar.gz", unittest.mock.ANY,
                                                            "release-1.0.0.tar.gz")

        self.assertEqual('[{"version": "release-1.0.0.tar.gz"}, {"version": "release-1.0.1.tar.gz"}]\n',
                         testutil.read_from_io(io))


if __name__ == '__main__':
    unittest.main()
