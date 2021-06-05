import importlib.util

import attr

import qts


@attr.frozen
class Wrapper:
    family: str
    name: str
    major_version: int
    module_name: str


wrappers = [pyqt_5_wrapper, pyqt_6_wrapper, pyside_5_wrapper, pyside_6_wrapper] = [
    Wrapper(family="PyQt", name="PyQt5", major_version=5, module_name="PyQt5"),
    Wrapper(family="PyQt", name="PyQt6", major_version=6, module_name="PyQt6"),
    Wrapper(family="PySide", name="PySide2", major_version=5, module_name="PySide2"),
    Wrapper(family="PySide", name="PySide6", major_version=6, module_name="PySide6"),
]

wrappers_by_name = {wrapper.name: wrapper for wrapper in wrappers}


def set_wrapper(wrapper: Wrapper):
    # This could accept the new wrapper if it matches the existing selection, but this
    # seems like it would mostly just encourage coding that hazards setting to a
    # different wrapper in some other case.  May as well complain early so that
    # developers get early warning and can adjust their design.

    if qts.wrapper is not None:
        raise qts.WrapperAlreadySelectedError()

    if wrapper not in wrappers:
        raise qts.InvalidWrapperError(wrapper=wrapper)

    qts.wrapper = wrapper


def available_wrappers(wrappers=wrappers):
    available = [
        wrapper for wrapper in wrappers if importlib.util.find_spec(wrapper.module_name)
    ]
    return available


def available_wrapper():
    all_available = available_wrappers(wrappers=wrappers)

    if len(all_available) == 0:
        raise qts.NoWrapperAvailable(wrappers=wrappers)
    elif len(all_available) > 1:
        raise qts.MultipleWrappersAvailable

    [the_one] = all_available
    return the_one


def wrapper_by_name(name: str):
    return wrappers_by_name[name]
