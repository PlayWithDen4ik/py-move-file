from os import makedirs, remove


def move_file(command: str) -> None:
    cm, source, dest = command.split()
    if cm != "mv":
        return
    try:
        with open(source, "r") as file1, open(dest, "w") as file2:
            file2.write(file1.read())
            remove(source)
    except FileNotFoundError:
        makedirs("/".join(dest.split("/")[:-1]), exist_ok=True)
        with open(source, "r") as file1, open(dest, "w") as file2:
            file2.write(file1.read())
            remove(source)
    else:
        return
