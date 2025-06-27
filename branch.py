import error

def changeBranch(args):
    try:
        f = open("./__gitrem/__config.gitrem").read().splitlines()
        print(f)
        f[1] = "branch = " + str(args)
        print(f)
        fWrite = open("./__gitrem/__config.gitrem", "w")
        for i in f:
            fWrite.write(i + "\n")
    except FileNotFoundError:
        error.RepoNotInitialized()
def readBranch():
    try:
        f = open("./__gitrem/__config.gitrem").read().splitlines()
        return f[1][9:]
    except FileNotFoundError:
        error.RepoNotInitialized()

def branch(args):
    if args.c:
        changeBranch(args.c)
