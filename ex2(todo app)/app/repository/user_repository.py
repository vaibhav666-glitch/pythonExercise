from uuid import UUID

from sqlalchemy.orm import Session

from app.models import User
from app.repository.interfaces import IUserRepository
from app.schemas import UserCreate


class UserRepository(IUserRepository):

    def __init__(self, db: Session):
        self.db = db

    def create(self, user: UserCreate) -> User:
        """
        Create a new user.
        """

        db_user = User(
            full_name=user.full_name,
            email=user.email,
            password=user.password,
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user

    def get_by_id(self, user_id: UUID) -> User | None:
        """
        Retrieve user by ID.
        """

        return (
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    def get_by_email(self, email: str) -> User | None:
        """
        Retrieve user by email.
        """

        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )