# cli-passthrough

Script for logging stdin/stdout of a separate process. Useful to
monitor an application that is automated via its CLI. Runs the
argument(s) given to this script as a separate process, while passing
stdin and stdout through and writing them to files.

A simple echo script (`echo.py`) is included to showcase the
`passthrough.py` script. Change the `cmd` global variable in
`passthrough.py` to run another command.

## Example
```
./passthrough.py foobar # run echo.py with argument foobar through passthrough.py

# in a second terminal:
tail -f tail -f echo.py\ foobar\ stdin.txt

# in a third terminal:
tail -f tail -f echo.py\ foobar\ stdout.txt
```
As you write text into the first terminal window you should see it logged to the stdin and stdout files.
