# Use Python 3.12 with slim Debian Bookworm
FROM python:3.12-slim-bookworm

# Set the working directory
WORKDIR /app

# Copy the requirements.txt and install dependencies
COPY requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables (optional, for debugging or other configurations)
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose the port on which the app will run
EXPOSE 5000

# Run the app using Gunicorn on port 5000, binding to all interfaces
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
