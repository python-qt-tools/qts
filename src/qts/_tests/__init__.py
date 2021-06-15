import attr


@attr.frozen
class QtModule:
    name: str


qt_modules = [QtModule(name="QtCore")]


