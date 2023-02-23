import zipfile
import os

def extarct():
    file1 = "my_extension.crx"
    cmd = "7z e -aoa -o{} {}".format("temp", file1)
    os.system(cmd)
    os.system("find $PWD -name temp")
