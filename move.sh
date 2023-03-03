#!/bin/bash
#if [ $1 -gt 0 ]; then
    mypath="./$1"
    mkdir -p "$mypath"
    mv $(ls | grep -P "\d+.jpg" | sort ) "$mypath"
    cd "$mypath"
    convert -compress JPEG $(ls | grep -P "\d+.jpg" | sort -n) "Bleach $1.pdf"
    mv "Bleach $1.pdf" ..
    echo Done!
#fi
