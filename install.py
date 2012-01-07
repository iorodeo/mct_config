#!/usr/bin/env python
from __future__ import print_function
import os
import os.path
import shutil

setup_file = 'mct_setup.bash'
usr_bin = os.path.join(os.environ['HOME'],'bin')
config_dir, dummpy = os.path.split(__file__)

# Create bin dirctory in users home folder if it doesn't already exist
if not os.path.isdir(usr_bin):
    print('creating {0}'.format(usr_bin))
    os.mkdir(usr_bin)

# Copy mct setup file to users bin directory, create the bin directory if it doesn't exist
src = os.path.join(config_dir,'bash', setup_file)
dst = os.path.join(usr_bin, setup_file)

print('copying {0} to {1}'.format(src,dst))
shutil.copy(src,dst)


