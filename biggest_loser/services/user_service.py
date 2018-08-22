import datetime
from typing import Optional

from biggest_loser import DbSession
from biggest_loser.data.users import User
from biggest_loser.data.seasons import Season
from passlib.handlers.sha2_crypt import sha512_crypt


def get_users():
    session = DbSession.factory()
    return session.query(User).all()


def create_user(fname: str, lname: str, code_name: str, email: str, password: str) -> User:
    user = User()
    user.fname = fname
    user.lname = lname
    user.code_name = code_name
    user.email = email.lower().strip()
    user.hashed_password = hash_text(password)

    session = DbSession.factory()
    session.add(user)
    session.commit()

    return user


def hash_text(text: str) -> str:
    hashed_text = sha512_crypt.encrypt(text, rounds=150_000)
    return hashed_text


def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return sha512_crypt.verify(plain_text, hashed_text)


def login_user(email: str, password: str) -> Optional[User]:
    if not email:
        return None

    email = email.lower().strip()

    session = DbSession.factory()
    user = session.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_hash(user.hashed_password, password):
        return None
    user.last_login = datetime.datetime.now()
    session.commit()
    return user


def update_last_login(user: User):
    session = DbSession.factory()
    user.last_login = datetime.datetime.now()
    session.add(user)
    session.commit


def find_user_by_id(user_id: int) -> Optional[User]:
    session = DbSession.factory()
    return session.query(User).filter(User.id == user_id).first()
