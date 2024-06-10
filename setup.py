from cx_Freeze import setup, Executable
base = None

options = {
    'build_exe': {    
        'packages = pyperclip tkinter ttk
    },
}

setup(
    name = sims4code ,
    options = options,
    version = "1.0",
    description = 'Voici mon programme',
    executables = sims4code.py
)