## Description

A collection of CLI scripts written in Python using the Click package. This will range from Linux utility scripts (i.e. database connection manager for MySQL + MongoDB) 

to scripts for personal intrests (at this time I am including a webscrapper for NBA scores). 


### Installation

More details will come soon. Each script is within its own directory. Each directory will (soon) contain it's own requirements.txt file. Each script was built under

a virtual enviroment, so it is heavily recommended to do the same. 

Steps:

    cd `script name`

    virtualenv venv

    . venv/bin/activate

    pip install -r requirements.txt

    pip install --editable .

    deactivate

Once all the steps have been followed the script you have installed should be installed. All scripts include --help flag for details to run them/flags/arguements.