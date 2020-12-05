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

print("Woof! Woof! 🐕")

for path in Path(input_path).rglob("*.rar"):
    fetchRar = os.path.join(input_path, path)
    getDirectory = os.path.split(path)[0]
    rf = rarfile.RarFile(fetchRar)
    name = rf.namelist()

    if args.fetch:
        print("sniff...sniff...Woof!", name[0])
        rf.extractall(getDirectory)

print("Woof! 🐕")
