from time import ctime
from pathlib import Path

Path(r"C:\Program Files\Microsoft")
Path("/usr/local/bin")
Path()
Path("ecommerce/__init__.py")
Path.home()

"""
- important methods 
"""

path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.parent)
print(path.suffix)
path = path.with_name("file.txt")
print(path)
# it will give the suffix of the given extension of a file
path = path.with_suffix(".txt")

"""
    - more required methods remember to are
"""

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("rename_to")
#
out = path.iterdir()
print(out)
path = Path("ecommerce")
something = [p for p in path.iterdir()]
print(something)

"""
    - glob()
    - it gives an iterator to search recursively
"""

py_files = [p for p in path.glob("*.py")]
print(py_files)

# this search recursively
py_files = [p for p in path.glob("**/*.py")]
print(py_files)

# to be able to search more recursively we should use rglob()
py_files = [p for p in path.rglob("*.py")]
print(py_files)

"""
    - important methods to work with files
    -  path.exists()  => checks weather the file exists or not
    -  path.unlink()  => deletes the file 
    -  path.rename("newName.extension") => used to rename the file
    -  path.stat() => gives the information about the file
"""

print(ctime(path.stat().st_ctime))

"""
    - we also have 
        => path.read_bytes() --> returns the content of the file as binaries
        => path.read_text() --> returns the content of the file as text
"""

# with open("__init__.py", "r") as file
#            file_name      mode
# then you have to close it too
# and this all tasks is handled by the read_text()
