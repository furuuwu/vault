Typical Workflow:

Initial setup (first-time build):
* docker-compose build      # Build images based on Dockerfile(s)
* docker-compose up         # Start containers

When you modify the Dockerfile or dependencies:
* docker-compose build      # Rebuild the images
* docker-compose up         # Start the containers

When you just want to start the containers after the images are built:
* docker-compose up         # This will use existing images and start the containers


Commands:

docker build:
* Rerun this command when you modify the Dockerfile or files that the image depends on (e.g., adding new code, installing new packages).
* After you build an image, you don't need to rerun docker build unless you change the Dockerfile or the files inside the image.

docker run:
* Rerun this command when you want to create a new container based on the image.
* You might rerun it after making changes to the code, but only if you want to start a fresh container.
* If you stop or remove the container, you will need to run docker run again to recreate the container.

docker-compose up:
* Use this to start the containers. If you haven't built the images yet, it will build and start them in one go. Use docker-compose up --build if you want to ensure that any changes to the Dockerfile are reflected.

docker-compose build: 
* Use it when you know you need to rebuild the images (after making changes to Dockerfiles, dependencies, etc.) but do not want to start the containers yet. You may want to do this if you're making multiple changes and want to ensure the images are up to date before starting the containers.