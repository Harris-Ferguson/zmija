# USASK 2nd Years Battlesnake
This a battlesnake server implementing the Battlesnake API to participate in the [Battlesnake Saskatchewan](https://play.battlesnake.com/competitions/saskatchewan-2020/) event
built by a group of 2nd year Usask CS Majors

Starter code taken from the [Battlesnake Python Starter Project](https://github.com/BattlesnakeOfficial/starter-snake-python)

## Running and Contributing Instructions
Fork this repo and add it to your [repl](https://repl.it/~) account, then run `python server.py` to launch the server. You will get a URL to give to your Battlesnake account to test your snake. PR's to the main branch on this repo will update the Competition Snake on the Team's account on Battlesnake. 

### Alternatives to repl
Although repl is the easiest to just get the snake running for testing, there are a few other options
- You could run this server on your machine, but you would need to set up a port forwarding tool 
- You can set up a function app on Azure, and through the U of S we get $100 compute credits for free, so this is a decent alternative 

### Mojave
[Mojave](https://github.com/smallsco/mojave) is a 3rd party battlesnakes desktop app. You can use this to test your server offline, its incredibly useful. Makes the process a lot smoother than constantly updating a repl and going to the battlesnakes site.
=======
## Contributing Instructions

### Running
Fork this repo and add it to your [repl](https://repl.it/~) account, then run `python app/server.py` to launch the server. You will get a URL to give to your Battlesnake account to
test your changes. PR's to this repo will update the Competition Snake, which will be connected to Our Team on Battlesnake. 
### Tests
This project uses pytest. simply run `pytest` in the root of the directory. You will need pytest installed either globally or in a virtual environment. 



## Dependancies 
You will need the CherryPy module installed on your repl for this to work. If you are having trouble running the server on repl, make sure you install cherrypy using pip.

## Team Planning Links
[Team Trello](https://trello.com/b/RdRO0AQ7/usask2ndyearbattlesnake)
