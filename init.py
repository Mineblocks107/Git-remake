import os
import shutil
import error

def init(args):
    try:
        if args.reinit == True:
            shutil.rmtree("./__gitrem/")
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