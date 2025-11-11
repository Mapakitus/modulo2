from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, Integer, String, Float, Boolean, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, Session

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
    
#modelos pydantic (schemas)
class SongResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    artist: str
    duration_seconds: int | None
    explicit: bool | None

#modelo para crear canciones (POST)
class SongCreate(BaseModel):
    title: str
    artist: str
    duration_seconds: int | None = None
    explicit: bool | None = None
    
#modelo para actualizar canciones (PUT)
#Todos los campos son obligatorios
class SongUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    title: str 
    artist: str
    duration_seconds: int | None 
    explicit: bool | None
    
#modelo para actualizar canciones parcialmente (PATCH)
#solo se envían los campos a modificar
class SongPatch(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    title: str | None = None
    artist: str | None = None
    duration_seconds: int | None = None
    explicit: bool | None = None
    
#Inicialización de la base de datos: crear tablas
Base.metadata.create_all(bind=engine)  

#método para incializar canciones por defecto
def init_db():
    """
    Inicializa la base de datos con canciones por defecto si no existen canciones.
    Sólo crea las canciones si no existen ya en la base de datos.
    """
    db = SessionLocal()
    try:
        #Extraigo los objetos Song de mi consulta y los convierto en una lista
        existing_song = db.execute(select(Song)).scalars().all()
        
        if existing_song:
            print("Canciones ya existen en la base de datos. No se crearán canciones por defecto.")
            return
        
        #Si no hay canciones, crear canciones por defecto
        default_songs = [
            Song(title="Imagine", artist="John Lennon", duration_seconds=183, explicit=False),
            Song(title="Billie Jean", artist="Michael Jackson", duration_seconds=294, explicit=False),
            Song(title="Smells Like Teen Spirit", artist="Nirvana", duration_seconds=301, explicit=True),
            Song(title="Bohemian Rhapsody", artist="Queen", duration_seconds=354, explicit=False),
            Song(title="Like a Rolling Stone", artist="Bob Dylan", duration_seconds=369, explicit=False),
            Song(title="Hotel California", artist="Eagles", duration_seconds=390, explicit=False),
            Song(title="Hey Jude", artist="The Beatles", duration_seconds=431, explicit=False),
            Song(title="Stairway to Heaven", artist="Led Zeppelin", duration_seconds=482, explicit=False),
            Song(title="Thriller", artist="Michael Jackson", duration_seconds=358, explicit=False),
            Song(title="Paranoid Android", artist="Radiohead", duration_seconds=386, explicit=True)
        ]  
        
        #Agregar las canciones por defecto a la sesión
        db.add_all(default_songs)
        db.commit()
        print("Canciones por defecto creadas en la base de datos.")
    finally:
        db.close()
        
#Llamar a la función de inicialización de la base de datos
init_db()

#dependencia de fastapi para obtener sesión de base de datos
def get_db():
    """
    Dependencia de FastAPI para obtener una sesión de base de datos.
    Se usa en los endpoints para interactuar con la base de datos.
    """
    db = SessionLocal()
    try:
        yield db #entrega la sesión al endpoint
    finally:
        db.close()

#aplicación FastAPI

#Crea la instancia de la aplicación FastAPI
app = FastAPI(title="Cancioncitas API", version="1.0.0")

#endpoint raíz
@app.get("/")
def home():
    return {"mensaje": "Welcome to the Cancioncitas API!"}

#ENDPOINTS CRUD

# GET - obtener TODAS las canciones
@app.get("/api/songs", response_model=list[SongResponse])
def find_all(db: Session = Depends(get_db)):
    #db.execute(): para ejecutar la consulta
    #select(Song): crea consulta SELECT * FROM songs
    #.scalars(): extrae los objetos Song de la consulta
    #.all(): convierte los objetos en una lista
    return db.execute(select(Song)).scalars().all()

# GET - obtener UNA canción por ID
@app.get("/api/songs/{id}", response_model=SongResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    #buscar canción por id de la ruta con un select y devuelve el objeto 
    # o None si no existe
    song = db.execute(
        select(Song).where(Song.id == id)
    ).scalar_one_or_none()
    
    if not song:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"No se ha encontrado la canción con id {id}"
        )
    return song