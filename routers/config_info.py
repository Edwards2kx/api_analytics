#external imports
from fastapi import APIRouter
#from pydantic import BaseModel

router = APIRouter()

thirPartyApps = [
    "nequi", "ahorro a la mano", "bancolombia"
]
#TODO: prepara listado de app packages para android y enviar en este endpoint
#TODO: guiarse del listado de veloxity

@router.get("/config")
async def root():
    return {"aplicaciones": thirPartyApps}
