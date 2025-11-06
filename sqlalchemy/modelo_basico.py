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
#Así se crea la base de datos en la raíz del proyecto
#DATABASE_URL = "sqlite:///./productos_prueba.db"

#Así se crea la base de datos en una carpeta llamada SQLalchemy
DATABASE_URL = "sqlite:///SQLalchemy/productos_prueba.db"

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
try:
    productos_existentes = db.query(ProductoORM).first()
    if not productos_existentes:
        productos = [
            ProductoORM(id=1, nombre="Leche", precio=1.99, stock=100, disponible=True),
            ProductoORM(id=2, nombre="Queso", precio=15.49, stock=50, disponible=True),
            ProductoORM(id=3, nombre="Yogur", precio=3.99, stock=200, disponible=False),
        ]
        db.add_all(productos)
        db.commit()
finally:
    db.close()
    
    