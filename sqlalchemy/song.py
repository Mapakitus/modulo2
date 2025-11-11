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

