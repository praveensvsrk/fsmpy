__author__ = "Praveen SVSRK"


class State:

    def __init__(self):
        self._name = None
        self._handlers = {}

    def __init__(self, name):
        self._name = name
        self._handlers = {}

    def on_entry_event(self, entry=None, *args, **kwargs):
        if entry is not None and not callable(entry):
            raise ValueError("entry must be either None or callable object")
        self._handlers['entry'] = entry
        self._handlers['entry_args'] = args
        self._handlers['entry_kwargs'] = kwargs

    def on_exit_event(self, exit=None, *args, **kwargs):
        if exit is not None and not callable(exit):
            raise ValueError("entry must be either None or callable object")
        self._handlers['exit'] = exit
        self._handlers['exit_args'] = args
        self._handlers['exit_kwargs'] = kwargs

    def entry(self):
        self._handlers['entry'](self._handlers['entry_args'], self._handlers['entry_kwargs'])

    def exit(self):
        self._handlers['exit'](self._handlers['exit_args'], self._handlers['exit_kwargs'])

    def __repr__(self):
        return self._name


