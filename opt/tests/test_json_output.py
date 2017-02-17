import unittest

from util import json_output


class TestJsonOutput(unittest.TestCase):
    def test_check_output_empty_version(self):
        output = json_output.check_output(None)
        self.assertEqual(output, "[]")

    def test_check_output_with_version(self):
        output = json_output.check_output(["version-v1-dev"])
        self.assertEqual(output, '[{"version": "version-v1-dev"}]')

    def test_check_output_with_multiple_versions(self):
        output = json_output.check_output(["1.0.0", "1.0.1"])
        self.assertEqual(output, '[{"version": "1.0.0"}, {"version": "1.0.1"}]')

    def test_outin_output(self):
        output = json_output.inout_output("version-v1-dev")
        self.assertEqual(output, '{"version": {"version": "version-v1-dev"}}')