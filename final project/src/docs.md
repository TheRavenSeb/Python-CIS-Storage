### Logger Module (`Logger.py`)

The `Logger` module is responsible for logging messages to a file with a timestamp in the filename. It uses Python's `logging` module to handle logging functionality.

#### Class: `logger`

**Attributes:**
- `log_file_path`: Path to the log file with a timestamp.

**Methods:**
- `info(message: str)`: Logs an informational message.
- `warning(message: str)`: Logs a warning message.
- `error(message: str)`: Logs an error message.
- `critical(message: str)`: Logs a critical message.
- `debug(message: str)`: Logs a debug message.

**Example Usage:**
```python
from modules.Logger import logger

logger_instance = logger()
logger_instance.info("Application started")
logger_instance.warning("Low disk space")
logger_instance.error("Failed to connect to database")
```

---

### Car Module (`car.py`)

The `Car` module defines a `Car` class to represent individual cars in the parking system.

#### Class: `Car`

**Attributes:**
- `carType`: Type of the car (e.g., SUV, sedan).
- `license`: License plate of the car.
- `UUID`: Unique identifier for the car.
- `pSpot`: Parking spot assigned to the car.
- `enterTime`: Timestamp when the car entered the parking.
- `exitTime`: Timestamp when the car exited the parking.
- `status`: Current status of the car (e.g., "Parked", "Exited").

**Methods:**
- `getEnterTime()`: Returns the enter time of the car.
- `getExitTime()`: Returns the exit time of the car.
- `getStatus()`: Returns the status of the car.
- `getParkingSpot()`: Returns the parking spot of the car.
- `getLicense()`: Returns the license plate of the car.
- `getCarType()`: Returns the type of the car.
- `getUUID()`: Returns the unique identifier of the car.
- `setParkingSpot(spot: str)`: Sets the parking spot of the car.
- `getParkingTime()`: Returns the total parking time of the car in hours.
- `getParkingTimeInSeconds()`: Returns the total parking time of the car in seconds.
- `getParkingTimeInMinutes()`: Returns the total parking time of the car in minutes.
- `getParkingTimeInHours()`: Returns the total parking time of the car in hours.

---

### Garage Module (`garage.py`)

The `Garage` module defines a `Garage` class to manage the parking structure.

#### Class: `Garage`

**Attributes:**
- `ParkingSpotSet`: Set of available parking spots.
- `ParkingCarList`: List of parked cars.
- `lisencePlateSet`: Set of license plates for parked cars.

**Methods:**
- `GetCars()`: Returns the list of parked cars.
- `GetSpots()`: Returns the set of available parking spots.
- `park(Car, spot: str)`: Parks a car in a specific spot.
- `unpark(Car)`: Removes a car from the parking spot.
- `pay(Car)`: Processes payment for the parked car based on the duration.
- `getCapacity()`: Returns the total capacity of the garage.

```python

#Example code
from modules.garage.py import garage
from modules.car.py import car
floor1 = new garage()
car1 = new car()


floor1.park(car)

```


