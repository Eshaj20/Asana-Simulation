import logging

# Configure global logging format and level
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Create a named logger for the application
logger = logging.getLogger("asana-simulator")
