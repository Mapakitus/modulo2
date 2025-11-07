from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Integer, String, Float, Boolean, DateTime, Date
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from datetime import date, datetime
from typing import Optional

app = FastAPI()

# base declarativa
class Base(DeclarativeBase):
    pass

class Usuario(BaseModel):
    nombre: str
    email: str
    edad: int
    
# modelo ORM SQLAlchemy (tabla)
class UsuarioORM(Base):
    __tablename__ = "usuarios"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    edad: Mapped[int] = mapped_column(Integer, nullable=False)

#Libro
class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    
# modelo ORM SQLAlchemy (tabla)
class LibroORM(BaseModel):
    __tablename__ = "libros"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String, nullable=False)
    autor: Mapped[str] = mapped_column(String, nullable=False)
    paginas: Mapped[int] = mapped_column(Integer, nullable=False)

#Categoria
class Categoria(BaseModel):
    nombre: str
    codigo: str    
    
# modelo ORM SQLAlchemy (tabla)
class CategoriaORM(BaseModel):
    __tablename__ = "categorias"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    codigo: Mapped[str] = mapped_column(String, nullable=False)
    
#PRODUCTO
class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int
    disponible: bool    
    
# modelo ORM SQLAlchemy (tabla)
class ProductoORM(BaseModel):
    __tablename__ = "productos"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    precio: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    disponible: Mapped[bool] = mapped_column(Boolean, nullable=False)
    
#EVENTO
class Evento(BaseModel):
    titulo: str
    fecha: date
    hora_incio: datetime
    capacidad: int
    activo: bool
    
# modelo ORM SQLAlchemy (tabla)
class EventoORM(BaseModel):
    __tablename__ = "eventos"       
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String, nullable=False)
    fecha: Mapped[date] = mapped_column(Date, nullable=False)
    hora_incio: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    capacidad: Mapped[int] = mapped_column(Integer, nullable=False)
    activo: Mapped[bool] = mapped_column(Boolean, nullable=False)
    
#CLIENTE
class Cliente(BaseModel):
    nombre: str
    email: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    
# modelo ORM SQLAlchemy (tabla)
class ClienteORM(BaseModel):
    __tablename__ = "clientes"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    telefono: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    direccion: Mapped[Optional[str]] = mapped_column(String)
    
#ARTICULO
class Articulo(BaseModel):
    titulo: str
    contenido: str
    autor: str
    fecha_publicacion: Optional[date] = None
    vistas: Optional[int] = 0
    
# modelo ORM SQLAlchemy (tabla)
class ArticuloORM(BaseModel):
    __tablename__ = "articulos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String, nullable=False)
    contenido: Mapped[str] = mapped_column(String, nullable=False)
    autor: Mapped[str] = mapped_column(String, nullable=False)
    fecha_publicacion: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    vistas: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, default=0)