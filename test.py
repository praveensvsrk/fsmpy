from fsmpy import fsmpy
from fsmpy import State

def entry(state):
    print "Entered state {0}".format(state)

def exit(state):
    print "Exited state {0}".format(state)

dfa = fsmpy.DFA()

s1 = State.State("0")
s1.on_entry_event(entry, s1)
s1.on_exit_event(exit, s1)

s2 = State.State("1")
s2.on_entry_event(entry, s2)
s2.on_exit_event(exit, s2)



dfa.add_state(s1)
dfa.add_state(s2)

dfa.add_transition(s1, "a", s2)
dfa.add_transition(s2, "b", s1)

dfa.print_transitions()


s1.entry()
s1.exit()

