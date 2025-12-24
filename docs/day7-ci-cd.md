Day 7 – CI/CD and Jenkins Pipeline

CI/CD helps teams detect problems early by automatically validating code changes through a series of enforced steps. Instead of discovering issues late in deployment or production, CI/CD pipelines fail fast and prevent broken code from progressing further.

Build and test are separate stages because they serve different purposes. The build stage verifies that the application can be packaged successfully, while the test stage verifies application behavior and correctness. Code may successfully build but still fail tests, and such code must not be allowed to progress further in the pipeline.

In this pipeline, the primary artifact is a Docker image. The image is built in a reproducible way so that the same source code always results in the same artifact, ensuring consistency across environments.

Pipelines are designed to fail fast. If any stage such as checkout, build, test, or packaging fails, the pipeline stops immediately. This enforces discipline, prevents broken code from spreading, and protects downstream systems.

In real Jenkins usage, pipelines are triggered by source code changes. Jenkins checks out the code, builds it, runs tests, packages the application into an artifact, validates the artifact, and only then allows deployment. Each stage acts as a quality gate that must pass before moving forward.
