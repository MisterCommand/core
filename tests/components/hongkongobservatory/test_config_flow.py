"""Tests for the HongKongObservatory config flow."""
from unittest.mock import patch

from hko import HKOError
import pytest

from homeassistant.components.hongkongobservatory.const import DOMAIN, CONF_LOCATION
from homeassistant.config_entries import SOURCE_USER

TEST_LOCATION = "Hong Kong Observatory"

async def test_connection_error(hass):
    """Test connection to the HKO API."""
    with patch(
        "homeassistant.components.hongkongobservatory.config_flow.hko.weather",
        side_effect=HKOError,
    ):
        result = await hass.config_entries.flow.async_init(
            DOMAIN,
            context={"source": SOURCE_USER},
            data={CONF_LOCATION: TEST_LOCATION},
        )
        assert result["errors"] == {"base": "cannot_connect"}