from .baseengine import BaseEngine

# TODO: document

class DummyEngine(BaseEngine):
    def exitAction(self):
        print('''Do exit action at the end.''')

    def timedAction(self):
        print('''Do timed action every X time.''')
