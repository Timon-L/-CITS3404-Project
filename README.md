# CITS3404-Project

The task is to create an online daily puzzle with interactivity and other features similar to Wordle. The project demonstrates the use of HTML, CSS, Flask, AJAX, JQuery and Bootstrap.

**Zero** is a number puzzle game. The player is given a randomly generated starting number, a set of numbers and mathematical operations. Use the operation and set of numbers to get the starting number to zero.

## Game design and architecture
The goal is to get a randomly generated starting number to 0 with the least number of moves. The game includes a starting number called the puzzle number, one number being currently used called the current, 3 upcoming numbers called upcoming numbers, 2 trade number options, 4 operators: division, multiplication, addition and subtraction.

By allowing the player to see 3 upcoming numbers lets the player to plan ahead. The trade buttons allows the player to have a bit more freedom in getting to the number 0. There are different trade options to facilitate that. Trade option 1, trades the current number with the first upcoming number and Trade option 2, trades the first upcoming number with the second.

The architecture that has been implemented on the client-side is using HTML for content, CSS for styling and Javascript for reactive purposes and functionality of the webpage. The server-side is using Flask for database inputs and retrivals.

## Launch instructions
Dependencies should be first installed, preferably on a virtual environment, with the following command:
```
pip3 install -r [path-to-server-folder]/requirements.txt
```
The Flask server can then be started with the following command:
```
flask run
```
In the event that the server does not launch, the environment variable `FLASKAPP` should be set to `main`.

## Unit testing
**Zero** employs unit testing on the database model `User`. All tests on the database can be run with the following command:
```
python3 -m dbunittest
```
This module creates 32 virtual users with randomly generated usernames and passwords, to test the following functionalities:
- Account creation, determining if accounts are only in the database after creating the entires to them.
- Passwords, determining if account password hashes in the database indeed were produced from user input. This takes the most time in the test due to the hashing algorithm used.
- Score changes, where scores are defined in this test as the statistics of the user (max/min/number of moves, number of games played/won)
After these tests the temporary database is dropped and destroyed.

On a recent machine, the tests should take around 90 seconds to complete.