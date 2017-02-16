import json
import sys
import tempfile


def get_payload():
    payload = json.load(sys.stdin)
    _, fname = tempfile.mkstemp()
    log("Logging payload to {}".format(fname))
    with open(fname, 'w') as fp:
        fp.write(json.dumps(payload))
    log(payload)
    return payload

def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)