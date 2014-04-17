##from __future__ import with_statement
##
##
###file = open('Test.mp3','r').read()
##
##
##
##
##find_str = "Title"                     # String to find
##fname = "Test.mp3"     # File to check
##
##with open(fname, "r") as f:
##    f.seek (0, 2)           # Seek @ EOF
##    fsize = f.tell()        # Get Size
##    f.seek (max (fsize-1024, 0), 0) # Set pos @ last n chars
##    lines = f.readlines()       # Read to end
##
##lines = lines[-10:]    # Get last 10 lines
##
### This returns True if any line is exactly find_str + "\n"
##
### If you're searching for a substring
##for line in lines:
##    if find_str in line:
##        print line
##        print len(line)
##        break
##
##
##    
##

file = open('Test2.mp3','r')
file.seek(-128, 2)
tag = file.read(128)
if len(tag) != 128:
        print "128"
if tag[0:3] != 'TAG':
        print "No Tag"

Title = tag[3:33].strip()
Artist = tag[33:63].strip()
Album = tag[63:93].strip()
Year = tag[93:97].strip()
Comment = tag[97:-3].strip()

print tag
print Title
print Artist
print Album
print Year
print Comment





















