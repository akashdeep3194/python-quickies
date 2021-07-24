import datetime
import time
import uuid
import sqlite3

conn = sqlite3.connect('Hotel_Management.db')
c = conn.cursor()


class Room:

    def __init__(self, room_details):
        self.id = uuid.uuid4()
        self.number = room_details[0]
        self.floor = room_details[1]
        self.cost = room_details[2]


class Booking:
    pass


class Guest:
    def __init__(self, name):
        self.name = name

    pass


class Receptionist:
    pass


class Admin:

    def listRooms(self):
        x= '''SELECT * From ROOMS'''
        c.execute(x)
        records = c.fetchall()
        for r in records:
            for ele in r:
                print(ele)


    @staticmethod
    def addRoom():
        roomDetails = [int(input("Enter Room Number\n")), int(input("Enter Floor Number\n")), float(input("Enter Room Cost\n"))]
        new_room = Room(roomDetails)
        print("Room Created with id", new_room.id)
        x = '''INSERT INTO ROOMS(Number,Floor,Date,id) VALUES ("{}","{}","{}","{}")'''.format(roomDetails[0], roomDetails[1],
                                                                                              datetime.datetime.utcnow().isoformat(), new_room.id)
        c.execute(x)
        conn.commit()


admininstrator = Admin()
# admininstrator.addRoom()
admininstrator.listRooms()
