import shutil
import extrafunc
import branch

def add(args):
    for arg in args:
        pastepath = ".\\__gitrem\\" + extrafunc.pad_path(branch.readBranch(), "__branch") + "\\__stagingArea\\" + arg
        shutil.copyfile(arg, pastepath)
    print("Added:", *args)

def stage(args):
    if args.a:
        add(args.a)
