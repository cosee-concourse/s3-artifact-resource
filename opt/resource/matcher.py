import re
import semver


def match_versions(regexp, files, version_request):
    matched_versions = []
    extracted_version_request = re.search(regexp, version_request).group(1)
    for version in files:
        if not (re.match(regexp, version) is None):
            extracted_version = re.search(regexp, version).group(1)
            if semver.compare(extracted_version, extracted_version_request) >= 0:
                matched_versions.append(version)
    return matched_versions