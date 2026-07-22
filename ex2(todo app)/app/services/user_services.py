from app.models import User
from app.repository.interfaces.user_repository_interface import IUserRepository
from app.schemas import UserCreate, UserLogin


class UserService:
    """
    Handles all user-related business logic.
    """

    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def register(self, user: UserCreate) -> User:
        """
        Register a new user.
        """

        existing_user = self.repository.get_by_email(user.email)

        if existing_user:
            raise ValueError("User with this email already exists.")

        return self.repository.create(user)

    def login(self, user: UserLogin) -> User:
        """
        Authenticate user.

        Password verification and JWT generation
        will be added later.
        """

        existing_user = self.repository.get_by_email(user.email)

        if existing_user is None:
            raise ValueError("Invalid email or password.")

        return existing_user