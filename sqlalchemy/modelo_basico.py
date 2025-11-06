from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

app = FastAPI()


# modelo Pydantic
class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int
    disponible: bool


# configuración base de datos

# está en mayúsculas porque es una constante (no cambia)
DATABASE_URL = "sqlite:///./productos_prueba.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# base declarativa
class Base(DeclarativeBase):
    pass


# modelo ORM SQLAlchemy (tabla)
class ProductoORM(Base):
    __tablename__ = "productos"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    precio: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    disponible: Mapped[bool] = mapped_column(Boolean, nullable=False)


# crear las tablas
Base.metadata.create_all(bind=engine)

# crear sesión
db = SessionLocal()
    