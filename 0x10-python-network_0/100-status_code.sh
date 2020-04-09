#!/bin/bash
# STATUS CODE
curl -o /dev/null -s -w "%{http_code}\n" "$1"
