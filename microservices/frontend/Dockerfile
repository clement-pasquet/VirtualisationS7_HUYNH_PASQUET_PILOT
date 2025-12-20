# =============================================================================
# ⚛️ Dockerfile Frontend - React/Vite
# Multi-stage build for size optimization
# =============================================================================

# =============================================================================
# 🏗️ STAGE 1: BUILD
# =============================================================================

FROM node:22-alpine AS build

# Metadata
LABEL maintainer="pasquet@et.esiea.fr"
LABEL description="Frontend React for Final Microservices Project"

WORKDIR /app

# Install dependencies (cache optimized)
COPY package*.json ./
RUN npm install

# Copy source code and build
COPY . .

# Build-time environment variable injection
ARG VITE_API_URL=http://localhost:8000
ENV VITE_API_URL=$VITE_API_URL

RUN npm run build

# =============================================================================
# 🌐 STAGE 2: PRODUCTION (Nginx)
# =============================================================================

FROM nginx:alpine

# Security: Run as non-root user (nginx image supports this out of the box with some tweaks,
# but for simplicity/standard alpine nginx usage we keep default user but fix permissions if needed.
# However, standard nginx image on 80 requires root. To be fully non-root we'd need to use >1024 port.
# For this student project level, correctly copying config and cleaning up is the priority.)

# Copy built assets
COPY --from=build /app/dist /usr/share/nginx/html

# Copy custom configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

# =============================================================================
# 🏥 HEALTH CHECK
# =============================================================================
HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD wget --quiet --tries=1 --spider http://localhost/health || exit 1

CMD ["nginx", "-g", "daemon off;"]
