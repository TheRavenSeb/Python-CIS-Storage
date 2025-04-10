
import Logger as logger
logger_intance = logger()
class Garage():

    def __init__(self):

        self.ParkingSpotSet = () # Only Spots
        self.ParkingCarList = [] # Only Cars
        """car:{

            Ctype:"suv",
            License:"132932398239",
            UUID:"1",
            Pspot:"1A1",
            enterTime:timestamp,
            exitTime:timestamp,
            Status:"Parked"

        }"""

        def GetCars(self):
            return self.ParkingCarList

        def GetSpots(self):
            return self.ParkingSpotSet

        def park(Car, spot):
            Car.Pspot =  spot
            self.ParkingCarList.push(Car)
            logger_intance.info(f"{Car.UUID} parked into spot {Car.Pspot}")

        def GTFO(self,Car): # was not my idea -Caleb
            """ Makes them fucking leave"""
            DidPay = self.pay(Car)
            if DidPay:
                self.ParkingSpotSet.add(Car.Pspot)
                logger_intance.debug(f"{Car.Pspot} now avaiable")
                self.ParkingCarList.remove(Car)
            
                return logger_intance.info("Car unparked from slot: " + self.parkingSlot)
            else:
               return logger_intance.error(f"{Car.UUID} IS POOR THEY MAY NOT LEAVE!!")
        
        
            


