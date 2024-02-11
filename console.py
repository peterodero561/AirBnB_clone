#!/usr/bin/env python3
# console.py

""" Console module """
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBcommand(cmd.Cmd, BaseModel):
    """ Console class to handle the input and output """
    #    intro = "Welcome to HBNB console!\nType help or ? to list commands.\n"
    prompt = "(hbnb)"

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

    def do_quit(self, line):
        """ Quit command to exit the program """
        #   print("Exiting ...")
        return True

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and 
        prints the id
        """
        if line == "":
            print("** class name missing **")

        if self.check_class(line):
            new_instance = globals()[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Print string representation of instance based on class name
        and id
        """
        words = line.split()
        if len(words) < 1:
            print("** class name missing **")
            return
        class_name = words[0]

        if self.check_class(class_name):
            if len(words) < 2:
                print("** instance id missing **")
                return
            instance_id = words[1]

            key = "{}.{}".format(class_name, instance_id)
            objects_dict = storage.all()

            if key in objects_dict:
                instance = objects_dict[key]
                print(instance)
            else:
                print("** no instance found **")

        else:
            print("** class doesn't exist **")
            return

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        words = line.split()
        if len(words) < 1:
            print("** class name missing **")
            return
        class_name = words[0]

        if self.check_class(class_name):
            if len(words) < 2:
                print("** instance id missing **")
                return
            instance_id = words[1]

            key = "{}.{}".format(class_name, instance_id)
            objects_dict = storage.all()

            if key in objects_dict:
                del objects_dict[key]
                storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBcommand().cmdloop()
