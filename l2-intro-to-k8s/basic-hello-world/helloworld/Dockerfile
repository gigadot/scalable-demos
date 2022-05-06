FROM node:8

# Expose port 8080, which is where we'll be listening
EXPOSE 8080

# Copy our server.js into the container
COPY server.js .

# Run server.js using the node interpreter when the container boots up
CMD node server.js