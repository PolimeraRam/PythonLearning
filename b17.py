import pathlib
import zipfile

def zip_files_with_subfolders(file_paths, zipfoldername):
    p = pathlib.Path(zipfoldername, "Compressed.zip")
    with zipfile.ZipFile(p, "w") as archive:
        for path in file_paths:
            archive.write(path)


def zip_files(file_paths, zipfoldername):
    p = pathlib.Path(zipfoldername, "Compressed.zip")
    with zipfile.ZipFile(p, "w") as archive:
        for path in file_paths:
            path = pathlib.Path(path)
            archive.write(path, arcname=path.name)

if __name__ == "__main__":
    zip_files_with_subfolders(["test.py","main.py"], "output")

