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

# Add mct_setup.bash to .bashrc file - create back up as .bashrc.bak
bashrc_file = os.path.join(os.environ['HOME'],'.bashrc')
bashrc_file_bak = os.path.join(os.environ['HOME'],'.bashrc.bak')

shutil.copy(bashrc_file, bashrc_file_bak)

bashrc_lines = []
with open(bashrc_file,'r') as f:
    bashrc_lines = [line for line in f.readlines()]

bashrc_lines_new = []
for line in bashrc_lines:
    if 'mct_setup.bash' in line:
        continue
    else:
        bashrc_lines_new.append(line)
source_line = 'source ~/bin/{0}'.format(setup_file)
print('adding {0} to .bashrc'.format(source_line))
bashrc_lines_new.append(source_line + '\n')
with open(bashrc_file,'w') as f:
    for line in bashrc_lines_new:
        f.write(line)








