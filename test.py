from fsmpy import pysm

s = pysm.StateMachine('deterministic')

s.addState("1")
s.addState("0")

s.addTransition("1", "a", "0")
s.printTransitions()
s.addTransition("1", "b", "0")
s.addTransition("1", "b", "1")

s.printTransitions()