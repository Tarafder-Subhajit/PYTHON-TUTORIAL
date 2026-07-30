import psutil

service_name = "nginx"
is_running = False

for process in psutil.process_iter(['name']):
    if process.info['name'] == service_name:
        is_running = True
        break

if is_running:
    print("Nginx is running")
else:
    print("Nginx is not running")