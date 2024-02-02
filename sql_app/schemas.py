from pydantic import BaseModel
from datetime import datetime
from typing import List, Union

#Device Info class
class DeviceInfoBase(BaseModel):
    device_id: str
    operative_system:str
    so_version:str
    manufacturer:str
    model:str
    cpu:str
    is_physical_device:bool
    ram_size:int
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

class Location(BaseModel):
    latitute: float
    longitude : float
    altitude : float
    is_mocked : bool
    time_stamp : datetime 
    country : str
    administrative_area : str
    locality : str
    
class FinancialServiceAppItem(BaseModel):
    app_name : Union[str, None]
    package_name : str

class ConnectedDeviceItem(BaseModel):
    uuid : str
    name : Union[str, None]
        
class UserData(BaseModel):
    device_data : DeviceInfoCreated
    location : Union[LocationCreated , None]
    wifi_network_list : Union[List[WifiNetworkItemCreated] , None] 
    network_type : Union [str , None] 
    connected_devices_list : Union[List[ConnectedDeviceItem], None] 
    installed_app_list : Union[List[FinancialServiceAppItem], None] 

#   'location': location?.toMap(),
#       'wifi_network_list': wifiNetworkList?.map((x) => x.toMap()).toList(),
#       'device_data': deviceData?.toMap(),
#       'network_type': networkType,
#       'bt_device_list' : btDeviceInfoList?.map((x) => x.toMap()).toList(),
#       'connected_devices_list' : installedAppList?.map((x) => x.toMap()).toList(),

class InfoBundleBase(BaseModel):
    unique_id : str
    user_data: UserData

class InfoBundleCreated(InfoBundleBase):
    pass

class InfoBundle(InfoBundleBase):
    id : str
    class Config:
        orm_mode = True
 

