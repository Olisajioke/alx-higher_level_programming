#!/usr/bin/python3
<<<<<<< HEAD
"""
models/base.py: Contains the Base class for managing id attributes.
"""
import json
import csv
import turtle


class Base:
    """The Base class for managing unique identifiers"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of the Base class.
        Args:
            id (int, optional): The unique identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries, sort_keys=True)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of dictionaries from a JSON string representation.
        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: A list of dictionaries represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): A list of instances that inherit from Base.

        Raises:
            TypeError: If list_objs is not a list of
            instances that inherit from Base.
        """
        if list_objs is None:
            list_objs = []
        if not all(isinstance(obj, cls) for obj in list_objs):
            raise TypeError("list_objs must be a list of instances" +
                            "that inherit from Base")

        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as file:
            dictionary_list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(dictionary_list)
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set based on the dictionary
        Args:
            **dictionary: A dictionary containing attribute values.

        Returns:
            cls: An instance of class with attributes set from dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class for create method")

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a JSON file.
        Returns:
            list: A list of instances based on the
            current class (cls) using this method.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r") as file:
                json_string = file.read()
                dictionary_list = cls.from_json_string(json_string)
                instances_list = [cls.create(**data)
                                  for data in dictionary_list]
                return instances_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file.
        Args:
            list_objs (list): A list of instances that inherit from Base.

        Raises:
            TypeError: If list_objs is not list of instances inherit from Base
        """
        if list_objs is None:
            list_objs = []
        if not all(isinstance(obj, cls) for obj in list_objs):
            raise TypeError("list_objs must be a list of instances" +
                            "that inherit from Base")

        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                else:
                    raise ValueError("Unsupported class for" +
                                     "CSV serialization")
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances loaded from a CSV file.
        Returns:
            list: list of instances based on current class using this method.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", newline="") as file:
                reader = csv.reader(file)
                instances_list = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        data = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4]),
                        }
                    elif cls.__name__ == "Square":
                        data = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3]),
                        }
                    else:
                        raise ValueError("Unsupported class for" +
                                         "CSV deserialization")
                    instance = cls.create(**data)
                    instances_list.append(instance)
                return instances_list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.
        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.
        """
        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Drawing Rectangles and Squares")

        drawer = turtle.Turtle()
        drawer.speed(1)

        def draw_rectangle(rect):
            drawer.penup()
            drawer.goto(rect.x, rect.y)
            drawer.pendown()
            for _ in range(2):
                drawer.forward(rect.width)
                drawer.left(90)
                drawer.forward(rect.height)
                drawer.left(90)

        def draw_square(square):
            drawer.penup()
            drawer.goto(square.x, square.y)
            drawer.pendown()
            for _ in range(4):
                drawer.forward(square.size)
                drawer.left(90)

        for rect in list_rectangles:
            draw_rectangle(rect)

        for square in list_squares:
            draw_square(square)

        screen.exitonclick()
>>>>>>> 59777f69d470eabf01922309604f60c3e6bb2a1b
