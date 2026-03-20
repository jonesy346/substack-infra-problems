"""
Question:

Build a small program using the Docker SDK that continuously lists running containers, their status, and resource usage (CPU and memory). This is a great template for a container monitoring dashboard.

Setup:
1. Install the Docker SDK: `pip install docker`
2. Open Docker Desktop and ensure it's running.
3. Spin up a test container to see the monitoring in action: `docker run -d --name test-container nginx`
"""

import docker
import time

client = docker.from_env()

def get_cpu_percent(stats):
    cpu_delta = stats['cpu_stats']['cpu_usage']['total_usage'] - \
                stats['precpu_stats']['cpu_usage']['total_usage']
    system_delta = stats['cpu_stats']['system_cpu_usage'] - \
                   stats['precpu_stats']['system_cpu_usage']
    num_cpus = stats['cpu_stats']['online_cpus']
    return (cpu_delta / system_delta) * num_cpus * 100.0

def get_memory_mb(stats):
    return stats['memory_stats']['usage'] / (1024 * 1024)

def monitor(interval=5):
    while True:
        containers = client.containers.list()
        print(f"\nRunning containers: {len(containers)}")
        for container in containers:
            stats = container.stats(stream=False)
            cpu = get_cpu_percent(stats)
            memory = get_memory_mb(stats)
            print(f"{container.name} - Status: {container.status} - CPU: {cpu:.2f}% - Memory: {memory:.2f} MB")
        time.sleep(interval)

monitor()
