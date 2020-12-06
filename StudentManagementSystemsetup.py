from cx_Freeze import *
import sys
includefiles=["student.ico.ico"]
excludes=[]
packages=[]
base=None
if sys.platform == "win32":
    base="Win32GUI"

shortcut_table = [
    ("DesktopShortcut", # shortcut
     "DesktopFolder", #Directory_
     "StudentManagementSystem", #Name
     "TARGETDIR", #Component_
     "[TARGETDIR]\studentmanagementsystem.exe",
     None, #Arguments
     None, #Description
     None, #Hotkey
     None, #Icon
     None, #IconIndex
     None, #Showcmd
     "TARGETDIR", #WkDir
    )
]

msi_data = {"Shortcut":shortcut_table}

bdist_msi_options = {"data":msi_data}
setup(
    version="0.1",
    description="Student Management System Developed By Gandhar Yedsikar",
    author="Gandhar Yedsikar",
    name="Student Management System",
    options={'build_exe':{'include_files':includefiles},"bdist_msi":bdist_msi_options,},
    executables=[
        Executable(
            script="studentmanagementsystem.py",
            base=base,
            icon="student.ico.ico",
        )
    ]

)