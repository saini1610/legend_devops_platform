Day 3 – Environment Variables and Docker Volumes 

Containers are stateless by default because any data written inside the container filesystem is lost when the container stops or is recreated. Containers are designed to be disposable and ephemeral.

Environment variables are used to change application configuration at runtime without modifying application code or rebuilding the Docker image. For example, our Flask application listens on port 5000 by default, but we can change its behavior at runtime using:

docker run -e PORT=8000 -p 8000:8000 legend-flask-app


This changes the application’s listening port without changing the source code or Dockerfile.

When a container stops, all data written inside the container filesystem is lost. To persist data beyond the container lifecycle, Docker volumes are used. Volumes are managed by Docker and exist independently of containers.

By mounting a volume into the container, application data can persist even when the container stops, restarts, or is recreated. This separates the lifecycle of the application from the lifecycle of the data.

This is critical for production systems because logs, application state, and other important data must persist across restarts and failures. Containers can be replaced, but data must survive.
