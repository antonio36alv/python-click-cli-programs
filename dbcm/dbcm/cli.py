from mongoengine import *
import readline

import click
disconnect()
connect("db_connections", host="127.0.0.1", port=27017)

from os import system

from .dbConnection import dbConnection

@click.command()
@click.option("--add", is_flag=True, help="Add a new connection")
@click.option("-C", is_flag=True, help="Connect to a DB")
def cli(add, c):
    """
    Self-made utility for managind database connections

    The intent is to rid of any need for Robo 3t or MySQL Workbench
    """
    if add:
        # we add a new connection and connect/test it
        createNewConnection()
    if c:
        print("show me what you got")
        if click.confirm("See all databases"):
            data = dbConnection.objects().as_pymongo()
            # handle how to print data here
            # probably just want representational id, name, db type
            print(data)

    nameSelected = input("Please enter a name or id: ")
    # maybe print again

    connection = dbConnection.objects(name=nameSelected)
    if connection["db_type"] == "mysql":
        click.echo(f"Connectiong to DB: {connection.name}")
        system(f"mysql -u {connection.username} -h {connection.host} -p")
"""
name
command
description
db_type
"""

    # system(f"mongo {host} -u {username} -p {password}")

def createNewConnection():
    # get name input
    name = input("Name of Db or controller to refrence by: ")
    # get description input
    description = input("(Optional) Description: ")
    while(len(description) < 20):
        readline.set_startup_hook(lambda : readline.insert_text(description))
        description = input("Please make your description longer:\n")
        
    # get db type (mongo or mysql)
    db_type = input("DB type (mysql or mongo): ")
    print(db_type)
    while(db_type != "mongo" and db_type != "mysql"):
        click.echo("Issue with your input, try again.")
        db_type = input("DB type (mysql or mongo): ")
    click.echo(f"Typical {db_type} command connection: ")
    if db_type == "mongo":
        click.echo("mongo ds139360.mlab.com:39360/heroku_6l9wrzj1 -u <dbuser> -p <dbpassword>")
    else:
        click.echo("mysql -u <username> -h <host> -p")
    command = input("Enter your command: ")
    if click.confirm("Connect/Test Connection? "):
        system(command)
        if click.confirm("Happy? Did that go well? If yes it will be saved."):
            connection = dbConnection(name=name, db_type=db_type, command=command, description=description)
            connection.save()
    if click.confirm(f"Add command: '{command}'?"):
        connection = dbConnection(name=name, db_type=db_type, command=command, description=description)
        connection.save()
        click.echo("saved!")

# if __name__ == "__main__":
#     cli()
