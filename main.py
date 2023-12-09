import os
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Minecraft Mod Switcher")

SCREEN_WITH = 300
SCREEN_HEIGHT = 40

#set window attrabutes.
root.resizable(False, False)
root.attributes('-topmost', 1)
root.geometry(str(SCREEN_WITH)+"x"+str(SCREEN_HEIGHT))
root.iconbitmap('./assets/icon.ico')



#change the working directory to .minecraft
os.chdir(os.getenv('APPDATA')+'/.minecraft/')

#list the folders that exist
def list_paths(path):
    directories = [x[1] for x in os.walk(path)]
    non_empty_dirs = [x for x in directories if x]
    return [item for subitem in non_empty_dirs for item in subitem]

#make the array of folders and remove the folder "_bclib_deactivated"
Folders = list_paths("mods/")
print(Folders)
ModFolders = []
for i in Folders:
    print(i)
    NumFiles = 0
    if i != '_bclib_deactivated':
        ModFolders.append(i)
        if not os.path.exists("mods/" + i + "/check.txt"):
            if os.path.exists('mods/check.txt'):
                with open('mods/check.txt') as d:
                    lines = d.readlines()
                    print(lines[0] + " " + i)
                if lines[0] != i:
                    with open("mods/" + i + "/check.txt","w") as f:
                        f.write(i)
            else:
                with open("mods/" + i + "/check.txt","w") as f:
                    f.write(i)
ModFolders.append("Nothing")
print(ModFolders)


    
    

def selectedSomthing(event):
    if os.path.exists('mods/check.txt'):
        with open('mods/check.txt') as d:
            lines = d.readlines()
            print(lines[0])
        for g in os.listdir("mods/"):
            if os.path.isfile("mods/"+g):
                os.rename("mods/" + g, "mods/" + lines[0] + "/" + g)
    if selectedFolder.get() != "Nothing":
        print("/mods/" + selectedFolder.get() + "/")
        for a in os.listdir("mods/" + selectedFolder.get() + "/"):
            #print(a)
            os.rename("mods/" + selectedFolder.get() + "/" + a, "mods/" + a)



selectedFolder = tk.StringVar()
selectedFolder_cb = ttk.Combobox(root, textvariable=selectedFolder)
selectedFolder_cb['values'] = ModFolders
selectedFolder_cb['state'] = 'readonly'
selectedFolder_cb.pack(fill = tk.BOTH, expand = True)
selectedFolder_cb.bind('<<ComboboxSelected>>', selectedSomthing)

root.mainloop()
