# Could not find platform independent libraries <prefix> in Python
## Q1:
## A1:
Try export PYTHONHOME=/usr/local. Python should be installed in /usr/local on OS X.

This answer has received a little more attention than I anticipated, I'll add a little bit more context.

Normally, Python looks for its libraries in the paths prefix/lib and exec_prefix/lib, where prefix and exec_prefix are configuration options. If the PYTHONHOME environment variable is set, then the value of prefix and exec_prefix are inherited from it. If the PYTHONHOME environment variable is not set, then prefix and exec_prefix default to /usr/local (and I believe there are other ways to set prefix/exec_prefix as well, but I'm not totally familiar with them).

Normally, when you receive the error message Could not find platform independent libraries <prefix>, the string <prefix> would be replaced with the actual value of prefix. However, if prefix has an empty value, then you get the rather cryptic messages posted in the question. One way to get an empty prefix would be to set PYTHONHOME to an empty string. More info about PYTHONHOME, prefix, and exec_prefix is available in the official docs.

## Ref
[Could not find platform independent libraries <prefix>](https://stackoverflow.com/questions/19292957/how-can-i-troubleshoot-python-could-not-find-platform-independent-libraries-pr)
