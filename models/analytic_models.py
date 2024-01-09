from pydantic import BaseModel
from datetime import datetime
from typing import List, Union


class DeviceInfo(BaseModel):
    operative_system:str
    so_version:str
    manufacturer:str
    model:str
    cpu:str
    is_physical_device:bool
    ram_size:int
    identifier: Union[str , None ]
    total_storage: Union[float , None]
    free_storage:Union[float , None]

# class LocationInfo(BaseModel):
#     latitute: float
#     longitude : float
#     altitude:float
#     is_mocked : bool
#     time_stamp : datetime 
#     country: str
#     administrative_area: Union [str , None] 
#     locality: Union [str , None]
    
class WifiNetworksItem(BaseModel):
    ssid : str
    bssid : str
    time_stamp : datetime
    level_in_db : int
    capabilities : str
    frequency: int
    channel_width : int
    
class Location(BaseModel):
    latitute: float
    longitude : float
    altitude : float
    is_mocked : bool
    time_stamp : datetime 
    country : str
    administrative_area : str
    locality : str
    
class InstalledAppItem(BaseModel):
    app_name : str
    package_name : str
    version_name : str
        
    
class UserData(BaseModel):
    device_data : DeviceInfo
    location : Location
    network_type : str
    # wifi_network_list : List[WifiNetworksItem]
    # bt_device_list : List[str] #TODO: reemplazar por el correcto
    # installed_app_list : List[InstalledAppItem]

class InfoBundle(BaseModel):
    unique_id : str
    user_data: UserData
