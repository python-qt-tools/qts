# TODO: maybe manage to not bypass this strict check
#       https://github.com/python-qt-tools/qts/issues/8
# mypy: implicit_reexport

import qts


if qts.wrapper is None:
    raise qts.NoWrapperSelectedError()
elif qts.is_pyqt_5_wrapper:
    from PyQt5.QtCore import *
elif qts.is_pyqt_6_wrapper:
    from PyQt6.QtCore import *
elif qts.is_pyside_5_wrapper:
    from PySide2.QtCore import *
elif qts.is_pyside_6_wrapper:
    from PySide6.QtCore import *
else:
    raise qts.InvalidWrapperError(wrapper=qts.wrapper)


if qts.is_pyqt_5_wrapper or qts.is_pyqt_6_wrapper:
    Signal = pyqtSignal
    del pyqtSignal

    SignalInstance = pyqtBoundSignal
    del pyqtBoundSignal
