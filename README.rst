Flake8 Mock plugin
==================

Remember that a mock’s job is to say, “You got it, boss” whenever anyone calls
it. It will do real work, like raising an exception, when one of its
convenience methods is called, like ``assert_called_once_with``. But it won’t
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
    * ``assert_not_called``
    * ``assert_called``
    * ``assert_called_once``
    * ``not_called``
    * ``called_once``
    * ``called_once_with``


Plugin for Flake8
-----------------

When both ``flake8 2.4`` and ``flake8-mock`` are installed, the plugin is
available in ``flake8``::

    $ flake8 --version
    2.4.1 (pep8: 1.5.7, flake8-mock: 0.1, pyflakes: 0.8.1)


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
    * Alejandro Gabriel Pereira (`NiteoWeb Ltd. <http://www.niteoweb.com>`_) is the main author.
    * Nejc Zupan (`NiteoWeb Ltd. <http://www.niteoweb.com>`_) provided the idea
      and proof-reading.


Changes
-------

0.1dev0 (10-19-2015)
````````````````
* First release.

