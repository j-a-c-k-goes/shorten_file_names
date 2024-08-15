# rename_files

## Context

### What Script Does?
This script has one objective. Shorten programming language (and some data) files that exceed eight characters in length. Shorter files used to be mandatory in certain operating system contexts. Also, a shorter file name is less typing (and noise).

*⚠️ Walking from '/' will likely make the shortening session a long one. Targeting a specific directory will cut down session time.*

### Rules
* Only valid program files can suggested for renaming.
* For a file to be suggested for renaming:
    - It must be over 8 characters in length.
    - It must be posses a programming language extension.
        + There is a list built into the `ftype.py` module. It is not conclusive but does cover a wide spectrum of programming file extensions. If you need more type, make a pull request with appendages to the module.
* Renaming a file with a divergent extension is not allowed.

### Use Case(s)
* You desire shorter file names.
* You want to think of more compact naming conventions.

## Installation
* Clone the repository
    - `git clone <link-to-this-repo>`
* Change into the repo
    - `cd <path-to-cloned-repo>`

## Running the script
* One-time use
    - `python main.py <dry-run-on|dry-run-off> <path> <file-extension>`
* Cleaning up logs periodically. 
    - Remove logs older than 30days every 15th day @ 10:30am
        + `crontab -e`
        + (from inside crontab) `30 10 15 * * find /tmp/*-log-*-shortened*.log -mtime +30 -exec rm {} \;`

*🔑 Running with dry-run-on mode is encouraged. This allows you to view what would be renamed without actually having the process take place. Try before you buy. Also: dry-run does not generate a log file.*

## Examples
* Search a directory for python files (w/ dry-run-on)
    - `python main.py dry-run-on <this-repo>/test-output .py`

## Using the `test-output`
`test-ouput` is included as a sandbox to run the script against low-stakes files. You should use the sandbox the first few times you use the script with `dry-mode-off`
* Search `test-output` for c++ files
    - `python main.py dry-run-off <this-repo>/test-output .cpp`

## Checking the Logs
* `main.py` creates a log file to display a few stats on what happened during the script run. 
* The file lives at: 
    - `/tmp/<timestamp>-log-files-shortened.log`

To display logged files, run `cat /tmp/*-log-shortened*.log`
