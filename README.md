WARNING: WORK IN PROGRESS
=========================


README of git-ftp2
==================

* This application is licenced under [GNU General Public License, Version 3.0]


Summary
-------

Git powered FTP client rewritten in python.


About
-----

I use git-ftp for my script based projects, mostly PHP. Most of the low-cost
web hosting companies do not provide SSH or git support, but only FTP.

That is why I needed an easy way to deploy my git tracked projects. Instead of
transfering the whole project, I thought, why not only transfer the files
that changed since the last time, git can tell me those files.

Even if you are playing with different branches, git-ftp knows which files
are different. No ordinary FTP client can do that.


Known Issues
------------

* See [git-ftp issues on GitHub] for open issues


Installing
----------

TBD

Usage
-----

	$ cd my_git_tracked_project
	$ git ftp push --user <user> --passwd <password> ftp://host.example.com/public_html

For interactive password prompt use:

	$ git ftp push -u <user> -p - ftp://host.example.com/public_html

Pushing for the first time:

	$ git ftp init -u <user> -p - ftp://host.example.com/public_html

See [man page](man/git-ftp.1.md) for more options, features and examples!


Contributions
-------------

By contributing you agree that these contributions are your own (or approved by your employer) and you grant a full, complete, irrevocable copyright license to all users and developers of the project, present and future, pursuant to the license of the project.

[git-ftp issues on GitHub]: http://github.com/git-ftp/git-ftp2/issues
[GNU General Public License, Version 3.0]: http://www.gnu.org/licenses/gpl-3.0-standalone.html
