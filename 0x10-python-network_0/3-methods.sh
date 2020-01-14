#!/bin/bash
# get list of methods
curl -si --request OPTIONS "$1" | grep '^Allow:' | cut -f2- -d' '
