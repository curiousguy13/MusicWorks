import os
my = []
for root, dirs, files in os.walk("Zedd/"):
    for file in files:
       if file.endswith(".mp3"):
           my.append(file)
##       print "root"
##       print root
##       print "dirs"
##       print dirs
##       print "files"
##       print file
##       print "here"
        
           
for file in my:
    print file

print "\ndone\n"

for root in os.walk("Zedd/"):
    #print root
    print "\nbla\n"
    for something in root:
        print something
      
##       print "root"
##       print root
##       print "dirs"
##       print dirs
##       print "files"
##       print file
##       print "here"





