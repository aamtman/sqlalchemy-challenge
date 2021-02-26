import numpy as np
import date time as dt 
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/passengers"
    )


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    #json list of Temperature observations (tobs) for the previous year
    #@app.route('/api/v1.0/tobs')
    #def tobs()

    #json list of the min temp, avg tem, max temp where date= given start<=
    #@app.route('/api/v1.0/tobs')
    def temps_startOnly(start):
        query = f'SELECT AVG(temp) AS "Average Temperature", MIN(temp) \
                AS "Minimum Temperature", MAX(temp) AS "Maximum Temperature"\
                FROM measurements WHERE date >= "{start}"

    return jsonify(pd.read_sql(query, engine).to_dict(orient='records'))

    #"""Return a list of all passenger names"""
    # Query all passengers
   # results = session.query(Measurement.date, Measurement.prcp).all()

    #json list: min temp, avg temp, max temp for dates between start/end inclusive
    @app.route('/api/v1.0/tobs')
    def temps_startAndEnd((start, end):
        query = (f'SELECT' AVG(temp) AS "Average Temperature", MIN(temp)\
                AS "Minimum Temperature", MAX(temp) AS "Maximum Temperature"\
                FROM measurements WHERE date >= "{start}" AND date <= "{end}"')
            retrun jsonify(pd.read_sql(query, engine).to_dict(orient='records'));

    session.close()

    # Convert list of tuples into normal list
    #precipitation = {date: prcp for date, prcp in results}

    #return jsonify(precipitation)


# @app.route("/api/v1.0/passengers")
# def passengers():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # Query all passengers
#     results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

#     session.close()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_passengers = []
#     for name, age, sex in results:
#         passenger_dict = {}
#         passenger_dict["name"] = name
#         passenger_dict["age"] = age
#         passenger_dict["sex"] = sex
#         all_passengers.append(passenger_dict)

#     return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)

