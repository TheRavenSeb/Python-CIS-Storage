
import Logger as logger
import datetime
logger_intance = logger()
class Garage():

    def __init__(self):

        self.ParkingSpotSet = () # Only Spots
        self.ParkingCarList = [] # Only Cars
        self.lisencePlateSet = () # Only Lisence Plates
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
            if spot not in self.ParkingSpotSet:
                return logger_intance.error(f"[GARAGE] Spot {spot} is not available")
            if Car.getParkingSpot() != None:
                return logger_intance.error(f"[GARAGE] Car {Car.UUID} is already parked in spot {Car.Pspot}")
            else:
                Car.enterTime = datetime.datetime.now()
                Car.setParkingSpot(spot)
                self.ParkingCarList.push(Car)
                logger_intance.info(f"[GARAGE] {Car.UUID} parked into spot {Car.Pspot}")
                self.ParkingSpotSet.remove(spot)
                logger_intance.debug(f"[GARAGE] {Car.Pspot} now unavailable")
                self.lisencePlateSet.add(Car.License)

        def unpark(self,Car):
            """ """
            Car.exitTime = datetime.datetime.now()
            DidPay = self.pay(Car)
            if DidPay:
                
                self.ParkingSpotSet.add(Car.Pspot)
                logger_intance.debug(f"[GARAGE] {Car.Pspot} now avaiable")
                self.lisencePlateSet.remove(Car.License)
                self.ParkingCarList.remove(Car)
            
                return logger_intance.info("[CAR] Unparked from slot: " + self.parkingSlot)
            else:
               return logger_intance.error(f"{Car.UUID} IS POOR THEY MAY NOT LEAVE!!")
        
        def pay(self,Car):
            """ Action to make car pay for the amount of time they have been parked $1 = 1 hour
            @param Car: Car class object
            @return: amount of money paid
            """
            
            if Car.Status == "Paid":
                return logger_intance.error(f"[CAR] {Car.UUID} has already paid")
            else:
                time = Car.getParkingTimeInHours()
                IsOverTwoHours = time > 2
                if IsOverTwoHours:
                    time = time * 2 # Multiply by 2 for over two hours as a fee
                amount = time * 1 # Converts to dollars
                amount = "$" + str(amount)
                
                Car.Status = "Paid"
                logger_intance.info(f"[CAR] {Car.UUID} has paid {amount} ")
                return True
        def getCapacity(self):
            """
            Returns the total capacity of the garage.
            """
            return len(self.ParkingCarList)    
            
            


