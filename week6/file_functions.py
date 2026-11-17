import os


def display_chars(path, count):
    file = open(path, "r")
    char = file.read(count)
    file.close()
    return char


def display_line(path):
    file = open(path, "r")
    line = file.readline()
    file.close()
    return line


def display_text(path):
    file = open(path, "r")
    text = ""
    for line in file:
        text = text + line
    file.close()
    return text


