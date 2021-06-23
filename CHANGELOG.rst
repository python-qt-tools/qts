qts 0.2
=======

Features
--------

- :func:`qts.autoset_wrapper` automatically selects an available wrapper and sets it.
  (`#21 <https://github.com/python-qt-tools/qts/pull/21>`__)
- :func:`qts.an_available_wrapper` returns a single wrapper that is available as long as there is at least one to choose.
  (`#21 <https://github.com/python-qt-tools/qts/pull/21>`__)
- Importing the Qt modules will set the wrapper via :func:`qts.autoset_wrapper` if one has not already been set.
  There is hope to provide a more explicit, yet still easily usable, API but this automation will be available for now.
  It may be removed or discouaraged at a later time.
  (`#21 <https://github.com/python-qt-tools/qts/pull/21>`__)


qts 0.1
=======

- Initial release