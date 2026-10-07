# Build notes

This build deliberately removes the fragile frontend/backend split used previously. FastAPI serves the same application and API from one Docker service, reducing deployment failure points.

All primary navigation paths have a functional destination. Buttons either change application state, call an API endpoint, persist progress, or navigate to another working module.
