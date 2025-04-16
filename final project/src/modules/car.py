    
        
from datetime import datetime
from uuid import uuid4
from typing import Optional

class Car:
    def __init__(self, carType: str, license: str, uuid: Optional[str] = None):
        self.carType = carType
        self.license = license
        self.UUID = uuid if uuid else str(uuid4())
        self.pSpot = None
        self.enterTime = None
        self.exitTime = None
        self.status = "Parked"
        """
        Car class to represent a car object.
        Attributes:
        - carType (str): Type of the car (e.g., SUV, sedan).
        - license (str): License plate of the car.
        - UUID (str): Unique identifier for the car.
        - pSpot (str): Parking spot assigned to the car.
        - enterTime (datetime): Timestamp when the car entered the parking.
        - exitTime (datetime): Timestamp when the car exited the parking.
        - status (str): Current status of the car (e.g., parked, exited).
        Methods:
        - __init__(self, carType, license, uuid): Initializes a new car object with the given attributes.
        - __str__(self): Returns a string representation of the car object.
        - getEnterTime(self): Returns the enter time of the car.
        - getExitTime(self): Returns the exit time of the car.
        - getStatus(self): Returns the status of the car.
        - setParkingSpot(self, spot): Sets the parking spot of the car.
        - getParkingSpot(self): Returns the parking spot of the car.
        - getLicense(self): Returns the license plate of the car.
        - getCarType(self): Returns the type of the car.
        - getUUID(self): Returns the unique identifier of the car.
        - getParkingTime(self): Returns the total parking time of the car in hours.
        - getParkingTimeInSeconds(self): Returns the total parking time of the car in seconds.

        - getParkingTimeInMinutes(self): Returns the total parking time of the car in minutes.
        - getParkingTimeInHours(self): Returns the total parking time of the car in days.
        """
    def __str__(self):
        return f"Car({self.carType}, {self.license}, {self.UUID}, {self.pSpot}, {self.enterTime}, {self.exitTime}, {self.status})"
    
    def getEnterTime(self):
        return self.enterTime
    
    def getExitTime(self):
        return self.exitTime
    
    def getStatus(self):
        return self.status
    
    def getParkingSpot(self):
        return self.pSpot
    
    def getLicense(self):
        return self.license
    
    def getCarType(self):
        return self.carType
    
    def getUUID(self):
        return self.UUID
    
    def setParkingSpot(self, spot):
        """
        Sets the parking spot of the car and updates the enter time and status.
        """
        self.pSpot = spot
        self.enterTime = datetime.now()
        self.status = "Parked"
        
        
    def getParkingTime(self):
        """
        Returns the total parking time of the car in hours.
        """
        if self.exitTime:
            return (self.exitTime - self.enterTime).total_seconds() / 3600
        else:
            return (datetime.now() - self.enterTime).total_seconds() / 3600
        
    def getParkingTimeInSeconds(self):
        """
        Returns the total parking time of the car in seconds.
        """
        if self.exitTime:
            return (self.exitTime - self.enterTime).total_seconds()
        else:
            return (datetime.now() - self.enterTime).total_seconds()
        
    def getParkingTimeInMinutes(self):
        """
        Returns the total parking time of the car in minutes.
        """
        if self.exitTime:
            return (self.exitTime - self.enterTime).total_seconds() / 60
        else:
            return (datetime.now() - self.enterTime).total_seconds() / 60
       
    def getParkingTimeInHours(self):
        """
        Returns the total parking time of the car in hours.
        """
        if self.exitTime:
            return (self.exitTime - self.enterTime).total_seconds() / 3600
        else:
            return (datetime.now() - self.enterTime).total_seconds() / 3600
        
    
        
        
    
    