import tarfile
import os


def compress_folder(filename, folderpath):
    tar = tarfile.open(os.path.join(folderpath,filename), 'x:gz')

    for file in files(folderpath):
        tar.add(os.path.join(folderpath,file), arcname=file)
    tar.close()


def uncompress_file(filename, destination):
    tarfile.open(filename, 'r:gz').extractall(destination)


def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file
