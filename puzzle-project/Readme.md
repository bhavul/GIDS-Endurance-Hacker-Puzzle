# Hacker's Puzzle developed for GIDS

For GIDS 2017 Conference, I had developed a coding/hacker sort of puzzle, and the winner was awarded with an iPad. This is that puzzle.
I was working with [Endurance International Group](https://www.endurance.com/) (Previously [Directi](https://www.directi.com/)) back then, and they had a booth at [GIDS](https://www.developermarch.com/developersummit/) 2017.


## Directory Structure

The whole project is based on [Pyramid framework](https://docs.pylonsproject.org/projects/pyramid/en/latest/index.html). Some of the files are also files that are required due to Pyramid conventions.

**For more on how to build and run pyramid projects**, [read here](https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/project.html)

| Directory / File | What they contain |
|---|---|
|development.ini| This is required to run the pyramid app |
|myapp.wsgi| Example wsgi |
|pyramid.wsgi| The wsgi file which controls how to run the app |
|setup.py| Used to install the app as a package, so pyramid can serve the app |
|**puzzle/** | **Contains the actual code for the app**. This has its own readme, which tells about each file.
|puzzle.egg-info/ | These are automatically generated files
|puzzle-project.iml | Automatically generated file
