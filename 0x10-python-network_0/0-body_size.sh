#!/bin/bash
curl -o /dev/null -s -w '%{size_download}\n' "$1"
