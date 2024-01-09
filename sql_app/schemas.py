from pydantic import BaseModel
from datetime import datetime
from typing import List, Union

#Device Info class
class DeviceInfoBase(BaseModel):
    operative_system:str
    so_version:str
    manufacturer:str
    model:str
    cpu:str
    is_physical_device:bool
    ram_size:int
    identifier: str
    total_storage: Union[float , None]
    free_storage:Union[float , None]

class DeviceInfoCreated(DeviceInfoBase): 
    pass   

class DeviceInfo(DeviceInfoBase):
    id : str

    class Config:
        orm_mode = True

#locationInfo class
class LocationBase(BaseModel):
    latitute: float
    longitude : float
    altitude:float
    is_mocked : bool
    time_stamp : datetime 
    country: str
    administrative_area: Union [str , None] 
    locality: Union [str , None]

class LocationCreated(LocationBase):
    pass

class Location(LocationBase):
    id : str

    class Config:
        orm_mode = True


class WifiNetworkItemBase(BaseModel):
    ssid : str
    bssid : str
    time_stamp : datetime
    level_in_db : int
    capabilities : str
    frequency: int
    channel_width : int

class WifiNetworkItemCreated(WifiNetworkItemBase):
    pass

class WifiNetworkItem(WifiNetworkItemBase):
    id : str
    class Config:
        orm_mode = True

# class Location(BaseModel):
#     latitute: float
#     longitude : float
#     altitude : float
#     is_mocked : bool
#     time_stamp : datetime 
#     country : str
#     administrative_area : str
#     locality : str
    
# class InstalledAppItem(BaseModel):
#     app_name : str
#     package_name : str
#     version_name : str
        
    
class UserData(BaseModel):
    device_data : DeviceInfoCreated
    location : LocationCreated
    wifi_network_list : List[WifiNetworkItemCreated]
    network_type : str
    # bt_device_list : List[str]
    # installed_app_list : List[InstalledAppItem]

class InfoBundleBase(BaseModel):
    unique_id : str
    user_data: UserData


class InfoBundleCreated(InfoBundleBase):
    pass

class InfoBundle(InfoBundleBase):
    id : str
    class Config:
        orm_mode = True
 

