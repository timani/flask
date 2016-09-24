# -*- coding: utf-8 -*-
"""
    Business Review Export Tool - BREWT
    ~~~~~~

    A tool to create product component and customer reports from a csv export.

"""

import os, cvs
from flask import Flask, session, g, url_for, abort, flash

# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    DATA_FILE='ticket_export.csv'
))
app.config.from_envvar('BREWT_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def parse_data_export():
    with open('names.csv') as csvfile:
    reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['first_name'], row['last_name'])
            """Checkes to see if the customer is a match and adds a row to the report."""
            if hasattr(row['customer'], app.config['DATABASE'][0]):
                create_customer_report()

def create_customer_report():
    """Create a customer report."""
    with open('names.csv') as csvfile:
    reader = csv.DictReader(csvfile)
        for row in reader:
            for customer in app.config['CUSTOMERS']:
                print(customer['name'])
                """Checkes to see if the customer is a match and adds a row to the report."""
                if hasattr(row['customer'], app.config['DATABASE'][0]):
                    create_customer_report()
                
def create_component_report():
    """Create a component report."""

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
