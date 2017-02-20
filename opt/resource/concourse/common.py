import json
import sys
import tempfile
from enum import Enum

from jsonschema import Draft4Validator


def load_payload():
    payload = json.load(sys.stdin)
    _, fname = tempfile.mkstemp()
    log_info("Logging payload to {}".format(fname))
    with open(fname, 'w') as fp:
        fp.write(json.dumps(payload))
    log_info(payload)
    return payload


def validate_payload(payload, schema):
    return validate_json(payload, schema)


def validate_json(input, schema):
    v = Draft4Validator(schema)

    valid = True

    for error in sorted(v.iter_errors(input), key=str):
        valid = False
        log_error("JSON Validation ERROR: " + error.message)

    if not valid:
        raise TypeError


def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def log_error(message):
    log(Fore.RED + str(message))


def log_warning(message):
    log(Fore.YELLOW + str(message))


def log_info(message):
    log(Fore.BLUE + str(message))


class Fore(Enum):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    RESET = 39
