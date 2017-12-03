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
Usage:
    git push [URL] [options]

Options:
    -u <user>, --user <user>            Use FTP user instead of $USER.
    -p <password>, --passwd <password>  Use FTP password.
    -P, --ask-passwd                    Ask for FTP password interactivly.
    -a, --all                           Upload all files and ignore already 
                                        deployed state.
    -s <scope>, --scope <scope>         Use a scope (e.g. dev, prod, testing).
    -c, --commit                        Set SHA1 hash of last deployed commit.
    -n, --dry-run                       Don't do anything.
    -q, --quiet                         Be silent.
    -v, --verbose                       Be verbosy.
    --active-ftp                        Use FTP active mode.
    --syncroot <syncroot>               Use a subdirectory to sync from as if it
                                        were the git project root path.
    --insecure                          Don't verify server's certificate.
    --cacert <file>                     Specify a <file> as CA certificate 
                                        store. Useful using self-signed cert.
"""

from gitftp_common import *
from docopt import docopt

class GitftpPush(GitftpCommon):

    def __init__(self):
        self._args = docopt(__doc__)
        GitftpCommon.__init__(self)
