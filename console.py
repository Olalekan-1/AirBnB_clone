#!/usr/bin/env python3

""" This module contains entry point for command
interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ The Cmd class - gives access to its atttributes;
    useful to create, design commmand line interpreter
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """ overide the default emptyline
        implementation
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program """
        exit()

    def do_EOF(self, line):
        """EOF command exit the interpreter """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
