#	Description of the project

AirBnB is an online platform or marketplace that allows people to list, discover, and book accommodations around the world, ranging from private rooms to entire houses or apartments.

This project attempts to clone the popular AirBnB - to mimic the core functionality and features of the the Web Application, providing similar users experience.

The focus of this project is to interact the mimic AirBnb via the Console - the command line interface.

#	Description of the command interpreter

since the interaction with the AirBnB project will be from the console, there is need to create commands that will handle various operations.

A command interpreter is a program that interpretes and executes command entered by users in a text-based interface. it will provides a way to interact with the mimic AirBnb via the console.

In Python, the cmd module provides a framework for building command-line interpreters or shells. It allows you to create interactive command-line applications with custom commands and functionalities.

#	Usage of the cmd module

To use the cmd module, you need to import it in your Python script:
-> import cmd

You can then create a subclass of the cmd.Cmd class and define your own commands by overriding the appropriate methods. Here's a simple example:

-> class MyCmd(cmd.Cmd):
	prompt = '(AiBnB) ' # display prompt to user

	do_greet(self, line):
		""" welcomes the user
		Args:
			line : The name of the user
		"""
		print("Welcome {}".format(line))
	do_EOF(self):
		""" Exit the command interpreter"""
		return True

-> if __name__ == '__main__':
    MyCmd().cmdloop()


