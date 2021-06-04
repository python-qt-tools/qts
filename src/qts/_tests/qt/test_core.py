from qts import QtCore


def test_signal():
    assert isinstance(QtCore.QObject.destroyed, QtCore.Signal)


def test_bound_signal():
    qt_object = QtCore.QObject()
    assert isinstance(qt_object.destroyed, QtCore.SignalInstance)
