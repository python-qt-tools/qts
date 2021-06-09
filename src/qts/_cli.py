import sys

import click

import qts


@click.group()
def main():
    pass


@main.group()
def mypy():
    pass


@mypy.command()
@click.option(
    "--wrapper",
    "wrapper_name",
    default=None,
    type=click.Choice(
        case_sensitive=False, choices=[wrapper.name for wrapper in qts.wrappers]
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
def args(wrapper_name, delimiter):
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
