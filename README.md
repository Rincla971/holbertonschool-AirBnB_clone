# AirBnB clone - The console

<img width="560" alt="rbnb" src="https://github.com/Rincla971/holbertonschool-AirBnB_clone/assets/146451776/b8708aca-bed4-4c29-b4f3-0b5280b97b23">

## INTRODUCTION

This is a command-line application designed to manage AirBnB objects, part of a larger project to build an AirBnB clone. The project focuses on creating a command interpreter for various functionalities like creating, retrieving, updating, and destroying objects. The application allows users to interact with objects of various classes, including User, State, City, and Place, and stores the data in a file-based storage system.
## Background Context
Welcome to the AirBnB clone project! Before starting, please read the AirBnB concept page.
## First Step
- The initial step in building the AirBnB clone is to create a command interpreter that manages AirBnB objects. This command interpreter is crucial for the overall functionality of the project. Key tasks include:
- Creating a parent class (BaseModel) to handle the initialization, serialization, and deserialization of instances.
- Establishing a flow of serialization and deserialization from instances to dictionaries to JSON strings to files.
- Creating classes for AirBnB objects (User, State, City, Place, etc.) that inherit from BaseModel.
- Developing the first abstracted storage engine (File storage) for the project.
- Implementing unit tests to validate all classes and the storage engine
## What's a Command Interpreter?
The command interpreter is similar to a command-line shell but is specific to the AirBnB project. It enables users to perform the following actions:

- Create a new object (e.g., User, Place, etc.).
- Retrieve an object from storage.
- Perform operations on objects (e.g., counting, computing statistics).
- Update attributes of an object.
- Delete an object.
## Resources
Read or watch:

- [cmd module](https://docs.python.org/3.4/library/cmd.html)
- packages concept page
- [uuid module](https://docs.python.org/3.4/library/uuid.html)
- [datetime](https://docs.python.org/3.4/library/datetime.html)
- [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

- How to create a Python package
- How to create a command interpreter in Python using the `cmd` module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage `datetime`
- What is an `UUID`
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

## Requirements
## Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Python Unit Tests

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the `unittest module`
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Author
[Fatoumata Bah](https://www.github.com/fatima9821)
[Reginord Rincla](https://www.github.com/Rincla971)


