import json
import sys
import tempfile

from jsonschema import Draft4Validator


def load_payload():
    payload = json.load(sys.stdin)
    _, fname = tempfile.mkstemp()
    log("Logging payload to {}".format(fname))
    with open(fname, 'w') as fp:
        fp.write(json.dumps(payload))
    log(payload)
    return payload


def validate_payload(payload, schema):
    return validate_json(payload, schema)


def validate_json(input, schema):
    v = Draft4Validator(schema)

    valid = True

    for error in sorted(v.iter_errors(input), key=str):
        valid = False
        log("JSON Validation ERROR: " + error.message)

    if not valid:
        raise TypeError


def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
