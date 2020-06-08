# Instructions

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

Good luck!
