# GeoPulse - Interoperable Geospatial & Sensor Observation Platform

GNR629 Projects | CSRE, IIT Bombay

Developed by Avinash Kumar Pithani and Manas Avinashe

GeoPulse is a client-server geospatial platform implementing OGC-compliant WMS, WFS, and SOS services for spatial data visualization, feature querying, and sensor observation analysis.

The platform integrates:

- Interactive GIS visualization using OpenLayers
- OGC web services through GeoServer
- Sensor Observation Service (SOS 2.0) APIs using FastAPI
- Spatial and observational data workflows using PostgreSQL/PostGIS and SQLite

The system supports interoperable geospatial workflows including:

- GetCapabilities
- GetMap
- GetFeature
- GetFeatureInfo
- DescribeSensor
- Sensor observation retrieval and filtering

The project demonstrates interoperable GIS architecture, modular frontend design, client-server communication, spatial database integration, XML/JSON processing, and interactive geospatial workflows.

---

# Project Overview

GeoPulse combines modular interoperable geospatial components within a unified client-server web portal.

## 1. OGC Web Services Client (WMS/WFS)

A web-based GIS client that communicates with OGC-compliant WMS/WFS servers to retrieve and visualize spatial datasets.

The system supports:

- Dynamic layer discovery
- Map rendering
- Feature querying
- XML parsing
- Spatial layer management
- Multi-layer visualization

The interoperable design enables the client to connect to both local GeoServer instances and external public WMS/WFS services.

### Application Domain: Soil Moisture Monitoring – Maharashtra

The WMS/WFS module demonstrates interoperable GIS workflows using soil moisture-related geospatial datasets for Maharashtra, India.

The application enables interactive exploration of environmental layers relevant to:

- Agricultural monitoring
- Irrigation planning
- Drought assessment
- Water resource analysis

---

## 2. Sensor Observation Service (SOS 2.0)

A FastAPI-powered SOS implementation for querying and visualizing weather sensor observations from global cities.

The SOS module supports:

- Sensor metadata retrieval
- Observation filtering
- Time-series querying
- Interactive visualization
- XML and JSON response formats
- Real-time map-based sensor interaction

The system includes:

- 25 global sensor locations
- ~17,000 weather observations
- Multiple environmental parameters:
  - Temperature
  - Humidity
  - Wind Speed
  - Pressure
  - Precipitation

---

# Key Features

## OGC WMS/WFS Features

- Connect to WMS/WFS services (GeoServer, MapServer, QGIS Server, etc.)
- Retrieve and parse GetCapabilities documents
- Display WMS raster layers
- Display WFS vector layers
- Perform GetFeatureInfo requests
- Interactive feature querying
- Bounding box selection and map zooming
- CRS/SRS selection support
- Layer stacking with z-index control
- XML response visualization and parsing
- Responsive light/dark themed UI

---

## SOS Features

- SOS 2.0 GetCapabilities support
- DescribeSensor support using SensorML
- Observation retrieval with XML/JSON output
- Observation filtering by:
  - Country
  - Bounding box
  - Time range
  - Parameter type
  - Comparison operators

- Interactive map markers
- Table-to-map synchronization
- Observation charts and visualization
- FastAPI backend APIs

---

# Technology Stack

## Backend

- FastAPI
- Python
- GeoServer
- Apache Tomcat
- PostgreSQL + PostGIS
- SQLite

---

## Frontend

- HTML5
- CSS3
- Vanilla JavaScript (Modular Architecture)
- OpenLayers

---

## Data Processing & Parsing

- XML / SensorML Parsing
- GeoJSON Processing
- DOMParser
- Spatial Query Workflows

---

# Architecture Overview

GeoPulse follows a modular client-server architecture consisting of:

- A frontend GIS client built with OpenLayers and modular Vanilla JavaScript
- GeoServer-based WMS/WFS services for interoperable spatial data access
- A FastAPI backend implementing SOS 2.0 endpoints for sensor observations
- PostgreSQL/PostGIS and SQLite databases for spatial and observational datasets

The platform separates:

- OGC service communication
- Spatial visualization
- XML/JSON parsing
- Sensor observation workflows
- UI state and layout management

This modular structure improves maintainability, extensibility, and interoperability across geospatial services.

---

# Folder Structure

```text
GeoPulse/
├── backend/
│   ├── main.py                 # FastAPI server and SOS endpoints
│   ├── weather.db              # SQLite database (~17k weather observations)
│   ├── sensorml.xml            # SensorML 2.0 description for all sensors
│   ├── db_setup.py             # Script to rebuild database from CSV
│   └── requirements.txt
│
├── data/
│   ├── cleaned_weather.csv
│   └── process_data.py         # Dataset preprocessing and filtering
│
└── frontend/
    ├── index.html              # Main web portal interface
    │
    ├── css/
    │   └── style.css           # Styling and theme definitions
    │
    └── js/
        ├── config.js           # Global configuration and fetch wrapper
        ├── layout.js           # Resizable panels and UI layout handling
        ├── map.js              # OpenLayers map initialization and layer management
        ├── ogcRequests.js      # WMS/WFS request building and processing
        ├── sos.js              # SOS workflows, filters, charts, and sensor interaction
        ├── tabs.js             # OGC/SOS tab switching logic
        ├── theme.js            # Light/dark theme management
        └── xmlParser.js        # XML parsing and formatted response display
```

---

# System Workflow

The platform follows a modular client-server architecture where frontend modules independently manage map rendering, OGC request processing, SOS interactions, XML parsing, UI state management, and layout control.

## WMS/WFS Workflow

### 1. GetCapabilities Request

The client sends WMS/WFS GetCapabilities requests to retrieve:

- Layer metadata
- CRS information
- Bounding extents
- Layer hierarchy

The XML response is parsed using JavaScript DOMParser.

---

### 2. WMS GetMap Requests

Selected layers are rendered as map overlays using OpenLayers with support for:

- Layer stacking
- Opacity control
- CRS selection
- Bounding box filtering

---

### 3. WFS GetFeature Requests

Vector features are retrieved in GeoJSON format and visualized interactively on the map.

Feature attributes are displayed dynamically in the UI.

---

### 4. GetFeatureInfo Queries

Clicking map layers triggers:

- WMS GetFeatureInfo requests
- WFS vector feature inspection

The system prioritizes layers based on z-index ordering.

The AbortController on each new click cancels any in-flight request from a previous click to prevent request buildup during rapid interactions.

---

### 5. Bounding Box Selection

The client supports:

- Auto-filled extents
- Manual coordinate entry
- Draw-on-map bounding box selection

Coordinate validation ensures valid spatial ranges.

---

## SOS Workflow

### 1. GetCapabilities

Retrieves SOS service metadata in XML format.

---

### 2. DescribeSensor

Returns SensorML descriptions for all available sensors.

---

### 3. Observation Retrieval

Users can query observations using filters including:

- Country
- Bounding box
- Time range
- Environmental parameter
- Comparison operators

Responses can be returned as:

- XML
- JSON

---

### 4. Interactive Visualization

Observation results are:

- Displayed on the map
- Linked to tabular results
- Visualized through charts

Map markers and table rows remain synchronized.

---

# API Endpoints

| Endpoint              | Description                 |
| --------------------- | --------------------------- |
| GET /                 | Redirects to frontend       |
| GET /sos/capabilities | SOS GetCapabilities XML     |
| GET /sos/sensor       | SensorML sensor description |
| GET /sos/sensors      | Sensor locations (JSON)     |
| GET /sos/observations | Filtered observation data   |

---

# Observation Filter Parameters

| Parameter | Example             | Description                        |
| --------- | ------------------- | ---------------------------------- |
| country   | Japan               | Case-insensitive country filter    |
| bbox      | 60,10,140,50        | minLon,minLat,maxLon,maxLat        |
| start     | 2025-01-01 00:00:00 | Start of time window               |
| end       | 2025-03-31 23:59:59 | End of time window                 |
| param     | temperature         | Observed parameter                 |
| op        | gt                  | eq, neq, lt, lte, gt, gte, between |
| value     | 30                  | Comparison value                   |
| value2    | 40                  | Used with between                  |
| limit     | 500                 | Maximum rows                       |
| fmt       | json                | xml or json                        |

---

# Running the Project

## Requirements

- Python 3.10+
- GeoServer running on port 8080 (required for WMS/WFS module)
- PostgreSQL with PostGIS extension

---

## Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 127.0.0.1 --port 8000
```

Then open:

```text
http://127.0.0.1:8000
```

---

# Platform Testing

## OGC WMS/WFS Module

- Connect to a GeoServer WMS/WFS endpoint
- Retrieve capabilities
- Load map layers
- Query spatial features
- Visualize multi-layer geospatial data

---

## SOS Module

1. Open SOS tab
2. Click GetCapabilities
3. Click DescribeSensor
4. Select filters
5. Retrieve observations
6. Interact with map markers and charts

---

# Public WMS/WFS Services for Testing

| Service                      | URL                                                       |
| ---------------------------- | --------------------------------------------------------- |
| GeoSolutions GeoServer (WMS) | https://gs-stable.geo-solutions.it/geoserver/wms          |
| GeoSolutions GeoServer (WFS) | https://gs-stable.geo-solutions.it/geoserver/wfs          |
| NASA GIBS (WMS)              | https://gibs.earthdata.nasa.gov/wms/epsg3857/best/wms.cgi |
| NOAA Weather (WMS)           | https://opengeo.ncep.noaa.gov/geoserver/wms               |

---

# Dataset Information

The project includes:

- 25 global weather sensor locations
- ~17,000 observation records
- 5 environmental parameters
- Time-series observations from 2024–2026

The spatial module additionally uses:

- GeoServer-hosted raster/vector layers
- PostgreSQL/PostGIS spatial datasets
- Soil moisture monitoring layers

---

# Dependencies

- OpenLayers
- FastAPI
- GeoServer
- PostgreSQL/PostGIS
- SQLite
- Vanilla JavaScript DOM APIs

The frontend follows a modular JavaScript architecture with dedicated modules for:

- OGC request handling
- SOS workflows
- XML parsing
- Theme management
- Layout handling
- Tab navigation
- Map interaction

No frontend frameworks or build tools are required.

---

# Notes

- GeoServer is required for WMS/WFS functionality.
- SOS functionality works independently using FastAPI.
- Spatial datasets are not included in the repository.
- The frontend is implemented using modular Vanilla JavaScript components without external frontend frameworks.
- The project demonstrates interoperable GIS architecture, OGC web service workflows, modular frontend design, and sensor observation system integration.
