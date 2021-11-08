# Simple tool for creating gists.

Copy file to path and use. Requires python3. To use a different version change shebang or create an alias that calls the script with the version you want.

```
usage: gist [-h] [-u USER] [-t TOKEN] [-n NAME] [-d DESCRIPTION] [-p PUBLIC] [file]

Post a gist to Github from a file or stdin.

positional arguments:
  file                  File to upload

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  Github username
  -t TOKEN, --token TOKEN
                        Your Github personal access token
  -n NAME, --name NAME  Filename to use in Github for your gist
  -d DESCRIPTION, --description DESCRIPTION
                        A description for your gist
  -p PUBLIC, --public PUBLIC
                        Make gist public

Authentication must be provided with the -u and -t arguments or by setting GITHUB_GIST_USER and GITHUB_GIST_TOKEN as environment variables.
```
