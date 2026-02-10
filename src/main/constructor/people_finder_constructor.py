from src.view.people_finder_view import PeopleFinderView
from src.controllers.people_finder_controller import PeopleFinderController

def people_finder_constructor():
    finder_person_view = PeopleFinderView()
    people_finder_controller = PeopleFinderController()
    # controller

    person_find_informations = finder_person_view.finder_person_view()
    response = people_finder_controller.find_by_name(person_find_informations)
    # enviar para controller

    if response['success']:
        finder_person_view.find_person_success(response["message"])
    else:
        finder_person_view.find_person_fail(response["error"])
