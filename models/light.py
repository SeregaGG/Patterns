from patterns import AbstractObserver


class Light(AbstractObserver):
    def do_something(self):
        print("Light on!")
