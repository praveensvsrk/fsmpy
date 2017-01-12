from fsmpy import fsmpy
from fsmpy import State

s = fsmpy.DFA()

a = State.State("0")
b = State.State("1")

s.addState(a)
s.addState(b)

s.addTransition(a, "a", b)
s.addTransition(b, "b", a)

s.printTransitions()