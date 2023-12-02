from patterns import AbstractObserver


class Camera(AbstractObserver):
    def do_something(self):
        print("Make photo")
