# Python Click Web Scapper

--Work-In-Progress--

## Description

I wanted to build a command line tool that allows a user to stay in the command line and check the NBA League's schedule for a particular day. Upon my research I found click, a Python package for creating command line interfaces. As of right now it is rather simple, you can only look at the schedule for each playing day. However, in time I plan on implementing more features.

## Installation

I split my requirements.txt into one for Windows and one for Linux. Really the only difference between the two is I removed pywin32 and pypiwin32. They both gave me issues when installing on Manjaro. Install the requirements:

Windows
    
    pip install -r windows.txt
    
Linux

    pip install -r linux.txt


Lastly, we setup the command with:

    pip install --editable .

## Usage

I use Git-Bash on Windows but a quick test showed it worked in PowerShell and CMD. I tested it in terminal in Manjaro without issues as well. Quick walkthrough of the commands.

Once installed properly you should be able to go into your terminal and enter the command:

    game-schedule

This should print the schedule for the current day. This will check the league's schedule for the day. For right now it only takes input for how many days you want to go back or forward. This is done by the -d flag, as you'll see below.

Yesterday's schedule (include's the scores):

    game-schedule -d -1

Tomorrow's schedule:

    game-schedule -d 1

Note: Games already played or in-progress will display a box score. Game's that are yet to be played will display the spread and over/under, if the information has been made available. 