Flake8 Mock plugin
==================

Remember that a mock's job is to say, "You got it, boss" whenever anyone calls
it. It will do real work, like raising an exception, when one of its
convenience methods is called, like ``assert_called_once_with``. But it won't
do real work when you call a method that only *resembles* a convenience method,
such as ``assert_called_once`` (no ``_with``!). Sometimes developers may not
notice that they are using a non-existent mock method, because they are not
getting an output error telling them so. And for some reason they can also
forget to verify that the test cases fail before writing implementation code.

This plugin checks for possible non-existent mock methods when you run
``flake8``, the Python code checker.

Inspired by http://engineeringblog.yelp.com/2015/02/assert_called_once-threat-or-menace.html.


Installation
------------

You can install or upgrade ``flake8-mock`` with these commands::

  $ pip install flake8-mock
  $ pip install --upgrade flake8-mock


List of non-existent methods checked
------------------------------------

    * ``assert_calls``
    * ``not_called``
    * ``called_once``
    * ``called_once_with``


Plugin for Flake8
-----------------

When both ``flake8`` and ``flake8-mock`` are installed, the plugin is
available in ``flake8``::

    $ flake8 --version
    5.0.4 (flake8-mock: 0.4, ...)


Example output
--------------

Once you run flake8, you can have something like::

    $ flake8 test_file.py
    test_file.py:27:1: M001 assert_calls is a non-existent mock method.
    test_file.py:28:1: M001 called_once_with is a non-existent mock method.
    test_file.py:39:1: M001 not_called is a non-existent mock method.
    test_file.py:40:1: M001 assert_called is a non-existent mock method.

Credits
-------
    * `Alejandro Gabriel Pereira <https://github.com/aleGpereira>`_ is the main author.
    * `Nejc Zupan <https://github.com/zupo>`_ (`Niteo <https://niteo.co>`_) provided the idea
      and proof-reading.

Collaborators
-------------
    * `John Vandenberg <https://github.com/jayvdb>`_
    * `Tom Prince <https://github.com/tomprince>`_
    * `Gasper Vozel <https://github.com/karantan>`_
    * `Bjørnar Myrheim <https://github.com/myrheimb>`_


Changes
-------

0.4 (05-12-2023)
````````````````
* Fix compatibility with flake8 >= 5.0.0.

0.3 (09-10-2016)
````````````````
* Don't warn on `assert_not_called`, `assert_called` or `assert_called_once`.
* Use ASCII only in README.rst

0.2 (12-16-2015)
````````````````
* Add Python 3 compatibility.

0.1 (10-20-2015)
````````````````
* First release.

0.1dev0 (10-19-2015)
````````````````````
* First dev release.
