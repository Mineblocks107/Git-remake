import argparse
import init

parser = argparse.ArgumentParser(description="A git remake done by mineblocks")

parser = argparse.ArgumentParser(description="Command dispatcher")
subparsers = parser.add_subparsers(dest='command', required=True)

init_parser = subparsers.add_parser('init', help='Initialize the repository')

add_parser = subparsers.add_parser('add', help='Add items to the staging area')
add_parser.add_argument('-f', action='store_true', help='Enable f flag')
add_parser.add_argument('value', help='Direct positional value')

args = parser.parse_args()

if args.command == 'init':
    init.init()
elif args.command == 'add':
    pass