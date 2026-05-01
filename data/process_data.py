import pandas as pd

# Load dataset
df = pd.read_csv("GlobalWeatherRepository.csv")

# Select required columns
df = df[[
    "location_name",
    "country",
    "latitude",
    "longitude",
    "last_updated_epoch",
    "temperature_celsius",
    "humidity",
    "wind_kph",
    "pressure_mb"
]]

# Rename columns
df = df.rename(columns={
    "last_updated_epoch": "timestamp",
    "temperature_celsius": "temperature",
    "wind_kph": "wind_speed",
    "pressure_mb": "pressure"
})

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"], unit='s')

# Create sensor_id
df["sensor_id"] = df["location_name"] + "_" + df["country"]

# Reduce dataset size (important)
df = df.sample(5000)

# Save cleaned file
df.to_csv("cleaned_weather.csv", index=False)

print("✅ Cleaned dataset created")