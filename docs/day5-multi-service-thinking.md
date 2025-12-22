Day 5 – Multi-Service Thinking and Dependencies

In this exercise, we ran two containers with different roles. The web container acted as the producer, serving the application, while the client container acted as the consumer, which depended on the web service to function correctly.

Both containers were connected to the same Docker network, which allowed them to communicate using the service (container) name and the exposed port. Docker’s internal DNS resolved the service name to the correct container IP.

When the web service was stopped, the consumer was unable to access it. This demonstrated that the consumer is fully dependent on the producer, and when a producer fails, the failure propagates to dependent services.

Startup order is critical in multi-service systems. If the producer service is not running before the consumer starts, the consumer will fail because its dependency is unavailable. In this case, the web service must be started before the client service.

Managing service dependencies manually is difficult and error-prone as the number of services increases. Failures, restarts, and startup order become hard to control. This is why orchestration tools exist — they automatically manage service lifecycles, dependencies, restarts, and recovery at scale.
