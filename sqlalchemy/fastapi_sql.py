"""
API REST de FastAPI con SQLAlchemy y SQLite    
    """
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Integer, String, Float, Boolean, DateTime, Date
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from datetime import date, datetime
from typing import Optional

#Configurar la base de datos
engine = create_engine("sqlite:///ecommerce.db")
SessionLocal = sessionmaker(bind=engine)
    
#Crear la clase Base
class Base(DeclarativeBase):
    pass

#Crear entidades que heredan de Base(models.py)
class Product(Base):
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    #Limitamos el tamaño del String a 100 caracteres para el nombre
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
   
#Crear DTOs con Pydantic (schemas.py)
class ProductDTO(BaseModel):
    nombre: str | None = None
    
#Crear las tablas en la base de datos
Base.metadata.create_all(engine)

#API REST FastAPI con SQLAlchemy
app = FastAPI(title="Products App", version="1.0.0")

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a Products API"}

#API REST:
#GET all products JSON
@app.get("/api/products")
def find_all():
   session = SessionLocal()
   products = session.query(Product).all()
   session.close()
   return products

#GET one product


#POST create product
@app.post("/api/products")
def create(product_dto: ProductDTO):
    session = SessionLocal()
    product = Product(nombre=product_dto.nombre)
    session.add(product)
    session.commit()
    session.refresh(product)
    session.close()
    return product


#PUT update product
#DELETE delete product


#HTML:
#GET all products in HTML
#GET one product in HTML
#POST create/update product in HTML