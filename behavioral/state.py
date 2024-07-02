# State Interface
class State:
    def do_action(self, context):
        pass

class StartState(State):
    def do_action(self, context):
        print("Player is in start state")
        context.set_state(self)
    def __str__(self):
        return "Start State"

class StopState(State):
    def do_action(self, context):
        print("Player is in stop state")
        context.set_state(self)
    def __str__(self):
        return "Stop State"

class Context:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

if __name__ == "__main__":
    context = Context()
    start_state = StartState()
    start_state.do_action(context)
    print(context.get_state())
    stop_state = StopState()
    stop_state.do_action(context)
    print(context.get_state())
