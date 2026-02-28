# Tool Contract — Open-Meteo (MCP-style)

## Purpose
This tool provides a **standard, predictable interface** for calling an external system (Open-Meteo API).

## Inputs
A single structured request object:
- `latitude` (float): required
- `longitude` (float): required
- `timezone` (str): optional (default `"America/New_York"`)
- `current_weather` (bool): optional (default `True`)
- `timeout` (int): optional (default `30`)

## Output
A Python `dict` (parsed JSON) containing:
- `latitude`, `longitude`, `timezone` (may vary by API)
- `current_weather` (if requested and available)

## Errors
- Raises `ValueError` for invalid latitude/longitude ranges
- Raises `requests.HTTPError` for non-200 API responses
- Raises `requests.Timeout` if the request exceeds `timeout`

## Example
```python
from src.tools.open_meteo import OpenMeteoRequest, fetch_open_meteo

req = OpenMeteoRequest(latitude=40.8259, longitude=-74.2090)
payload = fetch_open_meteo(req)
print(payload["current_weather"])
