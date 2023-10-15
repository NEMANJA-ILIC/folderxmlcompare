from xmldiff import main

# first,second=main.diff_files("folder1/books.xml", "folder2/books.xml")

# print(second)

result = main.diff_files("folder1/books.xml", "folder2/books.xml")

print(result[0].__class__.__name__)

if (result[0].__class__.__name__ == "MoveNode"):
    print("Enters")


# print(result)
