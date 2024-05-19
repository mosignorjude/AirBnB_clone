#!/usr/bin/python3
"""
This file defines the console class
which will serve as basis of the entire project
"""
import cmd
import sys
import re
from models.engine.file_storage import FileStorage
from utilities_for_console import *
from models import storage

# Global variable of existing classes.
classes = storage.models
# Global variable of regex pattern
pattern = r"^[Aa-Zz]\w*\.\((\w|-)*\)"


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

    def default(self, arg):
        """ overides the default method to handle unrecognised commands """
        if arg:
            args = arg.split('.')
            if '.' in arg and args[0] in classes and args[1][-1:] == ")":
                # if args[0] in classes and re.match(pattern, arg[1]):
                return self.handle_unregistered_command(arg)

        return cmd.Cmd.default(self, arg)

    def handle_unregistered_command(self, arg):
        """ handles other methods """
        if arg:
            args = arg.split('.')
            obj_class = args[0]
            method = args[1]
            if method == "all()":
                self.all_instances(arg)
            elif method == "count()":
                self.count_instances(arg)
            elif method.startswith("show(") or method.startswith("destroy("):
                self.show_or_destroy_instances(arg)

    def all_instances(self, arg):
        """
         retrieve all instances of a class by using: <class name>.all()
        """
        if arg:
            token = arg.split('.')
            obj_class = token[0]
            method = token[1]
            if obj_class in classes:
                if method == "all()":
                    self.do_all(f"{obj_class}")

                else:
                    print("** Invalid Method **")
                    return
            else:
                print("** class doesn't exist **")
                return

    def count_instances(self, arg):
        """ retrieve the number of instances of a class: <class name>.count() """
        if arg:
            count = 0
            args = arg.split('.')
            obj_class = args[0]
            method = args[1]
            if obj_class in classes and method == "count()":
                all_object = storage.all()
                for key, obj in all_object.items():
                    if key.startswith(obj_class):
                        count += 1
                print(count)

    def show_or_destroy_instances(self, arg):
        """ retrieve an instance based on its ID: <class name>.show(<id>) """
        if arg:
            args = arg.split('.')
            obj_class = args[0]
            method = args[1]
            if obj_class in classes:
                obj_id = extract_attr(method)
                if method.startswith("show(") and method[-1:] == ")":
                    self.do_show(f"{obj_class} {obj_id}")
                elif method.startswith("destroy(") and method[-1:] == ")":
                    self.do_destroy(f"{obj_class} {obj_id}")


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
