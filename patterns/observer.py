from abc import ABC, abstractmethod


class AbstractObserver(ABC):
    @abstractmethod
    def do_something(self):
        pass


class ControlSystem:
    def __init__(self):
        self.__observers: set[AbstractObserver] = set()

    def attach(self, observer: AbstractObserver):
        self.__observers.add(observer)

    def detach(self, observer: AbstractObserver):
        self.__observers.remove(observer)

    def hack_event(self):
        for observer in self.__observers:
            observer.do_something()

