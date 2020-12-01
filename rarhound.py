import argparse
import os
import sys
from pathlib import Path
import rarfile

parser = argparse.ArgumentParser(
    prog="rarhound",
    usage="%(prog)s [options] path",
    description="List the content of a folder",
    epilog="Woof! Woof! 🐕",
)

parser.add_argument(
    "-f", "--fetch", action="store_true", help="find and unzip all RAR files from root directory provided"
)

parser.add_argument("Path", metavar="path", type=str, help="the path to list")

args = parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print("The path specified does not exist")
    sys.exit()

for path in Path(input_path).rglob('*.rar'):
    fetchRar = os.path.join(input_path, path)
    rf = rarfile.RarFile(fetchRar)
    check = rarfile.is_rarfile(fetchRar)
    needsPassword = rf.needs_password()
    name = rf.namelist()

    if args.fetch:
        print(fetchRar)
        print('is_rarfile: ', check)
        print('needs_password: ', needsPassword)
        rf.extractall()
