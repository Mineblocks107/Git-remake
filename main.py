import argparse
import init
import add

parser = argparse.ArgumentParser(description="A git remake done by mineblocks")

parser = argparse.ArgumentParser(description="Command dispatcher")
subparsers = parser.add_subparsers(dest='command', required=True)

init_parser = subparsers.add_parser('init', help='Initialize the repository')

add_parser = subparsers.add_parser('add', help='Add items to the staging area')
add_parser.add_argument('values', nargs="*", help='Files')

args = parser.parse_args()


branch = None

if args.command == 'init':
    init.init()
elif args.command == 'add':
    add.add(args.values)