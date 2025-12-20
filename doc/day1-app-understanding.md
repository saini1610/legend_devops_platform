
Day 1 – Application, Processes, and Ports Understanding

Case 1: Running the application on default port
We created a simple Flask application and started it using:

python app/app.py


By default, the application listens on port 5000, which we verified by accessing:

http://localhost:5000


The application runs as a single OS process.

Case 2: Running the application on a different port
We changed the port using an environment variable:

PORT=8000 python app/app.py


The same application instance now listens on port 8000, which we verified using:

http://localhost:8000


This demonstrates that ports can be changed without modifying code.

Case 3: Browser reload behavior
Reloading the browser does not restart the application.
It only sends additional HTTP requests to the already running process listening on that port.
The application continues running until the process is stopped.

Case 4: Multiple processes and port conflicts
When two application processes are started on different ports, both can run simultaneously.

When two processes attempt to bind to the same port, operating systems normally block this to prevent conflicts.
On Windows, the Flask development server may show multiple processes as listening due to socket reuse behavior, but only one process actually handles traffic, which is confirmed by observing logs.

This behavior is unsafe for production and is why Flask warns against using the development server in real deployments. Production environments use proper WSGI servers and container orchestration to manage ports safely.
