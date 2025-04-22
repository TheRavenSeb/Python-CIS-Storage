
from modules.garage import Garage
from modules.car import Car 
from modules.Logger import logger 
import random
import time

logger_instance = logger()
garage = Garage()
car_types = ["suv", "sedan", "truck", "motorcycle"]
car_uuids = [f"UUID-{i}" for i in range(1, 101)]
car_licenses = [f"LICENSE-{i}" for i in range(1, 101)]

def generate_random_cars(num_cars):
    """
    Generate a list of random cars.
    :param num_cars: Number of cars to generate.
    :return: List of Car objects.
    """
    num_cars = int(num_cars)  # Convert to integer
    cars = []
    for _ in range(num_cars):
        car_type = random.choice(car_types)
        uuid = random.choice(car_uuids)
        license_plate = random.choice(car_licenses)
        car = Car(car_type, license_plate, uuid)
        cars.append(car)
    return cars

def test_parking_system():
    
    """
    Test the parking system by generating random cars and parking them in the garage.
    """
    a = input("Would you like to begin the simulation? Please type Yes or No. ")

    if a == "Yes" or a == "yes" or a == "YES" or a == "y" or a == "Y":
        b = input("How many cars would you like to generate for this test? ")
        num_cars = b  # Number of cars to generate
        cars = generate_random_cars(num_cars)
    else:
        logger_instance.info("Simulation aborted by user.")
        return
       
        
    for car in cars:
        spot = random.choice(list(garage.GetSpots()))
        if spot is None:
            logger_instance.error(f"No available parking spots for {car}")
            break
        garage.park(car, spot)
        logger_instance.info(f"Parked {car} in spot {spot}")
    
    for car in cars:
        time.sleep(1.5)
        garage.unpark(car)
        logger_instance.info(f"Unparked {car}")
        
        
if __name__ == "__main__":
    test_parking_system()
    logger_instance.info("All tests completed.")
    
    # Close the logger
    
    