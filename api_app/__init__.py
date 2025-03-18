import logging
import os
from os import getenv, environ
# Import the `configure_azure_monitor()` function from the
# `azure.monitor.opentelemetry` package.
from azure.monitor.opentelemetry import configure_azure_monitor
from flask import Flask  # Import the Flask class
app = Flask(__name__)    # Create an instance of the class for our use
# Configure OpenTelemetry to use Azure Monitor with the 
# APPI_CONN_STRING environment variable.

conn_string = os.getenv("APPI_CONN_STRING", "--not found--")
print(f"Connection string: {conn_string}")
configure_azure_monitor(
    connection_string=conn_string,  # Set the connection string to the value of the APPLICATIONINSIGHTS_CONNECTION_STRING environment variable.
    logger_name=__name__,  # Set the namespace for the logger in which you would like to collect telemetry for if you are collecting logging telemetry. This is imperative so you do not collect logging telemetry from the SDK itself.
    enable_live_metrics=True,
)
logger = logging.getLogger(__name__)  # Logging telemetry will be collected from logging calls made with this logger and all of it's children loggers.
logger.setLevel(logging.INFO)

import api_app.views