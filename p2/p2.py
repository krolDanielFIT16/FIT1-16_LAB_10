import os
import shutil

try:
    os.mkdir("A_NAMES")
    os.mkdir("B_NAMES")
except FileExistsError:
    pass

for file in os.listdir("."):
    if not os.path.isfile(file):
        continue
    if file[0].lower() in ["a", "b"]:
        shutil.copyfile(file, f"{'A_NAMES' if file[0].lower() == 'a' else 'B_NAMES'}/{file}")
