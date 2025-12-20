Day 2 – Docker Fundamentals

A Docker container runs an application as a single main process inside an isolated environment. The container lifecycle is directly tied to the lifecycle of that process.

When a container is stopped, Docker terminates the main process running inside it. Once the process exits, the container also stops. This makes containers lightweight and process-driven rather than virtual machines.

In Docker port mapping, the host port is the port exposed on the host machine, while the container port is the port on which the application listens inside the container.

For example:

docker run -p 8000:5000 legend-flask-app


In this case:

The host listens on port 8000

The application inside the container listens on port 5000

Docker forwards traffic from host port 8000 to container port 5000

The EXPOSE 5000 instruction in the Dockerfile documents the port used by the application inside the container. It does not publish the port by itself, but it indicates which port the containerized application expects to use.

Docker resolves the port and process confusion observed on Day 1 by isolating the application inside a container and explicitly controlling how host ports map to container ports. This makes application behavior predictable and repeatable.
