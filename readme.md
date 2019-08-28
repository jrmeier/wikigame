# Wikipedia Game

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


