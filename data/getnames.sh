#!/bin/bash
trashit compnames.txt
for x in $(ls| grep .html); do
    y=${x%.html}
    echo ${x%[0-9].html} "${y: -1}" >> compnames.txt
done
