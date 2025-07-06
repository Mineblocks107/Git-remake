import argparse
import init
import stage
import branch

parser = argparse.ArgumentParser(description="A git remake done by mineblocks")

parser = argparse.ArgumentParser(description="Command dispatcher")
subparsers = parser.add_subparsers(dest='command', required=True)

init_parser = subparsers.add_parser('init', help='Initialize the repository')
init_parser.add_argument('--reinit', action='store_true', help='Re-initialize repository')
init_parser.add_argument('-d', action='store_true', help='Re-initialize repository')
init_parser.add_argument('-i', action='store_true', help='Re-initialize repository')

stage_parser = subparsers.add_parser('stage', help='Deals with staging area')
stage_parser.add_argument('-a', nargs="*", help='Adds files to the staging area')
stage_parser.add_argument('-r', nargs="*", help='Removes files from the staging area')


branch_parser = subparsers.add_parser('branch', help='Deals with branches')
branch_parser.add_argument('-c', type=str, help='Changes the selected branch')
branch_parser.add_argument('-a', type=str, help='Adds the branch')
branch_parser.add_argument('-d', action="store_true", help='Adds the branch')


args = parser.parse_args()

if args.command == 'init':
    init.init(args)
elif args.command == 'stage':
    stage.stage(args)
elif args.command == 'branch':
    branch.branch(args)