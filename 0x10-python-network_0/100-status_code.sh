#!/bin/bash
# STATUS CODE
curl -s -o /dev/null -w "%{http_code}\n" "$1"
