from sqlalchemy.orm import Session
from datetime import datetime

from . import models, schemas

from typing import List

def create_device_info(db: Session, device_info: schemas.DeviceInfoCreated):
    #TODO: si ya existe el ID debe actualizar la información
    #* actualmente se registra un ID autoincremental por motivos de prueba
    current_time = datetime.now()
    db_device_info = models.DeviceInfo(**device_info.model_dump())
    db.add(db_device_info)

def get_device_info(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.DeviceInfo).offset(skip).limit(limit).all()

def get_device_info_by_id (db: Session, unique_id: str):
    return db.query(models.DeviceInfo).filter(models.DeviceInfo.unique_id == unique_id).first()

def create_location_info(db: Session,  device_id: str , location_info: schemas.LocationCreated):
    db_location_info = models.Location(**location_info.model_dump())
    db_location_info.device_id = device_id
    db.add(db_location_info)


def create_connected_device_info(db: Session,  device_id: str , connected_devices: List[schemas.ConnectedDeviceItem]):
    #TODO: si ya existe registro con el device_id se deben agregar solo los nuevos elementos
    if connected_devices == None:
        return
    for item in connected_devices:
        connected_device_info = models.ConnectedDevice(**item.model_dump())
        connected_device_info.device_id = device_id
        db.add(connected_device_info)

# def create_location_info(db:Session, location_info: schemas.LocationCreated):
#     db_location_info = models.Location(**location_info.model_dump())
#     db.add(db_location_info)

def get_location_info(db:Session, skip: int = 0, limit: int = 1000):
    if limit == 0:
        return db.query(models.Location).all()
    else: 
        return db.query(models.Location).offset(skip).limit(limit).all()


def create_financial_services_apps(db:Session , device_info: schemas.DeviceInfoCreated, financial_services_apps : List[schemas.FinancialServiceAppItem] ):
    if financial_services_apps != None:
        for service in financial_services_apps:
            db_financial_app = models.FinancialServiceApp(**service.model_dump())
            db_financial_app.device_id = device_info.device_id
            db_financial_app.os_name = device_info.operative_system
            db.add(db_financial_app)


def get_financial_services_apps(db:Session, skip: int = 0, limit: int = 1000):
    if limit == 0:
        return db.query(models.FinancialServiceApp).all()
    else: 
        return db.query(models.FinancialServiceApp).offset(skip).limit(limit).all()

#*recibe una lista
def create__wifi_network_info(db : Session, wifi_network_info : List[schemas.WifiNetworkItemCreated]):
    print(f'se recibio una lista con {len(wifi_network_info)}')
    for item in wifi_network_info:
        db_wifi_item = models.WifiNetworkItem(**item.model_dump())
        db.add(db_wifi_item)

def save_info_bundle(db: Session, infoBundle: schemas.InfoBundleCreated):
    device_id = infoBundle.user_data.device_data.device_id
    print('ingreso en save_info_bundle')

    create_device_info(db, infoBundle.user_data.device_data)

    if infoBundle.user_data.location != None:
        create_location_info(db, device_id , infoBundle.user_data.location)

    if infoBundle.user_data.connected_devices_list != None:
        create_connected_device_info(db, device_id, infoBundle.user_data.connected_devices_list) 

    if infoBundle.user_data.installed_app_list != None:
        create_financial_services_apps(db, infoBundle.user_data.device_data, infoBundle.user_data.installed_app_list)

    if infoBundle.user_data.connected_devices_list != None:
        create_connected_device_info(db, device_id, infoBundle.user_data.connected_devices_list)

    # if infoBundle.user_data.wifi_network_list != None:
    #     create__wifi_network_info(db, infoBundle.user_data.wifi_network_list)

    # create_connected_device_info(db: Session, )    

    # create_location_info(db, infoBundle.user_data.location)
    # create__wifi_network_info(db, infoBundle.user_data.wifi_network_list)
    db.commit()   
