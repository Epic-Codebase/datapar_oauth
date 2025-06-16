# Use a lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /bidesigner

# Install system dependencies for PostgreSQL, build tools, and WeasyPrint libraries
RUN apt-get update && apt-get install -y \
    libpq-dev gcc curl \
    libcairo2 \
    libpango1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info \
    libglib2.0-0 \
  && rm -rf /var/lib/apt/lists/*

# Install Poetry and add it to the PATH
ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    poetry --version  # Verify Poetry installation

# Copy only the dependency files to leverage Docker caching
COPY pyproject.toml poetry.lock ./

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

# Copy the entire Django project
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Expose the default Gunicorn port
EXPOSE 8000

# Collect static files
RUN mkdir -p /staticfiles && chown -R 1000:1000 /staticfiles
RUN python manage.py collectstatic --noinput

# Command to run the start script
CMD ["gunicorn", "bidesigner.wsgi:application", "--bind", "0.0.0.0:8000"]
