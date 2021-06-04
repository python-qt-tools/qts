import pytest

import qts


def test_version_is_a_string():
    assert isinstance(qts.__version__, str)


@pytest.mark.parametrize(
    argnames=["qt_name"],
    argvalues=[
        ["PyQt5"],
        ["PyQt6"],
        ["PySide2"],
        ["PySide6"],
    ],
)
def test_importing_does_not_import_qt(pytester: pytest.Pytester, qt_name: str):
    content = f"""
    import sys
    
    import qts


    def test():
        assert "{qt_name}" not in sys.modules
    """
    pytester.makepyfile(content)
    run_result = pytester.runpytest_subprocess()
    run_result.assert_outcomes(passed=1)
