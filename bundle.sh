#!/bin/bash

FILES=$(find ./mlib -name '*.py')

zip mlib $FILES ./DOC.txt ./README.txt ./LICENSE