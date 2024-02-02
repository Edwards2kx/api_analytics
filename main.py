#API modulo de analitica en Flutter

#external imports
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List
#internal imports
from routers import config_info , pdf_generator ,analytic_info
from sql_app import info_router


# from sql_app import main

app = FastAPI()

# routers
app.include_router(config_info.router)
app.include_router(info_router.router)
app.include_router(pdf_generator.router)

# *modelo de informacion recibida


# para correr el servidor
#uvicorn main:app --reload

# si se presentan problemas de que no se reconoce el comando correr con
#python -m uvicorn main:app --reload

#para conocer las librerias instaladas de python usar pip freeze

#para ver la documentacion ingresar a 
#http://127.0.0.1:8000/docs
#http://127.0.0.1:8000/redocs


#realizar un modelado de una clase basica que sera la recibida desde el plugin flutter