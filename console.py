#!/usr/bin/python3
"""
    Console Module to manage AirBNB clone project to Holberton School
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """
        Command line interpreter to AIRBNB clone
    """
    # default prompt
    prompt = "(hbnb)"

    # PRIVATE CLASS ATTRIBUTES
    __classes_list = ["BaseModel", "User", "City", "State", "Place",
                      "Review", "Amenity"]
    _QUIT_ = 1
    _SUCCESS_ = 0

    def __instance_verification(self, input):
        """
            Verify if the instance exists
        """

        # if the class name is missing,
        # print ** class name missing ** (ex: $ show)
        if input == '':
            print("** class name missing **")
            return self._QUIT_, None, None

        # Tokenized input
        args = input.split(" ")

        # If the class name doesn’t exist, print ** class doesn't exist **
        if args[0] not in self.__classes_list:
            print("** class doesn't exist **")
            return self._QUIT_, None, None

        # If the id is missing,
        # print ** instance id missing ** (ex: $ show BaseModel)
        if len(args) == 1:
            print("** instance id missing **")
            return self._QUIT_, None, None

        key = str(args[0]) + '.' + args[1]
        # If the key is valid Return key and args
        if key in storage.objects:
            return self._SUCCESS_, key, args

        # If the instance of the class name doesn’t exist
        # for the id, print ** no instance found **
        else:
            print("** no instance found **")
            return self._QUIT_, None, None

    def __attributes_verification(self, args_list):
        """
        verify if the attributes are valid
        """

        # If the attribute is missing,
        # print ** attribute name missing **
        if len(args_list) == 2:
            print("** attribute name missing **")
            return self._QUIT_

        # If the value is missing,
        # print ** value missing **
        if len(args_list) == 3:
            print("** value missing **")
            return self._QUIT_

        return self._SUCCESS_

    def do_EOF(self, args):
        """ EOF command - exit the program """
        return quit()

    def do_quit(self, args):
        """ Quit command - exit the program """
        return exit

    def emptyline(self):
        """
            Called when an empty line
            is entered in response to the prompt.
        """
        pass

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id

            Attributes
            name_class - the name of the class to create
        """
        if not arg:
            print("** class name missing **")
            return None
        else:
            args = arg.split()
            if args[0] not in self.__classes_list:
                print("** class doesn't exist **")

        if args[0] in self.__classes_list:
            name_class = args[0]
            args.pop(0)
            attributes = {}
            for _arg in args:
                attribute = _arg.split('=')
                if len(attribute) == 2:
                    key = attribute[0]
                    value = attribute[1]
                    if value.startswith('"'):
                        value = value[1:-1]
                    value = value.replace('_', ' ')
                    attributes[key] = value
                else:
                    pass
            new_model = eval(name_class)(**attributes)
            new_model.save()
            print(new_model.id)
            storage.reload()

    def do_show(self, input):
        """
            Prints the string representation of an
            instance based on the class name and id
        """

        verification, key, args = self.__instance_verification(input)

        if verification == self._QUIT_:
            return

        instance_dict = storage.objects.get(key)
        _object = eval(instance_dict.get('__class__'))(**instance_dict)
        print(_object.__str__())

    def do_destroy(self, input):
        """
            Deletes an instance based on the class
            name and id and save the change into the JSON file.
        """
        verification, key, args = self.__instance_verification(input)

        if verification == self._QUIT_:
            return

        storage.objects.pop(key)
        storage.save()

    def do_all(self, input):
        """
             Prints all string representation of
             all instances based or not on the class name.
        """

        instances_list = list()

        def print_instances(list):
            instance_dict = storage.all()
            for key in list:
                _object = storage.objects.get(key)
                # _object = eval(instance_dict('__class__'))(**instance_dict)
                instances_list.append(_object.__str__())
            print(instances_list)

        if input == '':
            list_all_keys = list(storage.objects.keys())
            print_instances(list_all_keys)

        else:
            args = input.split(" ")
            if args[0] in self.__classes_list:
                list_all_keys = list(storage.objects.keys())
                list_selected_keys = list()
                for key in list_all_keys:
                    if (str(args[0]) in key):
                        list_selected_keys.append(key)
                print_instances(list_selected_keys)
            else:
                print("** class doesn't exist **")

    def do_update(self, input):

        """
            Deletes an instance based on the class
            name and id and save the change into the JSON file.
        """

        verification, key, args = self.__instance_verification(input)

        if verification == self._QUIT_:
            return

        verification = self.__attributes_verification(args)

        if verification == self._QUIT_:
            return

        value = (args[3])[1:-1]  # erase double quotes
        object_attributes = storage.objects.get(key)
        object_attributes[args[2]] = value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
