"""
Finite-state machine
My day
"""
from random import random

class Person:
    """
    Base class for states
    """
    def __init__(self):
        self.state = None

    def set_state(self, state):
        """
        Set state
        """
        self.state = state

    def run(self):
        """
        Run day
        """
        print(person.state)
        while True:
            state_choice = self.state.random_next_state()
            if state_choice.done is False:
                if state_choice == have_a_shower:
                    state_choice.done = True
                self.set_state(state_choice)
            else:
                continue
            print(self.state)
            if self.state == sleep:
                break

class Business:
    """
    Some business of person
    """
    def __init__(self, name = None, output = None, next_states = None, prob = None) -> None:
        self.name = name
        self.output = output
        self.next_states = next_states
        self.prob = prob
        self.done = False

    def set_next_states(self, next_states):
        """
        Set next states
        """
        self.next_states = next_states

    def random_next_state(self):
        """
        Random next state by probability
        """
        if self.next_states is None:
            return None
        if self.prob is None:
            return None
        rand = random()
        probabilities = [elm for elm in self.prob]
        probabilities.append(rand)
        probabilities = sorted(probabilities, reverse=True)
        if probabilities.index(rand) != 0:
            return self.next_states[probabilities.index(rand) - 1]
        return self.next_states[0]

    def __str__(self) -> str:
        return self.output

if __name__ == "__main__":
    sleep = Business("sleep", "I am sleeping")
    wake_up = Business("wake_up", "New day!")
    breakfast = Business("breakfast", "I am eating breakfast in the Trapezna")
    brush_teeth = Business("brush_teeth", "I am brushing my teeth")
    go_to_first_pair = Business("go_to_first_pair", "I am going to the first pair")
    go_to_second_pair = Business("go_to_second_pair", "I am going to the second pair")
    lunch = Business("lunch", "I am eating lunch in the Trapezna")
    go_for_walk_with_Stepan = Business("go_for_walk_with_Stepan", "I am going for a walk with Stepan Fedyniak and friends")
    essey = Business("essey", "I am writing an essey")
    eat_ice_cream = Business("eat_ice_cream", "I am eating ice cream")
    do_lab_work = Business("do_lab_work", "I am doing lab work")
    talk_with_friends = Business("talk_with_friends", "I am talking with friends")
    prepare_to_test = Business("prepare_to_test", "I am preparing to test")
    clash_royale_one_on_one = Business("clash_royale_one_on_one", "I am playing clash royale one on one with friend")
    lie_down = Business("lie_down", "I am lying down")
    have_a_shower = Business("have_a_shower", "Water, hehe, bul bul bul")
    wake_up.next_states = [breakfast, brush_teeth, go_to_first_pair]
    wake_up.prob = [0.5, 0.3, 0.2]
    breakfast.next_states = [brush_teeth, go_to_first_pair, go_to_second_pair]
    breakfast.prob = [0.6, 0.3, 0.1]
    brush_teeth.next_states = [go_to_first_pair, go_to_second_pair]
    brush_teeth.prob = [0.8, 0.2]
    go_to_first_pair.next_states = [go_to_second_pair]
    go_to_first_pair.prob = [1.0]
    go_to_second_pair.next_states = [lunch, go_for_walk_with_Stepan]
    go_to_second_pair.prob = [0.8, 0.2]
    lunch.next_states = [essey, go_for_walk_with_Stepan, do_lab_work]
    lunch.prob = [0.4, 0.3, 0.3]
    eat_ice_cream.next_states = [essey, do_lab_work]
    eat_ice_cream.prob = [0.7, 0.3]
    essey.next_states = [do_lab_work]
    essey.prob = [1.0]
    do_lab_work.next_states = [prepare_to_test, talk_with_friends]
    do_lab_work.prob = [0.6, 0.4]
    talk_with_friends.next_states = [prepare_to_test, clash_royale_one_on_one]
    talk_with_friends.prob = [0.7, 0.3]
    prepare_to_test.next_states = [clash_royale_one_on_one, have_a_shower, lie_down, talk_with_friends]
    prepare_to_test.prob = [0.4, 0.3, 0.2, 0.1]
    clash_royale_one_on_one.next_states = [prepare_to_test, lie_down, sleep]
    clash_royale_one_on_one.prob = [0.5, 0.3, 0.2]
    lie_down.next_states = [prepare_to_test, clash_royale_one_on_one, sleep, have_a_shower]
    lie_down.prob = [0.35, 0.3, 0.2, 0.15]
    have_a_shower.next_states = [sleep, clash_royale_one_on_one]
    have_a_shower.prob = [0.6, 0.4]
    sleep.next_states = [wake_up]
    sleep.prob = [1.0]
    go_for_walk_with_Stepan.next_states = [eat_ice_cream, essey, do_lab_work]
    go_for_walk_with_Stepan.prob = [0.5, 0.3, 0.2]

    person = Person()
    person.set_state(sleep)
    person.run()
