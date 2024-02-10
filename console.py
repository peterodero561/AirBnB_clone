#!/usr/bin/env python3
# console.py

""" Console module """
import cmd


class HBNBcommand(cmd.Cmd):
    """ Console class to handle the input and output """
    #    intro = "Welcome to HBNB console!\nType help or ? to list commands.\n"
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """ Perform action when reaching end of line """
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        #   print("Exiting ...")
        return True


if __name__ == "__main__":
    HBNBcommand().cmdloop()
