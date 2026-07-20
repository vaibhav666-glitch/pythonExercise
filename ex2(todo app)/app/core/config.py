from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Database
    database_type: str
    database_host: str
    database_port: int
    database_name: str
    database_user: str
    database_password: str

    # JWT
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def database_url(self) -> str:
        """
        Build the database connection string based on the selected database.
        """

        if self.database_type.lower() == "postgres":
            return (
                f"postgresql+psycopg2://"
                f"{self.database_user}:{self.database_password}"
                f"@{self.database_host}:{self.database_port}"
                f"/{self.database_name}"
            )

        raise ValueError(
            f"Unsupported database type: {self.database_type}"
        )


@lru_cache
def get_settings() -> Settings:
    """
    Load settings only once during application startup.
    """
    return Settings()


settings = get_settings()