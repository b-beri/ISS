#!/bin/bash

find . -name \*.txt -type f -exec cat {} + | grep -o '\<Linux\>' | wc -l
# grep -o -i Linux | wc -l
