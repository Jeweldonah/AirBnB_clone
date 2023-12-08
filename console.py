#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program"""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing when an empty line isprovided"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
