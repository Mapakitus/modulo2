from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, Integer, String, Float, Boolean, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, Session

"""
VIDEO
- id: integer (autoincremental, clave primaria)
- title: string (obligatorio)
- channel: string (obligatorio)
- views: integer (opcional)
- has_subtitles: boolean (opcional)
"""

# CONFIGURACIÓN BASE DE DATOS

engine = create_engine(
    "sqlite:///SQLalchemy/videos.db", echo=True,
    connect_args={"check_same_thread": False}
)

#Crear fábrica de sesiones de base de datos
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=True,
    expire_on_commit=False,
    bind=engine
)

# MODELO DE BASE DE DATOS (SQLALCHEMY)

#clase base para modelos sqlalchemy, esto es para metadatos de las tablas
class Base(DeclarativeBase):
    pass

#modelo de la tabla videos
class Video(Base):
    __tablename__ = "videos"
    
    #Clave primaria
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    #requerido
    title: Mapped[str] = mapped_column(String, nullable=False)
    #requerido
    channel: Mapped[str] = mapped_column(String, nullable=False)
    #opcional
    views: Mapped[int | None] = mapped_column(Integer, nullable=True)
    #opcional
    has_subtitles: Mapped[bool | None] = mapped_column(Boolean, nullable=True)


# MODELO PYDANTIC (SCHEMAS)
class VideoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    channel: str
    views: int | None
    has_subtitles: bool | None

#Crear videos (POST)
class VideoCreate(BaseModel):
    title: str
    channel: str
    views: int | None = None
    has_subtitles: bool | None = None

#Actualizar videos completamente (PUT)
class VideoUpdateFull(BaseModel):
    title: str
    channel: str
    views: int | None = None
    has_subtitles: bool | None = None
    
#Actualizar videos parcialmente (PATCH)
class VideoUpdatePartial(BaseModel):
    title: str | None = None
    channel: str | None = None
    views: int | None = None
    has_subtitles: bool | None = None

# INICIALIZAR BASE DE DATOS (CREAR TABLAS)
Base.metadata.create_all(bind=engine)

#método para incializar canciones por defecto
def init_db():
    """
    Inicializa la base de datos con videos por defecto si no existen videos.
    Sólo crea los videos si no existen ya en la base de datos.
    """
    db = SessionLocal()
    try:
        #Extraigo los objetos Video de mi consulta y los convierto en una lista
        existing_video = db.execute(select(Video)).scalars().all()
        
        if existing_video:
            print("Ya existen videos en la base de datos. No se crearán videos por defecto.")
            return
        
        #Si no hay videos, crear videos por defecto
        default_videos = [
            Video(title="Mi primer video", channel="Ma Pakitus", views=183, has_subtitles=False),
            Video(title="Mi segundo video", channel="Ma Pakitus", views=1000, has_subtitles=False),
            Video(title="Mi tercer video", channel="Ma Pakitus", views=1200, has_subtitles=True),
            Video(title="Mi cuarto video", channel="Ma Pakitus", views=1830, has_subtitles=False),
            Video(title="Mi quinto video", channel="Ma Pakitus", views=2000, has_subtitles=False),
            Video(title="Mi sexto video", channel="Ma Pakitus", views=35000, has_subtitles=True),
            Video(title="Mi sépitmo video", channel="Ma Pakitus", views=15, has_subtitles=False),
            Video(title="Mi octavo video", channel="Ma Pakitus", views=789, has_subtitles=True),
            Video(title="Mi noveno video", channel="Ma Pakitus", views=1234, has_subtitles=False)
        ]  
        
        #Agregar los videos por defecto a la sesión
        db.add_all(default_videos)
        db.commit()
        print("Videos por defecto creadas en la base de datos.")
    finally:
        db.close()
        
#Llamar a la función de inicialización de la base de datos
init_db()
 

# DEPENDENCIA DE FASTAPI
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
        
# APLICACIÓN FASTAPI
#Crea la instancia de la aplicación FastAPI
app = FastAPI(title="Ma Pakitus Videos", version="1.0.0")

#endpoint raíz
@app.get("/")
def home():
    return {"mensaje": "Welcome to Ma Pakitus Videos API!"}

# ENDPOINTS CRUD (CREATE, READ, UPDATE, DELETE)
"""
Create: Método POST para agregar un nuevo video.
Read: Método GET para obtener videos (find_all y find_by_id)
Update: Método PUT y PATCH para actualizar un video existente. (update_full y update_partial)
Delete: Método DELETE para eliminar un video por su id. (delete)
"""

# GET - obtener TODOS los videos
@app.get("/api/videos", response_model=list[VideoResponse])
def find_all(db: Session = Depends(get_db)):
    #db.execute(): para ejecutar la consulta
    #select(Song): crea consulta SELECT * FROM videos
    #.scalars(): extrae los objetos Video de la consulta
    #.all(): convierte los objetos en una lista
    return db.execute(select(Video)).scalars().all()

# GET - obtener UN video por ID
@app.get("/api/videos/{id}", response_model=VideoResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    #buscar video por id de la ruta con un select y devuelve el objeto 
    # o None si no existe
    video = db.execute(
        select(Video).where(Video.id == id)
    ).scalar_one_or_none()
    
    if not video:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"No se ha encontrado el video con id {id}"
        )
    return video

# POST - crear un video
@app.post("/api/videos", response_model=VideoResponse, status_code=status.HTTP_201_CREATED)

def create(video_dto: VideoCreate, db: Session = Depends(get_db)):
    
    #validaciones básicas, el strip es para eliminar espacios en blanco delante y detrás
    if not video_dto.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El título del video no puede estar vacío."
        )       
        
    if not video_dto.channel.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El canal del video no puede estar vacío."
        )
        
    if video_dto.views is not None and video_dto.views < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El número de visualizaciones no puede ser negativo."
        )
    
    #crear objeto Video a partir del DTO
    video = Video(
        title=video_dto.title.strip(),
        channel=video_dto.channel.strip(),
        views=video_dto.views,
        has_subtitles=video_dto.has_subtitles
    )
    
    #agrega el objeto a la sesión
    db.add(video)
    #guarda el objeto en la base de datos
    db.commit()
    #refresca el objeto para obtener el id generado
    db.refresh(video)
    #devuelve el objeto creado
    return video

# PUT - actualizar COMPLETAMENTE un video
@app.put("/api/videos/{id}", response_model=VideoResponse)
def update_full(id: int, video_dto: VideoUpdateFull, db: Session = Depends(get_db)):
    #buscar video por id
    video = db.execute(
        select(Video).where(Video.id == id)
    ).scalar_one_or_none()
    
    if not video:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"No se ha encontrado el video con id {id}"
        )
    
    #validaciones básicas
    if not video_dto.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El título del video no puede estar vacío."
        )       
        
    if not video_dto.channel.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre del canal no puede estar vacío."
        )
        
    if video_dto.views is not None and video_dto.views < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El número de visualizaciones no puede ser negativo."
        )
    
    #actualizar campos
    video.title = video_dto.title.strip()
    video.channel = video_dto.channel.strip()
    video.views = video_dto.views
    video.has_subtitles = video_dto.has_subtitles
    
    
    #guardar cambios en la base de datos
    db.commit()
    #refrescar objeto
    db.refresh(video)
    return video

# PATCH - actualizar PARCIALMENTE un video
@app.patch("/api/videos/{id}", response_model=VideoResponse)
def update_partial(id: int, video_dto: VideoUpdatePartial, db: Session = Depends(get_db)):
    video = db.execute(
        select(Video).where(Video.id == id)
    ).scalar_one_or_none()
    
    if not video:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"No se ha encontrado el video con id {id}"
        )
    #actualizar solo los campos que no son None
    if video_dto.title is not None:
        if not video_dto.title.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El título del video no puede estar vacío."
            )
        video.title = video_dto.title.strip()
    
    if video_dto.channel is not None:
        if not video_dto.channel.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El nombre del canal no puede estar vacío."
            )
        video.channel = video_dto.channel.strip()
        
    if video_dto.views is not None:
        if video_dto.views < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Las visualizaciones no pueden ser negativas."
            )
        video.views = video_dto.views
        
    if video_dto.has_subtitles is not None:
        video.has_subtitles = video_dto.has_subtitles
        
    #guardar cambios en la base de datos
    db.commit()
    #refrescar objeto
    db.refresh(video)
    return video

# DELETE - eliminar un video por ID
@app.delete("/api/videos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    video = db.execute(
        select(Video).where(Video.id == id)
    ).scalar_one_or_none()
    
    if not video:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"No se ha encontrado el video con id {id}"
        )
    
    #eliminar video
    db.delete(video)
    db.commit()
    return None