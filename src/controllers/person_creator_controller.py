from src.models.sqlite.interfaces.people_repository_interface import PeopleRepositoryInterfaces

class PersonCreatorController:
    def __init__(self, people_repository) -> None:
        self.people_repository = people_repository