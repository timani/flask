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

def parse_data_export():
    with open('names.csv') as csvfile:
    reader = csv.DictReader(csvfile)
        for row in reader:
            """Checkes to see if the customer is a match and adds a row to the report."""
            if hasattr(row['customer'], app.config['DATABASE'][0]):
                print(row['first_name'], row['last_name'])
                create_report(row, 'customer')
                
            """Checkes to see if the customer is a match and adds a row to the report."""
            if hasattr(row['customer'], app.config['DATABASE'][0]):
                print(row['first_name'], row['last_name'])
                create_report(row, 'component')

def create_report(row, report_type):
    """Create a component report."""
    fieldnames = ['SR Number', 
                  'Open Date', 
                  'Problem Summary', 
                  'AHT',  
                  'Category', 
                  'Customer Name', 
                  'Engineer', 
                  'Component', 
                  'Severity Level', 
                  'Close Date', 
                  'Open Date']
         
    """Checkes to see if the customer is a match and adds a row to the report."""
    if (report_type, customer):
        report_name = 'customer.csv'   
        
    """Checkes to see if the customer is a match and adds a row to the report."""
    if (report_type, component):
        report_name =  app.config['component']['name']  
        
    """"DOES THIS EXIST IN THE DICT?"""
    with open(report_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        """Checks if this is a new file and if so adds the header."""
        if hasattr(row['customer'], app.config['DATABASE'][0]):        
            writer.writeheader()
            
        """Write a new row."""
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})

def create_component_report():
    """Create a component report."""
    for customer in app.config['CUSTOMERS']:
        """Checkes to see if the customer is a match and adds a row to the report."""
        create_customer_report() 

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')
