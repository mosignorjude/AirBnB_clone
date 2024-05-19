#!/usr/bin/python3
"""
This file defines the console class
which will serve as basis of the entire project
"""
import cmd
import sys
from models.engine.file_storage import FileStorage
from utilities_for_console import *
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    The console - A simple command interpreter that manages objects
    for the Airbnb project.
    All in interaction with the system are done via this class.
    """

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
    # -------------------------------------------------------------------------

    def do_create(self, line_arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id .
        Usage:
            $ create BaseModel
        """
        if line_arg:
            if len(line_arg.split()) >= 1:
                class_name = line_arg
                new_model = create_object(class_name)
                if new_model:
                    new_model.save()
                    print("{}".format(new_model.id))
                else:
                    print("** class doesn't exist **")
                    return
            else:
                return
        else:
            print("** class name missing **")

    # -------------------------------------------------------------------------

    def do_show(self, line_arg):
        """
        Prints the string representation of an instance based on
        class name and id.
        Usage:
             $ show BaseModel 1234-1234-1234
        """
        if not line_arg:
            print("** class name missing ***")
            return

        all_objects = storage.all()
        args = line_arg.split()
        if len(args) < 2:
            class_name = args[0]
            if class_name:
                if check_class_name(class_name, all_objects) == False:
                    print("** class doesn't exist **")
                    return
                else:
                    print("*** instance id missing ***")
        else:
            class_name = args[0]
            obj_id = args[1]
            class_key = f"{class_name}.{obj_id}"

            if class_key in all_objects:
                print(all_objects[class_key])
            else:
                print("** no instance found **")
                return

    # -------------------------------------------------------------------------

    def do_destroy(self, line_arg):
        """
        Deletes an instance based on the class name and id
        Usage:
            $ destroy BaseModel 1234-1234-1234
        """

        if not line_arg:
            print("** class name missing **")
            return
        all_objects = storage.all()
        args = line_arg.split()
        if len(args) < 2:
            if check_class_name(args[0], all_objects) == False:
                print("** class doesn't exist **")
                return
            else:
                print("*** instance id missing ***")
                return
        elif len(args) >= 2:
            class_name = args[0]
            obj_id = args[1]
            class_key = f"{class_name}.{obj_id}"

            if class_key in all_objects.keys():
                del all_objects[class_key]
                FileStorage.__objects = all_objects
                storage.save()
            else:
                print("** no instance found **")
                return

    # -------------------------------------------------------------------------

    def do_all(self, line_arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        Usage:
            $ all BaseModel
            or
            $ all
        """
        all_objects = storage.all()
        if line_arg:
            args = line_arg.split()
            if len(args) >= 1:
                class_name = args[0]
                if check_class_name(class_name, all_objects) == False:
                    print("** class doesn't exist **")
                    return
                for obj_key, obj in all_objects.items():
                    if obj_key.startswith(class_name):
                        print(obj)

        else:
            for key in all_objects:
                print(all_objects[key])

    # -------------------------------------------------------------------------

    def do_update(self, line_arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        Usage:
            $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        if not line_arg:
            print("** class name missing ***")
            return
        all_objects = storage.all()
        args = line_arg.split()
        if len(args) < 2:
            if check_class_name(args[0], all_objects) == False:
                print("** class doesn't exist **")
                return
            else:
                print("** instance id missing **")
                return
        elif len(args) < 3:
            if check_object(args, all_objects) == True:
                print("** attribute name missing **")
                return
            else:
                print("** no instance found **")
                return
        elif len(args) < 4:
            print("** value missing **")
            return
        elif len(args) >= 4:
            if update_obj_attr(args, all_objects, storage) == 1:
                print("** no instance found **")

    # -------------------------------------------------------------------------


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

# -----------------------------------------------------------------------------
