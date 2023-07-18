#!/usr/bin/env python3

""" This module contains entry point for command
interpreter
"""
import cmd
import re
import json
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
options = ['all', 'count', 'show', 'destroy', 'update']


class HBNBCommand(cmd.Cmd):
    """ The Cmd class - gives access to its atttributes;
    useful to create, design commmand line interpreter
    """
    prompt = "(hbnb) "

    def _name_option(
            self, name="", option="", model_id=None,
            key=None, value=None, attrib_dict=None
            ):
        """Helper function calling methods on an Object

        example (cmd) User.all()
        """
        output = []
        all_items = storage.all()

        if option == 'all':
            output = [
                str(item[1]) for item
                in all_items.items() if name in item[0]]
        elif option == 'count':
            output = sum(
                    1 for item in all_items.items()
                    if name in item[0])
        elif option == 'show':
            if model_id is not None:
                output = [
                        str(item[1]) for item in
                        all_items.items() if item[0] ==
                        "{}.{}".format(name, model_id.replace('"', ""))
                        ]
                if output:
                    output = output[0]
                else:
                    output = "** no instance found **"
            else:
                output = "** instance id missing **"

        elif option == 'destroy':
            output = "** no instance found **"
            if model_id is not None:
                search_key = "{}.{}".format(name, model_id.replace('"', ""))
                if search_key in all_items:
                    del all_items[search_key]
                    storage.save()
                    return
                output = "** no instance found **"
            else:
                output = "** instance id missing **"

        elif option == 'update':
            if attrib_dict is not None:
                search_key = "{}.{}".format(name, model_id.replace('"', ""))
                if search_key in all_items:
                    for key, value in attrib_dict.items():
                        for my_type in (int, float):
                            try:
                                value = my_type(value)
                                break
                            except Exception:
                                pass
                        all_items[search_key].__setattr__(key, value)
                    storage.save()
                    return
                else:
                    print("** no instance found **")
                    return

            if key is not None and value is not None and model_id is not None:
                key = key.replace('"', "")
                value = value.replace('"', "")
                model_id = model_id.replace('"', "")
                search_key = "{}.{}".format(name, model_id.replace('"', ""))
                if search_key in all_items:
                    for my_type in (int, float):
                        try:
                            value = my_type(value)
                            break
                        except Exception:
                            pass

                    all_items[search_key].__setattr__(key, value)
                    storage.save()
                    return
                else:
                    output = "** no instance found **"
            elif model_id is None:
                output = "** instance id missing **"
            elif key is None:
                output = "** attribute name missing **"
            elif value is None:
                output = "** value missing **"

        print(output)

    def default(self, line):
        pattern = (
                r"(?P<name>[A-Za-z]+)." +
                r"(?P<option>[a-z]+)\((?P<id>\".+?\")?" +
                r"\,?\s?(?P<key>\".+?\")?\,?\s?(?P<value>\".+?\"|\d+?)?\)"
                )
        update_dict_pattern = (
                r"(?P<name>[A-Za-z]+)." +
                r"(?P<option>[a-z]+)\((?P<id>\".+?\")?" +
                r"\,\s?(?P<attrib>\{.*?\})\)"
                )
        matched = re.match(update_dict_pattern, line)
        if matched:
            matched = matched.groupdict()
            name = matched['name']
            option = matched['option']
            attrib_dict = matched['attrib']
            model_id = matched['id']
            try:
                attrib_dict = json.loads(attrib_dict.replace("'", "\""))
                return self._name_option(
                        name, option, model_id,
                        attrib_dict=attrib_dict)
            except Exception as e:
                print("*** Unknown syntax: {}".format(line))
                return

        matched = re.match(pattern, line)
        matched = None if not matched else matched.groupdict()
        name = None if not matched else matched['name']
        name = None if name not in class_names else name
        option = None if not matched else matched['option']
        option = None if option not in options else option
        model_id = None
        key = None
        value = None

        if matched is not None:
            try:
                model_id = matched['id']
            except Exception:
                pass

            try:
                key = matched['key']
            except Exception:
                pass

            try:
                value = matched['value']
            except Exception:
                pass

        if name is not None and option is not None:
            return self._name_option(name, option, model_id, key, value)
        else:
            print("*** Unknown syntax: {}".format(line))

    def do_create(self, line):
        """ Creates a new instance of BaseMode
        """

        if not line:
            print("** class name missing **")
        elif line not in class_names:
            print("** class doesn't exist **")
        else:
            model = eval(line)()
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
        if not line:
            print([str(item) for item in storage.all().values()])
        elif line in class_names:
            print([
                str(item[1]) for item in storage.all().items()
                if item[0].startswith("{}.".format(line))])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ Updates an instance based on  the class name and id
        """
        content = line.split()
        if not line:
            print("** class name missing **")
        elif content[0] not in class_names:
            print("** class doesn't exist **")
        elif len(content) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(content[0], content[1]) not in storage.all():
            print("** no instance found **")
        elif len(content) == 2:
            print("** attribute name missing **")
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
