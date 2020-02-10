#!/usr/bin/node
/* eslint-disable */

require('child_process').exec("cat "+process.argv[2]+" "+process.argv[3]+" > "+process.argv[4]);
