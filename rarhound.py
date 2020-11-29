import argparse
import os
import sys

parser = argparse.ArgumentParser(
    prog="rarhound",
    usage="%(prog)s [options] path",
    description="List the content of a folder",
    epilog="Woof! Woof! 🐕",
)

parser.add_argument(
    "-f", "--fetch", action="store_true", help="find RAR files from directory provided"
)

parser.add_argument("Path", metavar="path", type=str, help="the path to list")

args = parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print("The path specified does not exist")
    sys.exit()

for folder in os.listdir(input_path):
    if args.fetch:
        print(folder)
        #     size = os.stat(os.path.join(input_path, folder)).st_size
        #     folder = '%10d  %s' % (size, folder)
        # print(folder)
