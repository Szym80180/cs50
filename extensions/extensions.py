filename = input("File name:")
filename = filename.strip().lower()

def PrintExtension(filename):
    extension = None
    for i in range(len(filename)):
        if filename[i] == ".":
            extension = filename[i+1:]

    if not extension:
        print("application/octet-stream")
        return

    if extension == "png":
        print(f"image/{extension}")
    elif extension == "gif":
        print(f"image/{extension}")
    elif extension == "jpg":
        print(f"image/jpeg")
    elif extension == "jpeg":
        print(f"image/{extension}")
    elif extension == "pdf":
        print(f"application/{extension}")
    elif extension == "zip":
        print(f"application/{extension}")
    elif extension == "txt":
        print("text/plain")
    else:
        print("application/octet-stream")

PrintExtension(filename)
