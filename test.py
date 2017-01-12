import StateMachine

s = StateMachine.StateMachine('deterministic')

s.addState("1")
s.addState("0")

s.addTransition("1", "a", "0")
s.printTransitions()
s.addTransition("1", "b", "0")
s.addTransition("1", "b", "1")

s.printTransitions()