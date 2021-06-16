.. _cli:

Command line interface
++++++++++++++++++++++

This tooling is a bit sparse right now.
Perhaps other useful helpers will be identified in the future.

mypy
====

args
----

..
   TODO: generate this?  verify it?


.. code-block:: console

    $ qts mypy args --help
    Usage: qts mypy args [OPTIONS]

      Generate arguments to be passed to mypy so it can understand which code
      should be active.  If applications or other libraries use the same
      conditions in their code then this will work for them as well.

    Options:
      --wrapper [PyQt5|PyQt6|PySide2|PySide6]
      --delimiter TEXT                Defaults to a space for TTYs and a newline
                                      otherwise.
      --help                          Show this message and exit.
