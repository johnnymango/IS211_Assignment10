#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Assignment 10 - Querying Pets Data"""

import sqlite3


#Creates connection.
conn = sqlite3.connect("pets.db")
cur = conn.cursor()

#Raw Input value for ID.
personID = raw_input('Please enter an ID number: ')

#Queries the DB; join allows for a single query with all data elements needed for output.
cur.execute(
    """SELECT person.first_name, person.last_name, person.age, pet.name, pet.breed, pet.age
    FROM person
        JOIN person_pet ON person.id = person_pet.person_id
        JOIN pet ON pet.id = person_pet.pet_id
    WHERE person.id = ?;""", [(personID)]
)
row = cur.fetchall()


#Parses and prints query result.
if personID == '-1':
    print 'Exiting Query.'
    exit()

elif row == []:
    print "Person ID was not found in database. Exiting."
    exit()

else:
    print "{} {} is {} years old.".format(row[0][0], row[0][1], str(row[0][2]))
    print "{} {} owned {}, a {}, that was {} years old.".format(row[0][0], row[0][1], row[0][3], row[0][4], str(row[0][5]))