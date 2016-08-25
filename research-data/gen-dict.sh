#!/bin/bash

# gen dict for research to fill in

cat member-profile-2012-2016.csv| tr ',' '\n' | sort -u  > dict.csv
