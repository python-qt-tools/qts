import typing

import pytest

import qts
from qts import QtCore


def test_signal() -> None:
    assert isinstance(QtCore.QObject.destroyed, QtCore.Signal)


def test_bound_signal() -> None:
    qt_object = QtCore.QObject()
    assert isinstance(qt_object.destroyed, QtCore.SignalInstance)


@pytest.mark.parametrize(
    argnames=["second_wrapper"],
    argvalues=[
        [qts.wrapper],
        [qts.Wrapper(family="", name="fake", major_version=0, module_name="")],
        [None],
    ],
)
def test_setting_twice_raises(second_wrapper: typing.Optional[qts.Wrapper]) -> None:
    with pytest.raises(qts.WrapperAlreadySelectedError):
        qts.set_wrapper(second_wrapper)  # type: ignore[arg-type]


def test_setting_invalid_wrapper_raises(pytester: pytest.Pytester) -> None:
    content = f"""
    import pytest

    import qts


    def test():
        with pytest.raises(qts.InvalidWrapperError):
            qts.set_wrapper(None)
    """
    pytester.makepyfile(content)
    run_result = pytester.runpytest_subprocess()
    run_result.assert_outcomes(passed=1)


def test_importing_with_invalid_wrapper_raises(pytester: pytest.Pytester) -> None:
    content = f"""
    import pytest

    import qts


    def test():
        qts.wrapper = 37
        with pytest.raises(qts.InvalidWrapperError):
            from qts import QtCore
    """
    pytester.makepyfile(content)
    run_result = pytester.runpytest_subprocess()
    run_result.assert_outcomes(passed=1)


def test_checking_with_no_available_wrappers_raises() -> None:
    with pytest.raises(qts.NoWrapperAvailableError):
        qts.available_wrapper(wrappers=[])


def test_checking_with_multiple_available_wrappers_raises() -> None:
    with pytest.raises(qts.MultipleWrappersAvailableError):
        qts.available_wrapper(wrappers=list(qts.available_wrappers()) * 2)


def test_importing_without_setting_raises(pytester: pytest.Pytester) -> None:
    content = f"""
    import pytest

    import qts


    def test():
        with pytest.raises(qts.NoWrapperSelectedError):
            from qts import QtCore
    """
    pytester.makepyfile(content)
    run_result = pytester.runpytest_subprocess()
    run_result.assert_outcomes(passed=1)
