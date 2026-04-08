# Builder stage
FROM python:3.9-slim as builder

WORKDIR /build

# Install build essentials
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt .

# Build wheels
RUN pip wheel --no-cache-dir --timeout=1000 --wheel-dir /build/wheels -r requirements.txt

# Final stage
FROM python:3.9-slim

WORKDIR /app

# Copy pre-built wheels from builder
COPY --from=builder /build/wheels /wheels

# Install wheels (no build needed)
COPY backend/requirements.txt .
RUN pip install --no-cache-dir --no-index --find-links /wheels -r requirements.txt && rm -rf /wheels

COPY backend/ .

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
