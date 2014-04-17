import os
import sys

if not os.path.exists('bla'):
    os.mkdir('bla')
os.chdir('bla')
if not os.path.exists('a'):
    os.mkdir('a')
os.chdir('..')
if not os.path.exists('b'):
    os.mkdir('b')

##os.echo('bla'>'b.txt')
##os.move('b.txt','bla')
##
def hello():
    print  'hello '

hello()



# recursively move a file or directory (src) to another location (dst).

# if the destination is a directory or a symlink to a directory, then src is moved
#inside that directory.

# the destination directory must not already exist.

# this would move files ending with .txt to the destination path

import shutil

sourcep = "bla/a/"
source = os.listdir(sourcep)
destination =  "bla/"
print source
for files in source:
    if files.endswith(".txt"):
        shutil.copy(sourcep+files,destination)

print "done"



sourcep = "bla/"
source = os.listdir(sourcep)
destination =  "c/"
if not os.path.exists(destination):
    os.mkdir(destination)
for files in source:
    if files.endswith(".txt"):
        shutil.move(sourcep+files,destination)

print "done"




