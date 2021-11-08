#!/usr/bin/env python3
import argparse
from io import TextIOWrapper
from os import environ
from sys import stderr, stdin
from time import time
from requests import post


EPILOG = """
  Authentication must be provided with the -u and -t arguments or by setting
  GITHUB_GIST_USER and GITHUB_GIST_TOKEN as environment variables.
"""

parser = argparse.ArgumentParser(description="Post a gist to Github from a file or stdin.", epilog=EPILOG)
parser.add_argument("file", nargs="?", type=argparse.FileType("r"), default=stdin, help="File to upload")
parser.add_argument("-u", "--user", type=str, default="", help="Github username")
parser.add_argument("-t", "--token", type=str, default="", help="Your Github personal access token")
parser.add_argument("-n", "--name", type=str, default=None, help="Filename to use in Github for your gist")
parser.add_argument("-d", "--description", type=str, default="", help="A description for your gist")
parser.add_argument("-p", "--public", type=bool, default=False, help="Make gist public")
args = parser.parse_args()

GITHUB_TOKEN = args.token or environ.get("GITHUB_GIST_TOKEN")
GITHUB_USER = args.user or environ.get("GITHUB_GIST_USER")


if not (GITHUB_TOKEN and GITHUB_USER):
  parser.print_help(stderr)

filename = args.name or str(time()).replace(".", "")

if isinstance(args.file, TextIOWrapper):
  data = args.file.read()
  if args.file.name != "<stdin>":
    filename = args.file.name
else:
  data = args.file

res = post(
  "https://api.github.com/gists",
  auth=(GITHUB_USER, GITHUB_TOKEN),
  json={
    "description": args.description,
    "public": args.public,
    "files": {
      f"{filename}": {
        "content": data
      }
    }
  }
)

if res.status_code not in (200, 201):
  print(res.content)
else:
  link = res.json()["files"][filename]["raw_url"]
  print(link)
