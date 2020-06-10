#!/usr/bin/env python3
# stdout/stdin passthrough and logging

import os
import sys
import subprocess

cmd = "./echo.py"
r_in, w_in = os.pipe()
r_out, w_out = os.pipe()
processid = os.fork()
if processid: # process responsible for logging
    processid = os.fork()
    if processid: # process responsible for stdin
        w_in = os.fdopen(w_in, "w")
        stdin_file = open("stdin.txt", "w")
        for line in sys.stdin:
            line = line.strip()
            print(line, file=stdin_file) # write to file
            print(line, file=w_in) # write to subprocess
            w_in.flush()
            stdin_file.flush()
        os.close(r_in)
        os.close(w_in)
        os.close(r_out)
        os.close(w_out)
        stdin_file.close()
        sys.exit(0)
    else:
        r_out = os.fdopen(r_out)
        stdout_file = open("stdout.txt", "w")
        for line in r_out:
            line = line.strip()
            print(line, file=sys.stdout) # write to stdout
            print(line, file=stdout_file) # write to file
            sys.stdout.flush()
            stdout_file.flush()
        os.close(r_in)
        os.close(w_in)
        os.close(r_out)
        os.close(w_out)
        stdout_file.close()
        sys.exit()
else: # process responsible for running cmd
    subprocess.run([cmd] + sys.argv[1:], stdin=os.fdopen(r_in), stdout=os.fdopen(w_out, "w"))
    os.close(r_in)
    os.close(w_in)
    os.close(r_out)
    os.close(w_out)
    sys.exit()
