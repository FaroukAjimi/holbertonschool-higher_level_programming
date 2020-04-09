#!/bin/bash
# ALLOWED
s=$(curl $1 -si | grep  Allow | head -n 1) ; cut -d ' ' -f2- <<< $s
