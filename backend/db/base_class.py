from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: any
    __name__: str

    def __tablename__(cls) -> str:
        return cls.__name__.lower()
