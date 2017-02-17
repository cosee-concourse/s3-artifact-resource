import sys
from io import StringIO


def mock_stderr():
    io = StringIO()
    sys.stderr = io
    return io


def mock_stdout():
    io = StringIO()
    sys.stdout = io
    return io


def read_from_io(io):
    io.seek(0)
    return io.read()


def put_stdin(content):
    sys.stdin = StringIO(content)