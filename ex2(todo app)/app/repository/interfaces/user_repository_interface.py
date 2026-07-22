from abc import ABC, abstractmethod
from uuid import UUID

from app.models import User
from app.schemas import UserCreate


class IUserRepository(ABC):
    """
    Contract for user repository implementations.
    """

    @abstractmethod
    def create(self, user: UserCreate) -> User:
        """Create a new user."""
        pass

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> User | None:
        """Retrieve a user by ID."""
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        """Retrieve a user by email."""
        pass