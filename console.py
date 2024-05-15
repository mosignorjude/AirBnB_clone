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
        for key in all_objects:
            obj_token = key.split('.')
            obj_name = obj_token[0]
            if line_arg:
                token = line_arg.split()
                print(len(token))
                if len(token) == 2:
                    if not token[0]:
                        print("** class name missing **")
                    if not token[1]:
                        print("** instance id missing **")
                    class_name = token[1]
                    class_id = token[2]
                    class_key = f"{class_name}.{class_id}"
                    if obj_name == class_name:
                        if class_key == key:
                            print(obj_name.__str__())
                        else:
                            print("** no instance found **")
                    else:
                        print("** class doesn't exist **")
            else:
                print("command out of range")


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
