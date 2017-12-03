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

import ftplib
import os, sys
import getpass

from git import *
from StringIO import StringIO


class GitftpCommon(object):

    def __init__(self):
        try:
            self._repo = Repo('.')
        except InvalidGitRepositoryError:
            sys.stderr.write("Fatal: Not a git repository?\n")
            sys.exit(1)
        self._git = self._repo.git
        self._cloned_git = self._cloned_repo.git

    def cloneRepoToTmp(self):
        import tempfile 
        self._tmpdir = tempfile.mkdtemp()
        self._cloned_repo = self._repo.clone(tmpdir)


    def __getRemoteUser(self):
        user = self._getConfig('user')
        if user == '':
            user = getpass.getuser()
        return user


    def setRemotes(self):
        self._remote_user = self.__getRemoteUser();
        self._remote_passwd = self._getConfig('passwd')


    def checkIsDirty(self):
        if self._repo.is_dirty():
            if not self._args['--quiet']:
                print('Warning: Uncommited changes will be ignored.')


    def checkDeployedCommit(self):
        pass


    def setLocalCommit(self):
        self._local_commit =  self._cloned_git.log(n=1, pretty="format:%H")

    def _getConfig(self, value):
        rtrn = ''
        if os.path.exists('.git-ftp-config'):
            try:
                rtrn = self._git.config('git-ftp.'+value, get=True, f='.git-ftp-config')
            except:
                pass
        return rtrn

