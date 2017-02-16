import unittest
import matcher


class TestMatcher(unittest.TestCase):
    def test_match_files_no_match(self):
        output = matcher.match_versions("release-(.*).tar.gz", ["foo", "bar"], "release-1.0.0.tar.gz")
        self.assertEqual(output, [])

    def test_match_files_one_match(self):
        output = matcher.match_versions("release-(.*).tar.gz", ["release-1.0.0.tar.gz", "debug-0.0.1.tar.gz"],
                                        "release-1.0.0.tar.gz")
        self.assertEqual(output, ["release-1.0.0.tar.gz"])

    def test_match_files_one_match_only_latest(self):
        output = matcher.match_versions("release-(.*).tar.gz", ["release-1.0.0.tar.gz", "release-0.0.1.tar.gz"],
                                        "release-1.0.0.tar.gz")
        self.assertEqual(output, ["release-1.0.0.tar.gz"])

    def test_match_files_one_match_only_newest(self):
        output = matcher.match_versions("release-(.*).tar.gz",
                                        ["release-1.0.0.tar.gz", "release-0.0.1.tar.gz", "release-1.0.1.tar.gz"],
                                        "release-1.0.0.tar.gz")
        self.assertEqual(output, ["release-1.0.0.tar.gz", "release-1.0.1.tar.gz"])
