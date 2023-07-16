#!/usr/bin/env python3

""" This module contains entry point for command
interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models import storage

class_names = ['BaseModel', 'User', 'Amenity', 'City',
               'Place', 'State', 'Review']


class HBNBCommand(cmd.Cmd):
    """ The Cmd class - gives access to its atttributes;
    useful to create, design commmand line interpreter
    """
    prompt = "(hbnb) "

    def do_create(self, line):
        """ Creates a new instance of BaseMode
        """
        content = line.split()

        if not line:
            print("** class name is missing **")
        elif content[0] not in class_names:
            print("** class doesn't exist **")
        else:
            model = eval(content[0])()
            storage.new(model)
            storage.save()
            print("{}".format(model.id))

    def do_show(self, line):
        """ Prints the string representation of an instance
        """
        content = line.split()
        found = False

        if not line:
            print("** class name missing **")
        elif content[0] not in class_names:
            print("** class doesn't exist **")
        elif len(content) == 1:
            print("** instance id missing **")
        else:
            instance_id = content[1]
            for key, val in storage.all().items():
                if key.endswith(".{}".format(instance_id)):
                    print(val)
                    found = True
                    break
            if not found:
                print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id
        """
        content = line.split()
        found = False

        if not line:
            print("** class name missing **")
        elif content[0] not in class_names:
            print("** class doesn't exist **")
        elif len(content) == 1:
            print("** instance id missing **")
        else:
            instance_id = content[1]
            all_items = storage.all()
            for key, val in all_items.items():
                if key.endswith(".{}".format(instance_id)):
                    found = True
                    del all_items[key]
                    storage.save()
                    break

            if not found:
                print("** no instance found **")

    def do_all(self, line):
        """ Prints all string representation of all instances
        """
        content = line.split()
        if not line:
            print([str(item) for item in storage.all().values()])
        elif content[0] in class_names:
            print([
                str(item[1]) for item in storage.items()
                if item[0].startswith("{}.".format(content[1]))])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ Updates an instance based on  the class name and id
        """
        content = line.split()
        if not line:
            print("** class name missiong **")
        elif content[0] not in class_names:
            print("** class doesn't exist **")
        elif len(content) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(content[0], content[1]) not in storage.all():
            print("** no instanc found **")
        elif len(content) == 2:
            print("**attribute name missing **")
        elif len(content) == 3:
            print("** value missing **")
        else:
            key = content[2]
            value = content[3]  # default type is string
            all_storage = storage.all()

            for attr_type in (int, float):
                try:
                    value = attr_type(value)
                    break
                except (ValueError):
                    pass

            all_storage["{}.{}".format(
                content[0], content[1])].__setattr__(key, value)
            storage.save()

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

    def postloop(self):
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
