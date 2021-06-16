import sys

import click

import qts


@click.group()
def main() -> None:
    pass


@main.group()
def mypy() -> None:
    pass


@mypy.command()
@click.option(
    "--wrapper",
    "wrapper_name",
    default=None,
    type=click.Choice(
        case_sensitive=False,
        choices=[wrapper.name for wrapper in qts.supported_wrappers],
    ),
)
@click.option(
    "--delimiter",
    # While bash command substitution works with either a space or a newline, fish
    # only accepts newlines for separating substituted arguments.
    default=" " if sys.stdout.isatty() else "\n",
    help="Defaults to a space for TTYs and a newline otherwise.",
    type=str,
)
def args(wrapper_name: str, delimiter: str) -> None:
    """Generate arguments to be passed to mypy so it can understand which code should
    be active.  If applications or other libraries use the same conditions in their
    code then this will work for them as well.
    """
    # TODO: make this selectable
    if wrapper_name is None:
        wrapper = qts.available_wrapper()
    else:
        wrapper = qts.wrapper_by_name(wrapper_name)

    qts.set_wrapper(wrapper)

    arguments = [
        f"--always-{'true' if qts.is_pyqt_5_wrapper else 'false'}=is_pyqt_5_wrapper",
        f"--always-{'true' if qts.is_pyqt_6_wrapper else 'false'}=is_pyqt_6_wrapper",
        f"--always-{'true' if qts.is_pyside_5_wrapper else 'false'}=is_pyside_5_wrapper",
        f"--always-{'true' if qts.is_pyside_6_wrapper else 'false'}=is_pyside_6_wrapper",
    ]

    click.echo(delimiter.join(arguments))
