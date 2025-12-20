# =============================================================================
# 🐍 Dockerfile Backend - Python/FastAPI
# =============================================================================

FROM python:3.11-alpine

# Install curl for healthcheck and creating a non-root user
RUN apk add --no-cache curl && \
    adduser -D -u 1000 appuser

# Metadata
LABEL maintainer="pasquet@et.esiea.fr"
LABEL description="Backend API for Final Microservices Project"

# Set working directory
WORKDIR /app

# =============================================================================
# 📦 DEPENDENCIES
# =============================================================================

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# =============================================================================
# 📁 SOURCE CODE
# =============================================================================

COPY . .

# Change ownership to non-root user
RUN chown -R appuser:appuser /app

# =============================================================================
# 🔧 CONFIGURATION
# =============================================================================

EXPOSE 8000

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# =============================================================================
# 🏥 HEALTH CHECK
# =============================================================================
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# =============================================================================
# 🚀 START
# =============================================================================

# Switch to non-root user
USER appuser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
