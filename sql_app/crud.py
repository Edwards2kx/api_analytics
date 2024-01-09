from sqlalchemy.orm import Session

from . import models, schemas

from typing import List, Union

def create_device_info(db: Session, device_info: schemas.DeviceInfoCreated):
    #TODO: si ya existe el ID debe actualizar la información
    #* actualmente se registra un ID autoincremental por motivos de prueba
    db_device_info = models.DeviceInfo(**device_info.model_dump())
    db.add(db_device_info)

def get_device_info(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DeviceInfo).offset(skip).limit(limit).all()

def create_location_info(db:Session, location_info: schemas.LocationCreated):
    db_location_info = models.Location(**location_info.model_dump())
    db.add(db_location_info)

#*recibe una lista
def create__wifi_network_info(db : Session, wifi_network_info : List[schemas.WifiNetworkItemCreated]):
    print(f'se recibio una lista con {len(wifi_network_info)}')
    for item in wifi_network_info:
        db_wifi_item = models.WifiNetworkItem(**item.model_dump())
        db.add(db_wifi_item)

def save_info_bundle (db: Session, infoBundle: schemas.InfoBundleCreated):
    print('ingreso en save_info_bundle')
    create_device_info(db, infoBundle.user_data.device_data)
    create_location_info(db, infoBundle.user_data.location)
    create__wifi_network_info(db, infoBundle.user_data.wifi_network_list)
    db.commit()   
