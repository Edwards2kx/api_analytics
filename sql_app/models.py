from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , Float, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class DeviceInfo(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String)
    operative_system = Column(String)
    so_version = Column(String)
    manufacturer = Column(String)
    model = Column(String)
    cpu = Column(String)
    is_physical_device = Column(Boolean)
    ram_size = Column(Integer)
    total_storage = Column(Float)
    free_storage = Column(Float)


class WifiNetworkItem(Base):
    __tablename__ = "wifi_network_info"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String)
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
    device_id = Column(String)
    latitute = Column(Float)
    longitude = Column(Float)
    altitude = Column(Float)
    is_mocked = Column(Boolean)
    time_stamp = Column(DateTime)
    country = Column(String)
    administrative_area = Column(String)
    locality = Column(String)
    
class FinancialServiceApp(Base):
    __tablename__ = "financial_service_apps"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String)
    package_name = Column(String)
    app_name = Column(String)
    os_name = Column(String)

class ConnectedDevice(Base):
    __tablename__ = "connected_devices"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String)
    uuid = Column(String)
    name = Column(String)

