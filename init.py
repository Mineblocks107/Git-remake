import os
import shutil
import error
import branch

def __init(args):
    try:
        if args.reinit == True:
            rem()
        os.mkdir("./__gitrem/")
        branch.writeNewBranch("main")
        open("./__gitrem/__config.gitrem", "w").write("# __config.gitrem\nbranch = main")
        print("Initialized the repository.")
    except FileExistsError:
        error.RepoAlreadyInitialized()
    # except:
    #     print("Unknown error happened")

def rem():
    shutil.rmtree("./__gitrem/")


def init(args):
    if args.d:
        rem()
    if args.i:
        __init(args)
