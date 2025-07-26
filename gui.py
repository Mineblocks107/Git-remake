import customtkinter as ctk
import tkinter.filedialog as tkfld
import init
import os
from CTkMenuBar import *

class GitRemArg:
    def __init__(self):
        self.reinit = False

root = ctk.CTk()
root.geometry("400x300")
root.title("GUI for gitrem")
repoDir = None

def newRepo():
    repoDir = tkfld.askdirectory()
    os.chdir(repoDir)
    init_args = GitRemArg()
    init_args.reinit = True
    init.__init(init_args)
    openRepo(repoDir)
    
    
def openRepo(dir = None):
    global repoDir
    if dir:
        repoDir = dir
    else:
        repoDir = tkfld.askdirectory()
    os.chdir(repoDir)
    updateLabelOnOpen()

def updateLabelOnOpen():
    global repoDir
    if repoDir:
        file_loc.configure(text="Current Repo: " + repoDir)
    else:
        file_loc.configure(text="Please select a repository.")
    
toolbar = CTkMenuBar(root)
toolbar.pack(side="top", fill="x", padx=0, pady=0) # Adjust padding as needed

file_btn = toolbar.add_cascade("File")
file_menu = CustomDropdownMenu(widget=file_btn)
file_menu.add_option(option="New", command=newRepo)
file_menu.add_option(option="Open", command=openRepo)
file_menu.add_separator()
file_menu.add_option(option="Exit", command=root.destroy)

file_loc = ctk.CTkLabel(root, text="Current Repo: " + (repoDir if repoDir else "Please select a repository."))
file_loc.pack(side="top", fill="x", padx=10, pady=10)


root.config(menu=toolbar)
root.mainloop()