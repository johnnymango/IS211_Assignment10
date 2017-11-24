#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Assignment 10 - Loading Pets Data"""

import sqlite3

#Person data
Person = (
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
)

#Pet data
Pet = (
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
)

#Relationship data
Person_Pet = (
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
)

conn = sqlite3.connect("pets.db")
cur = conn.cursor()


#Drops tables.
cur.execute("DROP TABLE IF EXISTS person")
cur.execute("DROP TABLE IF EXISTS pet")
cur.execute("DROP TABLE IF EXISTS person_pet")
conn.commit()


#Creates Person table.
cur.execute("CREATE TABLE person(id int PRIMARY KEY, first_name text,"
        "last_name text, age int)")
conn.commit()


#Creates Pet table.
cur.execute("CREATE TABLE pet(id int PRIMARY KEY, name text,"
        "breed text, age int, dead int)")
conn.commit()

#Creates Person_Pet table
cur.execute("CREATE TABLE person_pet(person_id int, pet_id int)")
conn.commit()

#Inserts data.
cur.executemany("INSERT INTO person VALUES(?, ?, ?, ?)", Person)
cur.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", Pet)
cur.executemany("INSERT INTO person_pet VALUES(?, ?)", Person_Pet)
conn.commit()

conn.close()
