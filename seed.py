"""Script to seed database."""

import os
import json
import csv
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb database')
os.system('createdb database')

model.connect_to_db(server.app)
model.db.create_all()

# Load data from JSON file
with open('data/data.json') as f:
    seed_data = json.loads(f.read())

# Load data from CSV file
f1 = open(filename)
csv_f = csv.reader(f1)
for row in csv_f:
    item, item, item = row