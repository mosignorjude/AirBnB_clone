#!/usr/bin/python3
import cmd
import sys
from models import storage
from models.base_model import BaseModel


""" Defines the command class of the console """


class HBNBCommand(cmd.Cmd):
    """ Represents the console """

    prompt = "(hbnb) "

    def do_quit(self, line_arg):
        """ Quits command to exit the program\n """
        return True

    def do_EOF(self, line_arg):
        """Exit command that quits the program\n """
        return True

    def emptyline(self):
        """ Do nothing when an empty line is entered\n """
        pass

    def do_create(self, line_arg):
        """ Creates a new instance of BaseModel """

        if line_arg:
            if line_arg == "BaseModel":
                new_model = BaseModel()
                new_model.save()
                print("{}".format(new_model.id))
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line_arg):
        """ Prints the string representation of an instance based on
        class name and id\n
        """
        all_objects = storage.all()
        if line_arg:
            token = line_arg.split()
            if len(token) == 1:
                print("*** instance is missing ***")
                return
            elif len(token) == 2:
                class_name = token[0]
                obj_id = token[1]
                class_key = f"{class_name}.{obj_id}"

                if class_key in all_objects.keys():
                    obj = all_objects[class_key]
                    print(obj)
                    storage.__objects = all_objects
                    storage.save()

                else:
                    print("** no instance found **")
                    return
                for obj_key in all_objects:
                    obj_token = obj_key.split('.')
                    obj_name = obj_token[0]
                    if obj_name == class_name:
                        pass
                    else:
                        print("** class doesn't exist **")
        else:
            print("** class name missing ***")

    def do_destroy(self, line_arg):
        """  Deletes an instance based on the class name and id """

        all_objects = storage.all()
        if line_arg:
            token = line_arg.split()
            if len(token) == 1:
                print("*** instance id missing ***")
                return
            elif len(token) == 2:
                class_name = token[0]
                obj_id = token[1]
                class_key = f"{class_name}.{obj_id}"

                if class_key in all_objects.keys():
                    del all_objects[class_key]
                else:
                    print("** no instance found **")
                    return
                for obj_key in all_objects:
                    obj_token = obj_key.split('.')
                    obj_name = obj_token[0]
                    if obj_name == class_name:
                        pass
                    else:
                        print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line_arg):
        """  Prints all string representation of all instances based or not on the class name """
        all_objects = storage.all()
        if line_arg:
            token = line_arg.split()
            if len(token) == 1:
                class_name = token[0]
                for obj_key, obj in all_objects.items():
                    if obj_key.startswith(class_name):
                        print(obj)
                    else:
                        print("** class doesn't exist **")
                        return
        else:
            print(all_objects)


def run_interactive_mode():
    """ Runs the console in interactive mode """
    HBNBCommand().cmdloop()


def run_non_interactive_mode():
    """ Runs the console in non interactive mode """
    commands = sys.argv[1:]
    for command in commands:
        try:
            HBNBCommand().onecmd(command)

        except Exception as e:
            print("Error executing {} : {}".format(command, e))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
