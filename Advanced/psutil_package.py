"""
# psutil (Process and System Utilities) is a cross-platform Python library used for:
#   System monitoring
#   Performance analysis
#   Process management
#   Capacity planning
#   Health checks
#   Infrastructure automation
"""

# INSTALL : pip install psutil

# Verify
import psutil
print(psutil.__version__)

"""
Common Devops Usecases :
->   Server health monitoring
->   Custom monitoring agents
->   Kubernetes node checks
->   Automated alerts
->   Capacity analysis
->   Process monitoring
->   Incident troubleshooting
->  Infrastructure reporting
"""
# 1. CPU Monitoring
cpu_usage = psutil.cpu_percent(interval=1) #cpu_percent() returns CPU utilization as a percentage, and the psutil docs show it being used with interval=1 to measure CPU usage over one second.
print(f"CPU Usage: {cpu_usage}%")



