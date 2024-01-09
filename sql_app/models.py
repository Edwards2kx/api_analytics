from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , Float, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class DeviceInfo(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    operative_system = Column(String)
    so_version = Column(String)
    manufacturer = Column(String)
    model = Column(String)
    cpu = Column(String)
    is_physical_device = Column(Boolean)
    ram_size = Column(Integer)
    identifier = Column(String)
    total_storage = Column(Float)
    free_storage = Column(Float)

class WifiNetworkItem(Base):
    __tablename__ = "wifi_network_info"
    id = Column(Integer, primary_key=True, index=True)
    ssid = Column(String)
    bssid = Column(String)
    time_stamp  = Column(DateTime)
    level_in_db = Column(Integer)
    capabilities = Column(String)
    frequency = Column(Integer)
    channel_width = Column(Integer)
    
class Location(Base):
    __tablename__ = "location_info"
    id = Column(Integer, primary_key=True, index=True)
    latitute = Column(Float)
    longitude = Column(Float)
    altitude = Column(Float)
    is_mocked = Column(Boolean)
    time_stamp = Column(DateTime)
    country = Column(String)
    administrative_area = Column(String)
    locality = Column(String)
    

