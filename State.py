__author__ = "Praveen SVSRK"


class State:

    def __init__(self):
        self._name = None

    def __init__(self, name):
        self._name = name


    def register_handlers(self, entry=None, exit=None):

        if exit is not None and not callable(exit):
            raise ValueError("exit must be either None or callable object")
        self._handlers = {'entry': entry, 'exit': exit}

    def on_entry(self, entry=None, *args, **kwargs):
        if entry is not None and not callable(entry):
            raise ValueError("entry must be either None or callable object")
        self._handlers['entry'] = entry
        self._handlers['entry_args'] = args
        self._handlers['entry_kwargs'] = kwargs

    def on_exit(self, exit=None, *args, **kwargs):
        if exit is not None and not callable(exit):
            raise ValueError("entry must be either None or callable object")
        self._handlers['exit'] = exit
        self._handlers['exit_args'] = args
        self._handlers['exit_kwargs'] = kwargs

    def add_transition(self, input, name):
        self._destination = name

