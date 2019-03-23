# Hacker's Puzzle developed for GIDS

For GIDS 2017 Conference, I had developed a coding/hacker sort of puzzle, and the winner was awarded with an iPad. This is that puzzle.
I was working with [Endurance International Group](https://www.endurance.com/) (Previously [Directi](https://www.directi.com/)) back then, and they had a booth at [GIDS](https://www.developermarch.com/developersummit/) 2017.


## Directory Structure

This directory contains the actual code that I developed for the app.


| Directory / File | What they contain |
|---|---|
|htmls/| This contains the different html files that are rendered. They're in `.pt` extensions as they are pyramid templates, and do have some dynamic nature to them (some variables get filled at runtime). But mostly, this is html code. |
|static/| This contains static files used by the above templates, namely bootstrap and othe css files. |
|schema.sql| This is a sql file which defines all the table structures. When you run the app, these are automatically run, and hence if reqd tables don't exist those are created.  |
|**views.py**| **This is the main file.** This handles all the logic for all the different levels/pages of the puzzles.  |
|getAndPost.py| Third level of puzzle requires some decryption to be done and answer to be submitted within 1 second. This can only be done via a script. This is a test code which passes that level.  |
|testDecryption.py | This is just code for caesar cypher's decryption.
|__init__.py | This initialises the app. This is called automatically by Pyramid and is the starting point of the app.


**For more on how to build and run pyramid projects**, [read here](https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/project.html)
