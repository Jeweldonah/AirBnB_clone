#!/usr/bin/python3
import cmd
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, args):
        """Create a new instance of BaseModel,
        save it to the JSON file, and print the id"""
        if not args:
            print("** class name missing **")
            return

        try:
            new_instance = models.classes[args]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Print the string representation of an instance
        based on the class name and id"""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return

        print(models.storage.all()[key])

    def do_destroy(self, args):
        """Delete an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return

        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, args):
        """Print string representations of all instances
        based on the class name"""
        args_list = args.split()
        if not args_list:
            print([str(value) for value in models.storage.all().values()])
        else:
            class_name = args_list[0]
            if class_name not in models.classes:
                print("** class doesn't exist **")
                return

            instances = [str(value) for key, value in
                         models.storage.all().items()
                         if key.split('.')[0] == class_name]
            print(instances)

    def do_update(self, args):
        """Update an instance based on the class name and id
        by adding or updating an attribute"""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return

        if len(args_list) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args_list[2]
        if len(args_list) < 4:
            print("** value missing **")
            return

        try:
            attribute_value = models.typecast_value
            (attribute_name, args_list[3])
        except ValueError:
            print("** value missing **")
            return

        instance = models.storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def emptyline(self):
        """Do nothing when an empty line is provided"""
        pass

    def do_quit(self, args):
        """Exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program"""
        print()  # Print a newline before exiting
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
