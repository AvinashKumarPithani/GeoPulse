from fastapi.responses import Response
import xml.etree.ElementTree as ET

from fastapi import FastAPI
import sqlite3
import pandas as pd

app = FastAPI()

DB_PATH = "weather.db"

# Get all data
@app.get("/observations")
def get_all():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM observations LIMIT 100", conn)
    conn.close()
    return df.to_dict(orient="records")


# Filtered query (IMPORTANT)
@app.get("/observations/filter")
def filter_data(
    min_lat: float,
    max_lat: float,
    min_lon: float,
    max_lon: float,
    start_time: str,
    end_time: str,
    min_temp: float = None
):
    conn = sqlite3.connect(DB_PATH)

    query = f"""
    SELECT * FROM observations
    WHERE latitude BETWEEN {min_lat} AND {max_lat}
    AND longitude BETWEEN {min_lon} AND {max_lon}
    AND timestamp BETWEEN '{start_time}' AND '{end_time}'
    """

    if min_temp:
        query += f" AND temperature > {min_temp}"

    df = pd.read_sql(query, conn)
    conn.close()

    return df.to_dict(orient="records")

@app.get("/")
def home():
    return {"message": "GeoPulse API is running"}

def to_xml(data):
    root = ET.Element("Observations")

    for row in data:
        obs = ET.SubElement(root, "Observation")

        for key, val in row.items():
            child = ET.SubElement(obs, key)
            child.text = str(val)

    return ET.tostring(root)

@app.get("/observations/xml")
def get_xml():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM observations LIMIT 100", conn)
    conn.close()

    xml_data = to_xml(df.to_dict(orient="records"))

    return Response(content=xml_data, media_type="application/xml")

@app.get("/sensor")
def get_sensor():
    with open("sensorml.xml", "r") as file:
        data = file.read()

    return Response(content=data, media_type="application/xml")