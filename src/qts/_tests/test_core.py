import pytest

import qts


def test_set_wrapper_succeeds(pytester: pytest.Pytester, wrapper: qts.Wrapper) -> None:
    content = f"""
    import sys

    import qts


    def test():
        assert {wrapper.module_name!r} not in sys.modules
        wrapper = qts.wrapper_by_name(name={wrapper.module_name!r})
        qts.set_wrapper(wrapper)
        from qts import QtCore
        imported_top_level_module_name = QtCore.QObject.__module__.partition('.')[0]
        assert imported_top_level_module_name == {wrapper.module_name!r}
    """
    pytester.makepyfile(content)
    run_result = pytester.runpytest_subprocess()
    run_result.assert_outcomes(passed=1)
