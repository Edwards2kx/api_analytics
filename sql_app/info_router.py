from typing import Annotated
from fastapi import APIRouter, BackgroundTasks, Depends
from sql_app import crud
from sql_app.database import SessionLocal
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

def add_info_to_database(info: str):
    print(f'tarea en segundo plano para procesar {info}')
    pass

# @router.post("/infosql", response_model=schemas.DeviceInfo)
#TODO: cambiar codigo de respuesta HTTP de OK a CREATED
# def info(infoFromDevice : schemas.DeviceInfoCreated, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
@router.post("/infosql")
def save_info(infoFromDevice : schemas.DeviceInfoCreated, background_tasks: BackgroundTasks, db: db_dependency):
    background_tasks.add_task(add_info_to_database, info="información adicional")
    #TODO: enviar a una clase que se encargue de recibir el bundle y el luego lo separe en varios elementos al finalizar hacer el commit a la base de datos
    device_info_db = crud.create_device_info(db, infoFromDevice)
    return infoFromDevice


@router.post("/info")
async def save_info(infoBundle : schemas.InfoBundleCreated, background_tasks: BackgroundTasks, db: db_dependency):
    # background_tasks.add_task(add_info_to_database, info="información adicional")
    crud.save_info_bundle(db, infoBundle)
    return None

#? como evitar saturar el sistema por ataque DDoS?
#? recibir peticiones de cualquier origen o que contengan alguna key especial? como se generaria la key?
#? momento de procesado de datos, durante o despues de responder?
#? como se procede a pasar el proyecto a una maquina virtual usando configurancion de ambiente? 