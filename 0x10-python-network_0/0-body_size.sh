#!/bin/bash
# display size of response
curl -o /dev/null -s -w '%{size_download}\n' "$1"
