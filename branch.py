import error
import os
import extrafunc
import shutil

def changeBranch(args):
    try:
        f = open("./__gitrem/__config.gitrem").read().splitlines()
        f[1] = "branch = " + str(args)
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

def writeNewBranch(branch):
    branchpath = ".\\__gitrem\\" + extrafunc.pad_path(branch, "__branch")
    os.makedirs(branchpath + "\\__commits\\", exist_ok=True)
    os.makedirs(branchpath + "\\__stagingArea\\", exist_ok=True)
    changeBranch(branch)

def removeBranch(branch):
    if branch and branch != "main":
        branchpath = ".\\__gitrem\\" + extrafunc.pad_path(branch, "__branch")
        shutil.rmtree(branchpath)

def branch(args):
    if args.c:
        changeBranch(args.c)
    if args.a:
        writeNewBranch(args.a)
    if args.d:
        removeBranch(readBranch())