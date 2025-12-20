# Final Project: Microservices Application

A fully containerized Microservices application built for the Virtualization & Containerization course at ESIEA.

## Architecture

This project consists of 3 orchestrated services:

1.  **Backend (API)**: Python FastAPI application serving REST endpoints.
2.  **Frontend (UI)**: React Application (Vite) served via Nginx.
3.  **Database**: PostgreSQL 16 (Alpine).

## Tech Stack

*   **Docker & Docker Compose**: Containerization and Orchestration.
*   **Python 3.11 & FastAPI**: High-performance backend API.
*   **React & Vite**: Modern frontend development.
*   **PostgreSQL**: Robust relational database.
*   **Nginx**: Production-grade web server / reverse proxy.

## Starting

### Prerequisites

*   Docker Desktop installed and running.
*   Git.

### Installation & Run

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd microservices
    ```

2.  **Start the application:**
    ```bash
    docker compose up --build -d
    ```

3.  **Verify status:**
    ```bash
    docker compose ps
    ```
    *All services should report `(healthy)`.*

### Accessing the Application

| Service | URL | Description |
| :--- | :--- | :--- |
| **Frontend** | [http://localhost:3000](http://localhost:3000) | Main User Interface |
| **Backend API** | [http://localhost:8000](http://localhost:8000) | JSON REST API |
| **API Docs** | [http://localhost:8000/docs](http://localhost:8000/docs) | Interactive Swagger UI |
| **Health Check** | [http://localhost:8000/health](http://localhost:8000/health) | API Status |

## Configuration

### Environment Variables (`.env`)

The application is pre-configured for development. Key variables:

*   **DB Credentials**: `DB_USER`, `DB_NAME` (managed via `.env`).
*   **Security**: Database password is managed via **Docker Secrets** (`secrets/db_password`).
*   **Networking**: Frontend connects to Backend via `VITE_API_URL` (injected at build time).

### Docker Network

All services communicate over a custom bridge network `app_network`. 
*   internal dns: `backend`, `db`, `frontend`.

## Features Implemented

*   [x] **Full Containerization**: Custom Dockerfiles for all services.
*   [x] **Orchestration**: `docker-compose.yml` with dependency management.
*   [x] **Security**: 
    *   Backend runs as non-root user.
    *   Docker Secrets for password management.
*   [x] **Health Checks**: Implemented for all 3 services.
*   [x] **Optimization**: Multi-stage builds for Frontend and Backend.
*   [x] **Persistence**: Docker Volumes for Database stability.

## Authors

*   **HUYNH**
*   **PASQUET**
*   **PILOT**

---
*ESIEA - Virtualisation S7 - 2025*