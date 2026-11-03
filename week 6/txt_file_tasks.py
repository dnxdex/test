import os


def cwd():
    directory = os.getcwd()
    print(f"The current working directory is {directory}")
    print("the directory contains the following files:", os.listdir(directory))
    return


def run():
    print("Processing...")
    cwd()
    return
