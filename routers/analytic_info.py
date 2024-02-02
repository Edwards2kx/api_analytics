# from fastapi import APIRouter, BackgroundTasks

# from models.analytic_models import InfoBundle

# router = APIRouter()

# def add_info_to_database(info: str):
#     print(f'tarea en segundo plano ejecutada sin problemas {info}')
#     pass

# @router.post("/")
# async def info(infoFromDevice : InfoBundle, background_tasks: BackgroundTasks):
#     background_tasks.add_task(add_info_to_database, info="some notification")
#     #TODO: identificar MAC de dispositivos bluetooth
#     #TODO: identificar POI segun coordenadas recibidas usando api de google maps
#     #TODO: guardar info en base de datos usando Alquemy libreria
#     return infoFromDevice
