import io


def read_file(file_path):
    return io.open(file_path, "r").read()
