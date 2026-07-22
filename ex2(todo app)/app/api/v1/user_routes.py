from fastapi import APIRouter, status

router = APIRouter()


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
)
async def register_user():
    """
    Temporary endpoint.

    This will later:
    - Validate request body
    - Call UserService
    - Hash password
    - Save user to database
    """

    return {
        "message": "Register endpoint is working"
    }


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    summary="Login user",
)
async def login_user():
    """
    Temporary endpoint.

    This will later:
    - Validate credentials
    - Verify password
    - Generate JWT
    - Return access token
    """

    return {
        "message": "Login endpoint is working"
    }