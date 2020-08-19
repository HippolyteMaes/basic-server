import csv
import json

from datetime import datetime

from flask import Flask


app = Flask(__name__)


@app.route('/')
@app.route('/<date_format>')
def smallapps(date_format=None):
    smallapps_json = []
    with open('smallapps.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            smallapp = {'name': row[0]}
            last_update = row[1].strip(' ')
            if len(last_update) > 0 and date_format == 'en':
                date = datetime.strptime(last_update, '%Y-%m-%d %H:%M')
                last_update = date.strftime('%Y-%d-%m %H:%M')
            smallapp['last_update'] = last_update
            smallapps_json.append(smallapp)
    return json.dumps(smallapps_json) 
