from sqlmodel import Field, SQLModel, Session

from app.models.users import User
from app.models import users


# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: str | None = None


class NewPassword(SQLModel):
    token: str
    new_password: str = Field(min_length=8, max_length=40)

    

def authenticate(*, session: Session, email: str, password: str) -> User | None:
    db_user = users.get_user_by_email(session=session, email=email)
    if not db_user:
        return None
    if not users.verify_password(password, db_user.hashed_password):
        return None
    return db_user