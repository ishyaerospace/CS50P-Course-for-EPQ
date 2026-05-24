with open("names.txt") as file:
    for line in file:
        print("hello,", line.rstrip()) # reads each line one at a time. no need to read all line then iterate through list
# unable to sort everything in advance.