# Logger Module Documentation

## Overview
The `Logger` module provides a class for logging messages with various severity levels. It is designed to simplify the process of tracking application events and debugging.

## Class: `Logger`
---
### Description
The `Logger` class is responsible for handling log messages and writing them to a specified output, such as a file or the console.

### Methods


---




#### `info(message: str)`
Logs an informational message.

- **Parameters**:
    - `message` (str): The informational message to log.

#### `warning(message: str)`
Logs a warning message.

- **Parameters**:
    - `message` (str): The warning message to log.

#### `error(message: str)`
Logs an error message.

- **Parameters**:
    - `message` (str): The error message to log.
---
### Example Usage

```python
from modules.Logger import Logger

# Initialize the logger
logger = Logger()

# Log messages
logger.info("Application started")
logger.warning("Low disk space")
logger.error("Failed to connect to database")
```
---
### Notes
- Ensure the log file path is writable.
- Log levels can be customized as needed.




# Car Module Documentation

## Overview
The `Car` module provides a class for representing a car with various attributes and methods to manipulate its state. It designed to simplify the process of managing car-related data and operations.

## Class: `Car`

### Description
The `Car` class is responsible for handling car attributes such as, Ctype, parkingSlot, licensePlate, timeInParking.
and provides methods to manipulate and retrieve this data easily.

### Methods


---
### Getters
#### `get_license_plate() -> str`
Returns the license plate of the car.
- **Returns**: (str) The license plate of the car.

#### `get_time_in_parking() -> str`
Returns the time the car has been in the parking lot.
- **Returns**: (str) The time the car has been in the parking lot.

#### `get_parking_slot() -> str`
Returns the parking slot of the car.
- **Default**: None
- **Parameters**: None
- **Returns**: (str) The parking slot of the car.

#### `get_Car_Type() -> str`
Returns the type of the car.
- **Parameters**: None
- **Returns**: (str) The type of the car.

---
### Setters
#### `set_license_plate(license_plate: str)`

Sets the license plate of the car.
- **Parameters**:
    - `license_plate` (str): The license plate to set.

- **Returns**: None










# Floor Module Documentation
---
## Overview
The `Floor` module provides a class for representing a parking floor with various attributes and methods to manipulate its state. It designed to simplify the process of managing parking floor-related data and operations. it will also store the cars that are parked in the parking slots.

### Methods
---
### Getters
#### `get_floor_number() -> int`
Returns the floor number of the parking floor.
- **Parameters**: None

- **Returns**: (int) The floor number of the parking floor.

#### `get_Parking_Slots()` -> list[str]
Returns the list of parking slots on the floor.
- **Parameters**: None

- **Returns**: (list[[Compact:Object], [Standerd:Object],[Electric:Object], [Oversized:Object] ]) The list of parking slots on the floor.

#### `get_parked_cars()` -> list[Car]

Returns the list of parked cars on the floor.
- **Parameters**: None
- **Returns**: (list[[Compact:Object], [Standerd:Object],[Electric:Object], [Oversized:Object] ]) The list of parked cars on the floor.


#### `get_available_slots()` -> list[str]

Returns the list of available parking slots on the floor.
- **Parameters**: None

- **Returns**: (list[[Compact:Object], [Standerd:Object],[Electric:Object], [Oversized:Object]]) The list of available parking slots on the floor.


---
### Setters
#### `park(Car:Class ,parking_slot: str)`
Parks the car in the specified parking slot.
- **Parameters**:
    - `Car` (Class): The car to park.
    - `parking_slot` (str): The parking slot to park the car in.
- **Returns**: logger.info("Car parked in slot: " + parking_slot)


#### `unpark(Car:Class)`
unparks the car from its current parking slot.
- **Parameters**:
    - `Car` (Class): The car to unpark.
- **Returns**: logger.info("Car unparked from slot: " + self.parkingSlot)
### Parking Slot Grid

Below is a grid of what each floor looks like in a code sense to refence each parking slot. for more then one floor, the grid will be the same but the parking slots will be different instead in a formate of "2A1.

| 1A1  | 1A2  | 1A3  | 1A4  | 1A5  | 1A6  | 1A7  | 1A8  | 1A9  | 1A10 |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 1B1  | 1B2  | 1B3  | 1B4  | 1B5  | 1B6  | 1B7  | 1B8  | 1B9  | 1B10 |
| 1C1  | 1C2  | 1C3  | 1C4  | 1C5  | 1C6  | 1C7  | 1C8  | 1C9  | 1C10 |
| 1D1  | 1D2  | 1D3  | 1D4  | 1D5  | 1D6  | 1D7  | 1D8  | 1D9  | 1D10 |
| 1E1  | 1E2  | 1E3  | 1E4  | 1E5  | 1E6  | 1E7  | 1E8  | 1E9  | 1E10 |




