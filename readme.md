# Wikipedia Game

## Instructions

The Wikipedia game:

Problem: 
	Given a starting page on Wikipedia, using connected pages, find a list of linked pages to a target page.

	For example, starting at the page: "Web Bot" and target page: "Tax Holiday". Web Bot has a link to the page "Barack Obama", which has a link to "Tax credit", which has a link to the page "Tax holiday", the end page. Therefore, the answer would be:

	Web Bot -> Barack Obama -> Tax credit -> Tax holiday

	I would run through this path way yourself to understand the problem:
	https://en.wikipedia.org/wiki/Web_Bot

Instructions:
	We're looking for a Python program called "wikipedia_game.py" that takes a source page and target page as command line arguments and you give me the list of connected links from start to end. Please zip up the wikipedia_game.py program along with a requirements.txt (if you used any pip packages) and any other resources used to solve the problem. Try to make sure that after unzipping and installing any pip requirements that the python program will run in it's current directory. If you have a more advanced solution, for example using a database, please provide instructions to set it up.

	Given this input for the python pogram:
	python wikipedia_game.py "Web Bot" "Tax Holiday"
	We should get this output:
	Web Bot -> Barack Obama -> Tax credit -> Tax holiday

Tips:
 - Any path can do but shorter will probably be easier
 - Run time can be long for unconnected pages
 - Feel free to use any python packages
 - Start with a closely connected pages
 - Normalizing page names and URL's is very helpful


## Setup

1. Create a new Python 3.6.5 env: `python3 -m venv .wikigame`
2. Install requirments: `pip3 install -r requirements.txt`
3. Activate the environment: `source .wikigame/bin/activate`

Now you shold be set up.

## Issues
While this does travel the branch, I keep running an error where Python quits unexpectedly. I think its because my queue is grows too large and overflows. I think the solution would be to create a hash table of and store references to hashes of the path instead of the entire path all the time. Due to time, I wasn't able get that added.

The given case: 
`python wikipedia_game.py "Web Bot" "Tax Holiday"`
doesn't complete.


A short path: `python wikipedia_game.py "Web Bot" "Tax Credit"` does complete.
