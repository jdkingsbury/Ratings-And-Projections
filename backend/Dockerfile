FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy the requirements file and install any needed packages
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Copy the rest of the application code
COPY . /app/

# Expose port
EXPOSE 8000

# Set the command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

