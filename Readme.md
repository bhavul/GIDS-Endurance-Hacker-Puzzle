# Hacker's Puzzle developed for GIDS

For GIDS 2017 Conference, I had developed a coding/hacker sort of puzzle, and the winner was awarded with an iPad. This is that puzzle.
I was working with [Endurance International Group](https://www.endurance.com/) (Previously [Directi](https://www.directi.com/)) back then, and they had a booth at [GIDS](https://www.developermarch.com/developersummit/) 2017.

So, this is essentially quite an old repository, just being pushed to Git quite late.

## How to install?

Warning : Some of these instructions may be little rusty. I had not created a proper readme.md file back when this was developed, and have reverse-engineered this whole readme now from bash history of the server as well as some common sense. 

### Specifications

* Requires Apache2 Server
* Runs on Python v2.7 (this was done back in 2017 and never required an update, hence not yet ported to v3)
* Uses sqlite3 for database
* Uses pyramid framework for handling APIs (alternative to django, flask)

### Installation and Running instructions

```shell
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi
sudo apt-get install sqlite3
```

The virtual environment(env, venv) is bundled with the app repository. Switching to the virtual environment should be as simple as : 

```shell
. /path/to/this/repo/venv/bin/activate
```

And then to install the current puzzle app as a python package

```shell
/path/to/this/repo/venv/bin/pip install -e .
```

Similarly, the `apache2.conf` has also been bundled so you'd know which one was used by the app and worked just fine.

Requires these python packages (all are installable via pip), in case you wish to use your own virtual environment :
 
```shell
pyramid==1.8.3
webtest
pytest
pytest-cov 
deform 
sqlite3
pysqlite
sqlalchemy 
pyramid_chameleon 
pyramid_debugtoolbar 
pyramid_tm 
zope.sqlalchemy 
waitress
pastedeploy
```

### Setup Instructions

Note : In my case, I had deployed the code at 
`/var/www/GIDS-puzzle-final/puzzle-project/puzzle` directory. There **_could_** be some references to this path in metadata files, which you can check for while deploying. For example, one place where this path exists is in `pyramid.wsgi`. 


The app runs on pyramid framework and hosted on apache. Since it is using sqlite3 db, the db file would need to be owned by www-data for the app to be able to read/write to the db.

```shell
chown www-data:www-data tasks.db
chown www-data:www-data schema.sql 

# In case you've deployed it somewhere else
chown www-data:www-data /var/www/GIDS-puzzle-final/puzzle-project/puzzle
```

## Running

To Start / Restart / Stop Apache server

```shell
# start
systemctl start apache2

# restart
systemctl restart apache2

# stop
systemctl stop apache2
```

To reload the app without any downtime

```shell
/etc/init.d/apache2 reload
```

How to run

```shell
# inside /var/www/GIDS-puzzle-final
# virtualenv -p python venv27
# . venv27/bin/activate

# inside puzzle-project (where you have setup.py)
# ../env/bin/pserve development.ini --reload
```


## Repository Structure

| Directory / File | What they contain |
|---|---|
|apache2.conf| The apache conf that was used for serving the app|
|bootstrap.min.css| The bootstrap file used by the static html pages|
|in.txt| The last puzzle has a hyperlink to download the input file for that coding puzzle. This is that input file. |
|env/| First python environment |
|venv/| Second python environment |
|Screenshots/ | Contains screenshots of the app, of how each page is supposed to look like
|puzzle-project/ | Contains the codebase of the project. It has its own readme.md inside it.


## Author

Bhavul Gauri 

