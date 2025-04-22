from modules.Logger import logger
import datetime
logger_intance = logger()
class Garage():

    def __init__(self):

        self.ParkingSpotSet = set() # Set of parking spots
        # Adding 50 parking spots to the set with the format "1A1"
        for i in range(1, 6):  # 5 rows
            for j in range(1, 11):  # 10 spots per row
                self.ParkingSpotSet.add(f"{i}A{j}")
        self.ParkingCarList = [] # Only Cars
        self.lisencePlateSet = set() # Only Lisence Plates
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
        """ Returns the list of cars in the garage """
        return self.ParkingCarList

    def GetSpots(self):
        return self.ParkingSpotSet

    def park(self,Car, spot):
        if spot not in self.ParkingSpotSet:
            return logger_intance.error(f"[GARAGE] Spot {spot} is not available")
        if Car.getParkingSpot() != None:
            return logger_intance.error(f"[GARAGE] Car {Car.UUID} is already parked in spot {Car.pSpot}")
        else:
            Car.enterTime = datetime.datetime.now()
            Car.setParkingSpot(spot)
            self.ParkingCarList.append(Car)
            logger_intance.info(f"[GARAGE] {Car.UUID} parked into spot {Car.pSpot}")
            self.ParkingSpotSet.remove(spot)
            logger_intance.debug(f"[GARAGE] {Car.pSpot} now unavailable")
            self.lisencePlateSet.add(Car.license)

    def unpark(self, Car):
        """ Unparks a car from the garage """
        Car.exitTime = datetime.datetime.now()
        DidPay = self.pay(Car)
        if DidPay:
            self.ParkingSpotSet.add(Car.pSpot)
            logger_intance.info("[CAR] Unparked from slot: " + Car.pSpot)
            logger_intance.debug(f"[GARAGE] {Car.pSpot} now available")
            
            # Check if the license plate exists before removing
            if Car.license in self.lisencePlateSet:
                self.lisencePlateSet.remove(Car.license)
            else:
                logger_intance.error(f"[GARAGE] License plate {Car.license} not found in the set")
            
            self.ParkingCarList.remove(Car)
            return
        else:
            return logger_intance.error(f"{Car.UUID} IS POOR THEY MAY NOT LEAVE!!")
    
    def pay(self,Car):
        """ Action to make car pay for the amount of time they have been parked $1 = 1 hour
        @param Car: Car class object
        @return: amount of money paid
        """
        
        if Car.status == "Paid":
            return logger_intance.error(f"[CAR] {Car.UUID} has already paid")
        else:
            time = Car.getParkingTimeInMinutes()
            time = time * 60
            time = round(time, 2)
            
            IsOverTwoHours = time > 2
            if IsOverTwoHours:
                time = time * 2 # Multiply by 2 for over two hours as a fee
            amount = time * 1 # Converts to dollars
            amount = "$" + str(amount)
            
            Car.status = "Paid"
            logger_intance.info(f"[CAR] {Car.UUID} has paid {amount} ")
            return True
    def getCapacity(self):
        """
        Returns the total capacity of the garage.
        """
        return len(self.ParkingCarList)




