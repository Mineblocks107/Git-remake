import os
import shutil
import error

def __init(args):
    try:
        if args.reinit == True:
            rem()
        os.mkdir("./__gitrem/")
        open("./__gitrem/__config.gitrem", "w").write("")
        os.mkdir("./__gitrem/__branch/")
        os.mkdir("./__gitrem/__branch/main/")
        os.mkdir("./__gitrem/__branch/main/__commits")
        os.mkdir("./__gitrem/__branch/main/__stagingArea")
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
