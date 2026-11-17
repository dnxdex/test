import os


def search_books(path):
    print("searching...")
    sections = ""
    books = "Books:\n"
    file = open(path, "r")
    for line in file:
        if line.startswith("Section:"):
            sections += line
        else:
            books += line
    file.close()
    print("Done")
    return f"{sections}\n\n{books}"


def save(path, content):
    print("saving...", end="")
    file = open(path, "w")
    file.write(content)
    print(" Done")


data = search_books("books.txt")
save("books.txt", data)
