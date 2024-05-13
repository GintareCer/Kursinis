# INTRODUCTION

## Goal
Analyze and understand a codebase related to a "Snake game" implemented in Python. 

## Topic
Object-Oriented Programming (OOP) principles and design patterns in a Python implementation of the "Snake game".

## Application
To allow users to play the "Snake game", where they control a snake moving around a grid or screen, consuming food to grow longer while avoiding collisions with the snake's own body or the boundaries of the game area.

## Using and Running the Program
To run the program, follow these steps:

1. Download all files that I uploaded to GIT to your computer.
2. Put all downloaded files into one folder.
3. Open your code editor e.g. Visual Studio Code.
4. Add folder that you created in code editor.
5. Go to main.py and press "Run Python File".

# BODY / ANLYSIS

## 4 OOP pillars that are used in the code
### Encapsulation
Encapsulation refers to the bundling of data with the methods that operate on that data, or the restriction of direct access. Access modifiers limit access to the variables and methods of a class. Python provides three types of access modifiers. Access modifiers limit access to the variables and methods of a class. Python provides three types of access modifiers private, public, and protected.

Public Member: Accessible anywhere from otside oclass.

Private Member: Accessible within the class.

Protected Member: Accessible within the class and its sub-classes private, public, and protected.


This pillar can be seen in a lot of different parts of the code. For example, in "snake.py" code:

![snake.py.1pic](<Screenshot (364).png>)

![snake.py.2pic](<Screenshot (366).png>)

1. The list_of_piece attribute is accessible from outside the class.

2.  In several methods (reset_snake, move_snake), the class directly manipulates the list_of_piece attribute.

This pillar can also be seen in “scoreboard.py” code:

1. The file handling operations for reading and writing the high score are encapsulated within the read_scoreboard_file() and update_high_score() methods. This encapsulation ensures that the details of how the high score is stored and retrieved are hidden from the rest of the program.

2. The methods provided by the Scoreboard class serve as an interface for interacting with the scoreboard data. These methods encapsulate the logic for updating and managing the score and level, abstracting away the internal details of how these operations are implemented.

In code “display.py”:

1. The MyScreen class depends on the Snake class for the listen_snake method. Dependency injection is a principle of encapsulation where dependencies are passed into a class rather than being created or accessed directly within the class. This promotes loose coupling and makes the class easier to test and reuse.

2. Constants like X_SCREEN, Y_SCREEN, SCREEN_COLOR, and SCREEN_TITLE are defined outside the class - they are encapsulated within the module.

### Inheritance

Inheritance - a mechanism that allows a class to inherit properties and behaviors from another class.

We can see that inheritance is used in code "scoreboard.py".

![scoreboard.py.1pic](<Screenshot (372).png>)

"Scoreboard" class directly inherits from Turtle, which is presumably a class provided by the turtle module.

Inheritance can also be seen in "food.py" code:

![food.py.1pic](<Screenshot (373).png>)

In this picture we can see, class Food(Turtle): which indicates that the "Food" class inherits from the "Turtle" class. By inheriting from "Turtle", the "Food" class gains access to all the methods and attributes of the "Turtle" class, such as penup(), shape(), shapesize(), color(), and speed(). This allows the "Food" objects to be treated as turtle graphics objects and utilize turtle-specific functionality.

We can notice that "bord.py" code also use inhertance:

![bord.py.1pic](<Screenshot (374).png>)

"BordGame" is defined as a subclass of "Turtle". This means that "BordGame" inherits all the attributes and methods of the Turtle class. When you create an instance of "BordGame", you can use both the methods and attributes defined in "BordGame" itself and those inherited from "Turtle".

### Abstraction

Abstraction - the ability to separate the what from the how, to focus on the high-level ideas separately from
the low-level details.


In code "snake.py":

The "Snake" class encapsulates the behavior and properties of a snake in the game. It provides methods for creating the snake, adding a tail, moving the snake, changing its direction, and resetting it. This class abstracts away the details of how the snake's body is managed and how it moves, making it easier to interact with the snake object without needing to understand its internal workings.

In "scoreboard.py" code:

![scoreboard.py.1pic](<Screenshot (375).png>)

1. The "Scoreboard" class abstracts away the concept of keeping track of the game's score, level, and high score. It encapsulates related functionality and data attributes into a single class, providing a higher-level interface for interacting with these elements.

![scoreboard.py.2pic](<Screenshot (376).png>)


![scoreboard.py.3pic](<Screenshot (378).png>)

2. The read_scoreboard_file and update_high_score methods abstract away the details of reading from and writing to a file. They provide a clear interface for interacting with the score data stored in a file without exposing the underlying file handling implementation details.

![scoreboard.py.4pic](<Screenshot (379).png>)

![scoreboard.py.5pic](<Screenshot (382).png>)

3. The methods increase_score, increase_level, and refresh_score abstract away the logic for updating the score and level based on game events. They provide a clear interface for incrementing the score and level, as well as refreshing the displayed score information.


### Polymorphism

Polymorphism is the ability of any data to be processed in more than one form.

## Design patterns 

In code "food.py":
Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. The MyScreen() class is a candidate for implementing the Singleton pattern if it guarantees that only one instance of MyScreen is created throughout the program execution. 

Using the Singleton pattern in this scenario helps to streamline resource usage, ensure consistency, provide global access, synchronize access in multithreaded environments, and encapsulate instance creation logic, ultimately leading to a more efficient and maintainable codebase.

# RESULTS

1. The analysis revealed that the codebase effectively utilizes OOP principles such as encapsulation, inheritance, and abstraction, which contribute to better organization, modularity, and maintainability of the code.

2. By encapsulating data and behavior within classes and providing well-defined interfaces, the codebase hides internal complexities and allows for easier understanding and modification of individual components.

3. Challenges during implementation may have included ensuring proper adherence to OOP principles throughout the codebase, as well as identifying and applying appropriate design patterns to improve code structure and maintainability.

# SUMMARY

The Snake game codebase embodies OOP principles, leveraging design patterns effectively and laying a strong foundation for future enhancements. Beyond just entertainment, it doubles as an educational tool, offering a hands-on experience in grasping Python's OOP concepts and design patterns.