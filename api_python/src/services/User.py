from fastapi import Depends

from ..repository.User import User


class User():
    def __init__(self,
                 userRepository: User = Depends()
                 ) -> None:
        self.userRepository = userRepository

    def find(self):
        return self.userRepository.find()

    def insert(self, item):
        self.userRepository.insert(item)
