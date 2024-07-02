class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def save_state_to_memento(self):
        return Memento(self._state)

    def get_state_from_memento(self, memento):
        self._state = memento.get_state()

class CareTaker:
    def __init__(self):
        self._memento_list = []

    def add(self, state):
        self._memento_list.append(state)

    def get(self, index):
        return self._memento_list[index]

if __name__ == "__main__":
    originator = Originator()
    care_taker = CareTaker()
    originator.set_state("State #1")
    originator.set_state("State #2")
    care_taker.add(originator.save_state_to_memento())
    originator.set_state("State #3")
    care_taker.add(originator.save_state_to_memento())
    originator.set_state("State #4")
    print("Current State: " + originator.get_state())
    originator.get_state_from_memento(care_taker.get(0))
    print("First saved State: " + originator.get_state())
    originator.get_state_from_memento(care_taker.get(1))
    print("Second saved State: " + originator.get_state())
