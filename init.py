import os
from error import *

def init():
    try:
        os.mkdir("./__gitrem/")
        os.mkdir("./__gitrem/branch/")
        os.mkdir("./__gitrem/branch/main/")
        os.mkdir("./__gitrem/branch/main/__commits")
        os.mkdir("./__gitrem/branch/main/__stagingArea")
    except FileExistsError:
        raise RepoAlreadyInitialized("Repository has already been initialized")
    except:
        raise Exception("Unknown error happened")
    print("Initialized the repository.")
    