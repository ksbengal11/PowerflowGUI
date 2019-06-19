import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = 'C:/Users/karan/AppData/Local/Programs/Python/Python36/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/karan/AppData/Local/Programs/Python/Python36/tcl/tk8.6'

buildOptions = dict(
	packages = ["pkg_resources._vendor", "tkinter", "numpy", 'scipy'],
	excludes = ['scipy.spatial.cKDTree'],
	include_files = ['C:/Users/karan/AppData/Local/Programs/Python/Python36/DLLs/tcl86t.dll', 'C:/Users/karan/AppData/Local/Programs/Python/Python36/DLLs/tk86t.dll']
	)

executables = [Executable('main.py')]

setup(name='Loadflow',
	version='1.0',
	description='',
	options=dict(build_exe=buildOptions),
	executables=executables)