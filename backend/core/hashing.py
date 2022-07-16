from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    @staticmethod
    def verify_pwd(pwd, hashed_pwd):
        return context.verify(pwd, hashed_pwd)

    @staticmethod
    def get_pwd_hash(pwd):
        return context.hash(pwd)
