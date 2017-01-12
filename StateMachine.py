__author__ = "Praveen SVSRK"


class StateMachine:

    def __init__(self, type = "deterministic"):
        self.transitions = {}
        self.type = type
        if type is not "deterministic" and type is not "non-deterministic":
            raise ValueError("Type must be 'deterministic' or 'non-deterministic'")
        print "State Machine Created"

    def addState(self, name):
        if not isinstance(name, str):
            raise TypeError("State must be a string")
        self.transitions[name] = list()

    def addTransition(self, old, input, new):
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
                    if self.type is "deterministic":
                        raise ValueError("Multiple transitions on same input is not possible"
                                     "(Use non-deterministic FSM instead)")
            else:
                self.transitions[old].append(tuple((input, new)))

    def delTransition(self):
        pass

    def printTransitions(self):
        for state in self.transitions:
            print state, ":", self.transitions[state]

    def exists(self, state):
        if state in self.transitions:
            return True
        else:
            return False
