from State import State

__author__ = "Praveen SVSRK"


class DFA:

    def __init__(self, *states):
        self._initial = None
        self._transitions = {}
        for state in states:
            self.addState(state)
        print "DFA Created"

    def add_state(self, state, initial=False):
        if not isinstance(state, State):
            raise TypeError("State must be of type 'State'")
        if state in self._transitions:
            raise ValueError("State {0} already exists".format(state))
        self._transitions[state] = list()
        if initial:
            if self._initial is None:
                self._initial = state
            else:
                raise ValueError("Initial state already exists")

    def add_transition(self, old, input, new):
        if not isinstance(old, State) or not isinstance(new, State):
            raise TypeError("State must be of type 'State'")
        if not isinstance(input, str):
            raise TypeError("Input must be a string")
        if self.exists(old) is False:
            raise ValueError("Source State doesn't exist")
        if self.exists(new) is False:
            raise ValueError("Destination State doesn't exist")

        if not self._transitions[old]:
            self._transitions[old].append((input, new))
        else:
            for key, value in self._transitions[old]:
                if input is key:
                    if value is new:
                        raise ValueError("Transition already exists")
                    else:
                        raise ValueError("Multiple transitions on same input is not possible"
                                     "(Use NFA instead)")
            else:
                self._transitions[old].append(tuple((input, new)))

    def del_transition(self):
        pass

    def print_transitions(self):
        for state in self._transitions:
            print state, ":", self._transitions[state]

    def exists(self, state):
        if state in self._transitions:
            return True
        else:
            return False


class NFA:

    def __init__(self):
        self.transitions = {}
        print "NFA Created"

    def add_state(self, name):
        if not isinstance(name, str):
            raise TypeError("State must be a string")
        self.transitions[name] = list()

    def add_transition(self, old, input, new):
        if not isinstance(old, str) or not isinstance(new, str):
            raise TypeError("State must be a string")
        if not isinstance(input, str):
            raise TypeError("Input must be a string")
        if self.exists(old) is False:
            raise ValueError("Source State doesn't exist")
        if self.exists(new) is False:
            raise ValueError("Destination State doesn't exist")

        if not self.transitions[old]:
            self.transitions[old].append((input, new))
        else:
            for key, value in self.transitions[old]:
                if input is key:
                    if value is new:
                        raise ValueError("Transition already exists")
            else:
                self.transitions[old].append(tuple((input, new)))

    def del_transition(self):
        pass

    def print_transitions(self):
        for state in self.transitions:
            print state, ":", self.transitions[state]

    def exists(self, state):
        if state in self.transitions:
            return True
        else:
            return False