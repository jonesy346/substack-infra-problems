"""
Question:

Write a script using the Docker SDK that launches and manages a web application container connected to a database container. This is a template for a multi-container application.

Setup:
1. Install the Docker SDK: `pip install docker`
2. Open Docker Desktop and ensure it's running.
3. If you hit container or network conflict errors on re-runs, clean up stale resources:
    docker container prune
    docker network prune

Note: Here we use Redis as a simple in-memory data store and Nginx as a web server for demonstration purposes.
"""

import docker

client = docker.from_env()

# 1. Create a network for the containers to communicate
try:
    network = client.networks.create("sample-app-network", driver="bridge")
    print(f"Network '{network.name}' created.")
except docker.errors.APIError as e:
    print(f"Network already exists or error: {e}")
    network = client.networks.get("sample-app-network") # Get existing network


redis_container = None
web_container = None

try:
    # network + container setup
    # 2. Run the Redis container

    redis_container = client.containers.run(
        "redis:alpine",
        name="redis",
        detach=True,
        network=network.name,
    )
    print(f"Redis container '{redis_container.name}' started.")

    # 3. Run the web application container (assuming you have a 'web_image' built)
    # You would first build your application image programmatically or via CLI
    # web_image = client.images.build(path=".", tag="my-web-app")

    web_container = client.containers.run(
        "nginx", # Replace with your image name
        name="web",
        detach=True,
        ports={'80/tcp': 8080},
        network=network.name
    )
    print(f"Web container '{web_container.name}' started.")

    # Monitor containers

    containers = client.containers.list()
    for container in containers:
        print(f"Container: {container.name}, Status: {container.status}")

    input("Press Enter to stop containers...")

except docker.errors.APIError as e:
    print(f"Error starting containers: {e}")

finally:
    web_container.stop()
    web_container.remove()
    redis_container.stop()
    redis_container.remove()
    network.remove()
    print("Cleaned up containers and network.")
