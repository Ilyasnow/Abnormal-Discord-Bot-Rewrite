import discord

#Module for on_ready() discord event

#module attributes
attributes = {"Name":"on_ready",
              "Type":"event",
              "Description":"on_ready() event handler",
              "Events":["on_ready","foo"]}

class Event():

    def on_ready(self,client):
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
