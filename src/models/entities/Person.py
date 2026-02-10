class Person:
    def __init__(self, name: str, age: int, height: float):
        self._name = name
        self._age = age
        self._height = height

    
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def height(self):
        return self._height