#!/bin/bash

FILES=$(find ./mlib -name '*.py')
# Based on: https://stackoverflow.com/a/16265283

# Syntax
#  NAME1:NAME2
#    NAME1 is the path on the file system
#    NAME2 is the path on which it will be stored IN the zip arcive
#
#  NAME1
#    NAME1 will be stored as given

python -c '
import zipfile as zf, sys
args=sys.argv
args.pop(0)
z=zf.ZipFile(args[0],"w")
args.pop(0)
for arg in args:
    paths=arg.split(":")
    src=""
    dest=""
    if len(paths)==2:
        src=paths[0]
        dest=paths[1]
    else:
        src=paths[0]
        dest=paths[0]
    z.write(src,dest)
z.close()
' mlib.zip $FILES DOC.txt:mlib/DOC.txt README.txt:mlib/README.txt LICENSE:mlib/LICENSE