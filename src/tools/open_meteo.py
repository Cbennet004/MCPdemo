from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional
import requests


OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"


@dataclass(frozen=True)
class OpenMeteoRequest:
    """
    Structured input for the Open-Meteo tool call (MCP-style).
    """
    latitude: float
    longitude: float
    timezone: str = "America/New_York"
    current_weather: bool = True
    timeout: int = 30


class ToolInputError(ValueError):
    """Raised when tool inputs are invalid (e.g., lat/lon out of range)."""


class ToolResponseError(RuntimeError):
    """Raised when tool response is missing expected fields."""


def _validate_request(req: OpenMeteoRequest) -> None:
    # Latitude range: -90..90
    if not (-90.0 <= req.latitude <= 90.0):
        raise ToolInputError(f"latitude out of range (-90..90): {req.latitude}")

    # Longitude range: -180.0..180.0
    if not (-180.0 <= req.longitude <= 180.0):
        raise ToolInputError(f"longitude out of range (-180..180): {req.longitude}")

    if req.timeout <= 0:
        raise ToolInputError(f"timeout must be > 0 seconds: {req.timeout}")


def fetch_open_meteo(req: OpenMeteoRequest) -> Dict[str, Any]:
    """
    MCP-style tool call:
    - Takes structured input (OpenMeteoRequest)
    - Calls external API
    - Returns structured output (dict)
    - Raises clear errors on invalid input or unexpected response
    """
    _validate_request(req)

    params = {
        "latitude": req.latitude,
        "longitude": req.longitude,
        "timezone": req.timezone,
    }
    if req.current_weather:
        params["current_weather"] = "true"

    r = requests.get(OPEN_METEO_URL, params=params, timeout=req.timeout)
    r.raise_for_status()
    payload: Dict[str, Any] = r.json()

    # Minimal response validation
    if req.current_weather and "current_weather" not in payload:
        raise ToolResponseError("Response missing 'current_weather' field")

    return payload


def get_current_weather(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Helper to safely extract current_weather block.
    """
    cw = payload.get("current_weather")
    if not isinstance(cw, dict):
        raise ToolResponseError("'current_weather' is missing or not an object")
    return cw
