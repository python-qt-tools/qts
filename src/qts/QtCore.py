import qts


if qts.wrapper == qts.pyqt_5_wrapper:
    from PyQt5.QtCore import *

    Signal = pyqtSignal
    del pyqtSignal

    SignalInstance = pyqtBoundSignal
    del pyqtBoundSignal
elif qts.wrapper == qts.pyqt_6_wrapper:
    from PyQt6.QtCore import *
elif qts.wrapper == qts.pyside_5_wrapper:
    from PySide2.QtCore import *
elif qts.wrapper == qts.pyside_6_wrapper:
    from PySide6.QtCore import *
elif qts.wrapper is None:
    raise qts.NoWrapperSelectedError()
else:
    raise qts.InvalidWrapperError(wrapper=qts.wrapper)