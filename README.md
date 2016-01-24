# Stealth Company Technical Test

## Introduction
Command line application that renders vetors as ascii characters.

## Execution ##

### Requisites ###
The following software is needed to execute this application:
* Python 2.7
* [virtualenv](http://pypi.python.org/pypi/virtualenv>)

### Python Virtual Environment ###
We deploy this application into it's own virtual environment therefore you will
need to do the same. Install & Activate the virtualenv (this assumes you are in
the root of the application folder using a cli):

        easy_install virtualenv
        mkdir ~/.virtualenvs
        cd ~/.virtualenvs
        virtualenv sc
        source ~/.virtualenvs/sc/bin/activate

### Install Python Packages ###
This assumes you are in the root of the application folder using cli:

        while read line; do easy_install -ZU $line; done < requires.txt
        while read line; do easy_install -ZU $line; done < requires-for-tests.txt

### Executing Unit Tests ###
This assumes you are in the root of the application folder using cli:

        python setup.py develop
        nosetests

### Executing Query ###
This assumes you are in the root of the application folder using cli. The
follow to be executed once to setup the application:

        python setup.py develop

The following to be used to find information (assumes you are in the src
folder):

        python stealthco/main.py [(x,y) - (x,y), (x,y) - (x,y),...]

## Test Cases ##
* (4,9) – (14,0), (0,4) – (19,4)
