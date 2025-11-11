from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

app = FastAPI()


#Configurar base de datos
# está en mayúsculas porque es una constante (no cambia)

engine = create_engine(
    "sqlite:///SQLalchemy/cancioncitas.db", echo=True,
    connect_args={"check_same_thread": False}
)

#Crear fábrica de sesiones de base de datos
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=True,
    expire_on_commit=False,
    bind=engine
)

#modelo base de datos (sqlalchemy)

#clase base para modelos sqlalchemy, esto es para metadatos de las tablas
class Base(DeclarativeBase):
    pass

#modelo de la tabla song
class Song(Base):
    __tablename__ = "songs"
    
    #Clave primaria
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    #requerido máximo 200 caracteres
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    #requerido máximo 200 caracteres
    artist: Mapped[str] = mapped_column(String(200), nullable=False)
    #opcional
    duration_seconds: Mapped[int | None] = mapped_column(Integer, nullable=True)
    #opcional
    explicit: Mapped[bool | None] = mapped_column(Boolean, nullable=True)