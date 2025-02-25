import os
import shutil
import sys

from tox.run import run

# -------------------------------------------------------------

def main():
    cwd = os.getcwd()
    os.environ['REPO_DIRPATH'] = cwd
    os.environ['TOX_ENVNAME'] = os.path.basename(cwd)
    mode = 'pkg' if is_package(dirpath=cwd) else 'req'
    script_dirpath = os.path.dirname(__file__)
    tox_fpath = os.path.join(script_dirpath, 'tox.ini')

    args = ('-c', tox_fpath , '-e', mode)
    if len(sys.argv) > 1:
        args = (*args,sys.argv[1])

    build_dirpath = os.path.join(cwd, 'build')
    if os.path.isdir(build_dirpath):
        print(f'- Deleting build directory {build_dirpath}')
        shutil.rmtree(build_dirpath)

    print(f'-------------------------- Launching tox tests --------------------------')
    run(args)


def is_package(dirpath : str):
    fnames = os.listdir(dirpath)
    has_setup = 'setup.py' in fnames
    has_pyproject = 'pyproject.toml' in fnames
    return has_setup or has_pyproject

