#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2013 René Moser <mail@renemoser.net>
# http://github.com/git-ftp/git-ftp2
#
# Git-ftp is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Git-ftp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Git-ftp. If not, see <http://www.gnu.org/licenses/>.

"""
git and python powered ftp client.

It uses git to determine which local files have changed since the last 
deployment to the remote server and saves you time and bandwidth by uploading 
only those files.

It keeps track of the deployed state by uploading the SHA1 of the last deployed 
commit in a log file.

Usage:
    git-ftp init [URL] [options]
    git-ftp push [URL] [options]
    git-ftp show [URL] [options]
    git-ftp catchup [URL] [options]

Options:
    --version                           Show version.
    -h --help                           Show help.
"""

import os
import sys
import signal

from gitftp_init import *
from gitftp_push import *
from gitftp_show import *
from gitftp_catchup import *

from docopt import (docopt, Option, Argument, Command)

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():
    args = docopt(__doc__,
        version='git-ftp 2.0.0',
        options_first=True)
    if args['init']:
        gf = GitftpInit()
        gf.checkIsDirty()
        gf.setRemotes
        return
    elif args['push']:
        gf = GitftpPush()
        gf.checkIsDirty()
        gf.setRemotes()
        return
    elif args['show']:
        gf = GitftpShow()
        gf.setRemotes()
        return
    elif args['catchup']:
        gf = GitftpCatchup()
        gf.setRemotes()
        return
    else:
        exit("%r is not a git-ftp command. See 'git-ftp help'")

if __name__ == '__main__':
    main()
