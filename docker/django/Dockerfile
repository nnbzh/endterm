# Use the official Python image
FROM python:3.9

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the poetry.lock and pyproject.toml files
COPY poetry.lock pyproject.toml /app/

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the application code
COPY . /app/

# Expose port 8000
EXPOSE 8000