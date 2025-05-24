# user/domain/repository/user_repo.py
from abc import ABCMeta, abstractmethod
from user.domain.user import User

class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user: User):
        raise NotImplementedError
    
    @abstractmethod
    def find_by_email(self, email: str) -> User:
        # 이메일을 기준으로 유저 검색
        # if searching result False, raise 422 Err
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def update(self, user: User):
        raise NotImplementedError
    
    @abstractmethod
    def get_users(
        self,
        page: int,
        items_per_page: int,
        ) -> tuple[int, list[User]]:
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, id: str):
        raise NotImplementedError