from typing import Hashable, Callable
from models import Light, Camera
from .observer import AbstractObserver


class Factory(object):
    @staticmethod
    def get(class_name: Hashable) -> AbstractObserver:
        if not isinstance(class_name, Hashable):
            raise ValueError("Параметр class_name должен быть хэшируемым!")

        classes: dict[Hashable, Callable[..., AbstractObserver]] = {
            "Camera": Camera,
            "Light": Light
        }

        class_ = classes.get(class_name, None)
        if class_ is not None:
            return class_()

        raise ValueError
