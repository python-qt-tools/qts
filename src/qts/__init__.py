import typing

from qts._core import (
    available_wrapper,
    available_wrappers,
    pyqt_5_wrapper,
    pyqt_6_wrapper,
    pyside_5_wrapper,
    pyside_6_wrapper,
    set_wrapper,
    Wrapper,
    wrapper_by_name,
    wrappers,
)
from qts._errors import (
    InvalidWrapperError,
    MultipleWrappersAvailableError,
    NoWrapperAvailableError,
    NoWrapperSelectedError,
    QtsError,
    WrapperAlreadySelectedError,
)
from qts._version import get_versions

__version__ = get_versions()["version"]
del get_versions


wrapper: typing.Optional[Wrapper] = None
