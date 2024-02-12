#!/usr/bin/env python3
# console.py

""" Console module """
import cmd
from models.base_model import BaseModel


class HBNBcommand(cmd.Cmd, BaseModel):
    """ Console class to handle the input and output """
    #    intro = "Welcome to HBNB console!\nType help or ? to list commands.\n"
    prompt = "(hbnb) "

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

if __name__ == "__main__":
    HBNBcommand().cmdloop()
