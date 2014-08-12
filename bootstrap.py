#!/usr/bin/env python

# script to install the git utils

import os, sys, argparse
import shutil
from distutils.spawn import find_executable

# default variables
default_install = os.path.dirname(find_executable('git'))
default_generator = 'html' if sys.platform == 'win32' else 'man'
actions = ['install', 'uninstall', 'generate']

# command line parser
parser = argparse.ArgumentParser()
parser.description = """
Script that aids in the installation of git-utils along with the generation of
documentation for the git-utils. The default installation path for this system
is set to {ins}. The generator used for this system is set to {gen}. Generating
man pages or html required pandoc to be installed and findable through PATH.
""".format(ins=default_install, gen=default_generator)

parser.add_argument('action', help='specify what action to take', choices=actions)
parser.add_argument('--install-dir', metavar='<dir>', help='specifies path to the installed scripts', default=default_install)
parser.add_argument('--quiet', action='store_true', help='do not explain what is being done')
args = parser.parse_args()

# change working directory
os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))

def explain(msg):
    if not args.quiet:
        print(msg)

if args.action == 'install':
    # install utils by copying the script files
    # to the install directory
    for script in os.listdir('scripts'):
        p = os.path.join('scripts', script)
        explain('copying file from {} to {}'.format(p, args.install_dir))
        shutil.copy2(p, args.install_dir)

elif args.action == 'uninstall':
    # remove the files
    for script in os.listdir('scripts'):
        p = os.path.join(args.install_dir, script)
        explain('removing {}'.format(p))
        os.remove(p)
elif args.action == 'generate':
    print('generate action is currently unsupported')
