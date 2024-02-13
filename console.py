#!/usr/bin/env python3
# console.py

""" Console module """
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBcommand(cmd.Cmd):
    """ Console class to handle the input and output """
    #    intro = "Welcome to HBNB console!\nType help or ? to list commands.\n"
    prompt = "(hbnb) "
    class_list = [
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
            ]

    def check_class(self, line):
        """
        checks if class exists
        """
        try:
            globals()[line]
            return True
        except (NameError, KeyError):
            print("** class doesn't exist **")
            return False

    def do_EOF(self, line):
        """ Perform action when reaching end of line """
        return True

    def emptyline(self):
        '''prints nothing incase of an enmpty line and enter'''
        pass

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and
        prints the id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBcommand.class_list:
            print("** class name missing **")
            return
        try:
            if args[0] == "BaseModel":
                new = BaseModel()
                new.save()
            elif args[0] == "User":
                new = User()
                new.save()
            elif args[0] == "Place":
                new = Place()
                new.save()
            elif args[0] == "State":
                new = State()
                new.save()
            elif args[0] == "City":
                new = City()
                new.save()
            elif args[0] == "Amenity":
                new = Amenity()
                new.save()
            elif args[0] == "Review":
                new = Review()
                new.save()
            else:
                print("** class doesn't exist **")
                return
            print(new.id)
        except NameError:
            print("** class doesn't exist** ")

    def do_show(self, arg):
        """
        Print string representation of instance based on class name
        and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBcommand.class_list:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        try:
            if class_name == "BaseModel":
                obj = BaseModel.load(class_name, instance_id)
            elif class_name == "User":
                obj = User.load(class_name, instance_id)
            elif class_name == "Place":
                obj = Place.load(class_name, instance_id)
            elif class_name == "City":
                obj = City.load(class_name, instance_id)
            elif class_name == "State":
                obj = State.load(class_name, instance_id)
            elif class_name == "Amenity":
                obj = Amenity.load(class_name, instance_id)
            elif class_name == "Review":
                obj = Review.load(class_name, instance_id)
            else:
                print("** class doesn't exist **")
            print(obj)
        except FileNotFoundError:
            print("** no instance found ** ")

    def do_destroy(self, arg):
        ''' Deletes an instance based on the class name
            and id (save the change into the JSON file).
        '''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBcommand.class_list:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        try:
            # load data from JSON file
            with open("file.json", "r") as f:
                data = json.load(f)

            key = f"{class_name}.{instance_id}"
            if key not in data:
                print("** no instance found **")
                return

            # delete instance
            del data[key]

            # save updated data to json file
            with open("file.json", "w") as f:
                json.dump(data, f)
        except FileNotFoundError:
            print("** no instance found **")

    def do_all(self, arg):
        ''' Prints all string representation of all instances
            based or not on the class name.
        '''
        try:
            args = arg.split()
            if not args:
                class_name = None
            else:
                class_name = args[0]
                if class_name not in HBNBcommand.class_list:
                    print("** class doesn't exist **")
                    return

            # load data from json file
            with open("file.json", "r") as f:
                data = json.load(f)

            if class_name:
                filtered_data = {
                        key: value for key,
                        value in data.items() if key.startswith(
                            class_name + ".")
                        }
            else:
                filtered_data = data

            if not filtered_data:
                print("** no instances found **")
                return

            # print string representaton of each instance
            for obj_data in filtered_data.values():
                obj = BaseModel(**obj_data)
                print(obj)
        except FileNotFoundError:
            print("** no instances found **")

    def do_update(self, arg):
        '''Updates an instance based on the class name and
            id by adding or updating attribute
            (save the change into the JSON file).
        '''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBcommand.class_list:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        try:
            with open("file.json", "r") as f:
                data = json.load(f)
            key = f"{class_name}.{instance_id}"
            if key not in data:
                print("** no instance found **")
                return
            obj_data = data[key]
            obj = BaseModel(**obj_data)

            # check if the attribut name is valid and not reserved
            if attribute_name in ["id", "created_at", "updated_at"]:
                print("** cannot update reserved atrribute **")
                return

            setattr(obj, attribute_name, attribute_value)
            data[key] = obj.to_dict()
            with open("file.json", "w") as f:
                json.dump(data, f)

        except FileNotFoundError:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBcommand().cmdloop()
