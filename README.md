<div>
  <img src="https://user-images.githubusercontent.com/69850751/175876062-f252cc1b-bd44-46b3-9ddb-a7692b2eede4.png"     alt="">
</div>


# AirBnB Clone - The Console Project

## Description
The AirBnB Clone - The Console Project is a command-line interface (CLI) application that replicates some of the functionalities of the popular AirBnB platform. It allows users to create, manage, and interact with objects such as users, places, and bookings. The project is developed using Python and follows an object-oriented programming (OOP) approach.

## Command Interpreter
The command interpreter is the core component of the AirBnB Clone - The Console Project. It provides a command-line interface where users can interact with the application and perform various operations. The command interpreter supports a set of commands that can be used to manipulate and manage the objects within the application. Some of the available commands include:

- `create`: Creates a new object of a specified class.
- `show`: Displays detailed information about a specific object.
- `all`: Lists all objects of a specific class or all objects in the application.
- `update`: Updates the attributes of a specific object.
- `destroy`: Deletes a specific object from the application.

## How to Start
To start the AirBnB Clone - The Console Project, follow the steps below:

1. Clone the project repository from GitHub: [https://github.com/your-username/airbnb-clone](https://github.com/your-username/airbnb-clone)
2. Ensure that you have Python 3.x installed on your system.
3. Open a terminal or command prompt.
4. Navigate to the project directory.
5. Run the following command to start the command interpreter:

```
$ python console.py
```

## How to Use
Once the command interpreter is running, you can use various commands to interact with the application. Here are some examples of how to use the command interpreter:

- To create a new user:
```
(hbnb) create User
```

- To show information about a specific place:
```
(hbnb) show Place 1234-5678-9012
```

- To list all available bookings:
```
(hbnb) all Booking
```

- To update the price of a place:
```
(hbnb) update Place 9876-5432-1098 price 100
```

- To delete a user:
```
(hbnb) destroy User 1234-5678-9012
```

## Examples
Here are some examples of commands and their expected outputs:

- Example 1: Creating a new user
```
(hbnb) create User
```
Output:
```
1234-5678-9012
```

- Example 2: Showing information about a specific place
```
(hbnb) show Place 1234-5678-9012
```
Output:
```
[Place] (1234-5678-9012) {'id': '1234-5678-9012', 'name': 'Cozy Cabin', 'price': 80, 'city': 'New York'}
```

- Example 3: Listing all available bookings
```
(hbnb) all Booking
```
Output:
```
[Booking] (1234-5678-9012) {'id': '1234-5678-9012', 'user_id': 'abcd-efgh-ijkl', 'place_id': '9876-5432-1098', 'start_date': '2023-01-01', 'end_date': '2023-01-05'}
[Booking] (9876-5432-1098) {'id': '9876-5432-1098', 'user_id': 'mnop-qrst-uvwx', 'place_id': '1234-5678-9012', 'start_date': '2023-02-01', 'end_date': '2023-02-10'}
```

- Example 4: Updating the price of a place
```
(hbnb) update Place 9876-5432-1098 price 100
```
Output:
```
(hbnb)
```

- Example 5: Deleting a user
```
(hbnb) destroy User 1234-5678-9012
```
Output:
```
(hbnb)
```

Feel free to explore more commands and functionalities of the AirBnB Clone - The Console Project. Enjoy!