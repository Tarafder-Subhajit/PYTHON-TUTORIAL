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
cpu_usage = psutil.cpu_percent(interval=1)
#cpu_percent() returns CPU utilization as a percentage, and the psutil docs show it being used with interval=1 to measure CPU usage over one second.
print(f"CPU Usage: {cpu_usage}%")
print("Logical CPUs:", psutil.cpu_count())
print("Physical CPUs:", psutil.cpu_count(logical=False))
# cpu_count() gives CPU count, and cpu_count(logical=False) gives physical core count when available.

# 2. Memory Monitoring

# virtual_memory() returns a named tuple with memory statistics, including total, available, used, and percentage used.
memory = psutil.virtual_memory()
print(f"Total Memory: {memory.total}")
print(f"Available Memory: {memory.available}")
print(f"Used Memory: {memory.used}")
print(f"Memory Usage: {memory.percent}%")

# swap_memory() returns swap total, used, free, and percent usage.
swap = psutil.swap_memory()
print(f"Swap Total: {swap.total}")
print(f"Swap Used: {swap.used}")
print(f"Swap Usage: {swap.percent}%")

# 3. Disk Monitoring: Disk usage monitoring is important because full disks can crash applications, databases, CI/CD tools, and Kubernetes nodes.

# disk_usage() returns total, used, free, and percentage usage for a given path.
disk = psutil.disk_usage('/')
print(f"Total Disk Space: {disk.total}")
print(f"Used Disk Space: {disk.used}")
print(f"Free Disk Space: {disk.free}")
print(f"Disk Usage: {disk.percent}%")

# disk_io_counters() provides disk input/output statistics such as read count, write count, read bytes, and write bytes.
disk_io = psutil.disk_io_counters()
print(f"Disk Read Count: {disk_io.read_count}")
print(f"Disk Write Count: {disk_io.write_count}")
print(f"Disk Read Bytes: {disk_io.read_bytes}")
print(f"Disk Write Bytes: {disk_io.write_bytes}")

# 4. Network Monitoring: Network monitoring helps detect high traffic, connectivity issues, and interface-level problems.

# net_io_counters() provides network input/output statistics such as bytes sent, bytes received, packets sent, and packets received.
net_io = psutil.net_io_counters()
print(f"Bytes Sent: {net_io.bytes_sent}")
print(f"Bytes Received: {net_io.bytes_recv}")
print(f"Packets Sent: {net_io.packets_sent}")
print(f"Packets Received: {net_io.packets_recv}")

#net_if_addrs() returns network interface addresses, and net_if_stats() returns interface status information such as whether the interface is up.
interfaces = psutil.net_if_addrs()
for interface, addresses in interfaces.items():
    print(interface)
    for address in addresses:
        print(address.address)



# 5. Process Monitoring: Process monitoring is crucial for identifying resource-intensive processes, memory leaks, and potential security threats.

# process_iter() is used to iterate over running processes and retrieve process information.
for process in psutil.process_iter(['pid', 'name', 'status']):
    print(process.info)

# Process() allows you to work with a specific process by PID and retrieve details like name, status, CPU usage, and memory information.
pid = 1234
process = psutil.Process(pid)

print("Name:", process.name())
print("Status:", process.status())
print("CPU Usage:", process.cpu_percent(interval=1))
print("Memory Info:", process.memory_info())

# Kill a process 
# process.terminate() sends a termination signal to the process, while process.kill() forcefully kills the process.
pid = 1234
process = psutil.Process(pid)
process.kill()

# 6. System Boot Time: psutil.boot_time() returns the system boot time as a timestamp, which can be converted to a human-readable format using the datetime module.
import datetime
boot_time = psutil.boot_time()
boot_time_human = datetime.datetime.fromtimestamp(boot_time)
print(f"System Boot Time: {boot_time_human}")
