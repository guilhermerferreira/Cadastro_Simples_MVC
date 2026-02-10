from src.models.entities.Person import Person

class __PersonRepository:
    def __init__(self):
        self._people = []

    def registry_person(self, person: Person) -> None:
        self._people.append(person)

    def find_person_by_name(self, name: str) -> Person:
        for person in self._people:
            if person.name == name:
                return person
            return None 
        
person_repository = __PersonRepository()