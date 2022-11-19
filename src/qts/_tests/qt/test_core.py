from qts import QtCore


def test_signal() -> None:
    # TODO: Working around hinting failure where PySide6 doesn't provide a .destroyed
    #       attribute.
    destroyed = getattr(QtCore.QObject, "destroyed")
    assert isinstance(destroyed, QtCore.Signal)


def test_bound_signal() -> None:
    qt_object = QtCore.QObject()
    # TODO: Working around hinting failure where PySide6 doesn't provide a .destroyed
    #       attribute.
    destroyed = getattr(qt_object, "destroyed")
    assert isinstance(destroyed, QtCore.SignalInstance)
