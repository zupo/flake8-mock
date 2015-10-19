Flake8 Mock plugin
==================

Remember that a mock’s job is to say, “You got it, boss” whenever anyone calls
it. It will do real work, like raising an exception, when one of its convenience
methods is called, like assert_called_once_with. But it won’t do real work when
you call a method that only resembles a convenience method, such as
assert_called_once (no _with!). Sometimes the developer may not notice that
is using an non-existent method because is not getting an output error telling
him so. And for some reason can also forget to try the test cases to fail
making sure that also fails!.

This plugin provides checking possible non-existent methods for ``flake8``,
the Python code checker.


Installation
------------

You can install or upgrade ``flake8-debugger`` with these commands::

  $ pip install flake8-debugger
  $ pip install --upgrade flake8-debugger


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

When both ``flake8 2.2`` and ``flake8-mock`` are installed, the plugin is
available in ``flake8``::

    $ flake8 --version
    2.0 (pep8: 1.5.7, flake8-mock: 0.1dev, pyflakes: 0.8.1)


Example output
--------------

Once you run flake8, you can have something like::

    $ flake8 test_file.py
    test_file.py:27:1: M001 assert_calls is a non-existen method.
    test_file.py:28:1: M001 called_once_with is a non-existen method.
    test_file.py:39:1: M001 not_called is a non-existen method.
    test_file.py:40:1: M001 assert_called is a non-existen method.


Changes
-------

0.1dev (unreleased)
````````````````
* First release

