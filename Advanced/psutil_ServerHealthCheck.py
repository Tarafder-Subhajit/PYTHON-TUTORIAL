import psutil

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 85

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print("===== Server Health Report =====")
print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")
print(f"Disk Usage: {disk}%")

if cpu > CPU_THRESHOLD:
    print("WARNING: High CPU usage")

if memory > MEMORY_THRESHOLD:
    print("WARNING: High memory usage")

if disk > DISK_THRESHOLD:
    print("WARNING: High disk usage")

if cpu <= CPU_THRESHOLD and memory <= MEMORY_THRESHOLD and disk <= DISK_THRESHOLD:
    print("System is healthy")