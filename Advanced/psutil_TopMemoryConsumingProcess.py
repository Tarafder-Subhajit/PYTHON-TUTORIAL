import psutil

processes = []

for process in psutil.process_iter(['pid', 'name', 'memory_percent']):
    processes.append(process.info)

top_processes = sorted(
    processes,
    key=lambda x: x['memory_percent'],
    reverse=True
)

print("Top 5 Memory Consuming Processes:")

for process in top_processes[:5]:
    print(
        f"PID: {process['pid']}, "
        f"Name: {process['name']}, "
        f"Memory: {process['memory_percent']:.2f}%"
    )