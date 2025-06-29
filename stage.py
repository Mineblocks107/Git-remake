import shutil
import extrafunc
import branch
import os

def add(args):
    for arg in args:
        pastepath = ".\\__gitrem\\" + extrafunc.pad_path(branch.readBranch(), "__branch") + "\\__stagingArea\\" + arg
        shutil.copyfile(arg, pastepath)
    print("Added:", *args)

def rem(args):
    for arg in args:
        delpath = ".\\__gitrem\\" + extrafunc.pad_path(branch.readBranch(), "__branch") + "\\__stagingArea\\" + arg
        os.remove(delpath)
    print("Removed:", *args)

def stage(args):
    if args.a:
        add(args.a)
    if args.r:
        rem(args.r)
