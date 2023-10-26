# Use an official Nginx runtime as the base image
FROM nginx:1.25.3

# Copy your Nginx configuration file to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Create a directory for your Django static files
RUN mkdir -p /usr/share/nginx/html/static

# Copy your Django static files from src/static to the appropriate location in the container
COPY src/static /usr/share/nginx/html/static
