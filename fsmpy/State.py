__author__ = "Praveen SVSRK"


class State:

    def __init__(self):
        self._name = None
        self._handlers = {}

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("State name must be a string")
        self._name = name
        self._handlers = {}

    def register_handlers(self, entry=None, exit=None):
        if entry is not None and not callable(entry):
            raise ValueError("entry must be either None or callable object")
        self._handlers['entry'] = entry
        self._handlers['exit'] = exit

    def on_enter(self):
        self._handlers['entry']()

    def on_exit(self):
        self._handlers['exit']()

    def __repr__(self):
        return self._name


