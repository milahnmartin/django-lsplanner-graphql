FROM python:3.12-slim

WORKDIR /app

# Copy just the requirements file first to leverage Docker layer caching
COPY ./requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY ./src .

# Expose the port the FastAPI application runs on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
