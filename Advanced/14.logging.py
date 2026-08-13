"""
Use logging instead of print() for professional scripts. 
Python docs describe logging as a way to track events that happen when software runs, with levels like DEBUG, INFO, WARNING, ERROR, and CRITICAL.

DevOps use cases:

Log automation script activity
Log backup success or failure
Log API errors
Log deployment steps
Log health check results
"""
# Basic Logging
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Script started")
logging.warning("Disk space is low")
logging.error("Backup failed")

"""
Logging Levels

Common levels:

DEBUG = detailed troubleshooting
INFO = normal activity
WARNING = something unexpected but script can continue
ERROR = something failed
CRITICAL = serious failure
"""
# Add Timestamp and Format
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Backup started")
logging.warning("Disk usage above 80 percent")
logging.error("Backup failed")

# Write Logs to a File
import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Script started")
logging.info("Checking server health")
logging.error("Server web01 is down")