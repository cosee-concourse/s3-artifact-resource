import json
import model


def check_output(versions):
    if versions is None:
        return json.dumps([])
    else:
        version_dictionary = []
        for version in versions:
            version_dictionary.append({model.VERSION_JSON_NAME: version})
        return json.dumps(version_dictionary)


def inout_output(version):
    return json.dumps({"version": {model.VERSION_JSON_NAME: version}})
