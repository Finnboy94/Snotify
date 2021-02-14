from cx_Freeze import setup, Executable
base = "Win32GUI"
executables = [Executable("snotify.py", base=base)]
packages = ["SwSpotify","time","win10toast"]
options = {
    'build_exe': {
        'packages':packages,
        'include_files': ['snotify.ico'],
        'include_msvcr': True,
    },
}

setup(
    name = "Snotify",
    options = options,
    version = "1.0",
    description = 'Snotify',
    executables = executables
)
