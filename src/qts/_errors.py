class QtsError(Exception):
    """Base exception class for all Qts exceptions.

    Do not raise directly.
    """


class InvalidWrapperError(QtsError):
    """Raised when an invalid wrapper is specified."""

    def __init__(self, wrapper):
        super().__init__(f"Unkown wrapper specified: {wrapper!r}")


class MultipleWrappersAvailable(QtsError):
    """Raised when searching for one wrapper but multiple are available."""

    def __init__(self, searched, found):
        searched_list = ", ".join(wrapper.module_name for wrapper in searched)
        found_list = ", ".join(wrapper.module_name for wrapper in found)
        super().__init__(f"Found {found_list} while searching through {searched_list}")


class NoWrapperAvailable(QtsError):
    """Raised when searching for wrappers and none are available."""

    def __init__(self, wrappers):
        wrapper_list = ", ".join(wrapper.module_name for wrapper in wrappers)
        super().__init__(
            f"No wrapper module available when searching for: {wrapper_list}"
        )


class NoWrapperSelectedError(QtsError):
    """Raised when a wrapper selection is required but has not been made."""

    def __init__(self):
        super().__init__("No wrapper selected, see qts.set_wrapper()")


class WrapperAlreadySelectedError(QtsError):
    """Raised when attempting to set a wrapper but one has already been selected."""

    def __init__(self, existing_wrapper, requested_wrapper):
        message = (
            f"Wrapper {existing_wrapper.name} already selected while requesting"
            f" {requested_wrapper.name}"
        )
        super().__init__(message)
