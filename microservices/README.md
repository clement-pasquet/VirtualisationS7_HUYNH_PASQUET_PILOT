# Projet Final : Application Microservices

Une application microservices entièrement conteneurisée, développée pour le cours de Virtualisation & Conteneurisation à l'ESIEA.

## Architecture

Ce projet se compose de 3 services orchestrés :

1.  **Backend (API)** : Application Python FastAPI servant des endpoints REST.
2.  **Frontend (UI)** : Application React (Vite) servie via Nginx.
3.  **Base de données** : PostgreSQL 16 (Alpine).

## Stack Technique

*   **Docker & Docker Compose** : Conteneurisation et Orchestration.
*   **Python 3.11 & FastAPI** : API backend performante.
*   **React & Vite** : Développement frontend moderne.
*   **PostgreSQL** : Base de données relationnelle robuste.
*   **Nginx** : Serveur web / reverse proxy de production.

## Démarrage

### Pré-requis

*   Docker Desktop installé et en cours d'exécution.
*   Git.

### Installation & Lancement

1.  **Cloner le dépôt :**
    ```bash
    git clone <votre-url-repo>
    cd microservices
    ```

2.  **Démarrer l'application :**
    ```bash
    docker compose up --build -d
    ```

3.  **Vérifier le statut :**
    ```bash
    docker compose ps
    ```
    *Tous les services doivent indiquer `(healthy)`.*

### Accéder à l'Application

| Service | URL | Description |
| :--- | :--- | :--- |
| **Frontend** | [http://localhost:3000](http://localhost:3000) | Interface Utilisateur Principale |
| **Backend API** | [http://localhost:8000](http://localhost:8000) | API REST JSON |
| **API Docs** | [http://localhost:8000/docs](http://localhost:8000/docs) | Swagger UI Interactif |
| **Health Check** | [http://localhost:8000/health](http://localhost:8000/health) | Statut de l'API |

## Endpoints API

| Méthode | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/tasks` | Récupérer toutes les tâches |
| `POST` | `/tasks` | Créer une nouvelle tâche (body JSON requis) |
| `DELETE` | `/tasks/{id}` | Supprimer une tâche par ID |
| `GET` | `/health` | Vérifier le statut de santé de l'API |

## Captures d'écran

![5.png](..\assets\5.png)
> *Interface principale montrant la liste des tâches et le formulaire d'ajout.*

## Dépannage

**Problèmes Courants :**

1.  **Échec de connexion à la Base de données :**
    *   Assurez-vous que le service `db` est healthy : `docker compose ps`
    *   Vérifiez les logs : `docker compose logs db`
    *   Vérifiez les secrets : Assurez-vous que `secrets/db_password` existe.

2.  **Erreur de communication Frontend/Backend :**
    *   Vérifiez la console du navigateur (F12) pour les erreurs réseau.
    *   Assurez-vous que `VITE_API_URL` est correct (doit être `http://localhost:8000`).
    *   Vérifiez que le CORS est activé (logs Backend).

## Exemples

**Tester l'API avec Curl :**

```bash
# 1. Vérifier la santé (Health Check)
curl http://localhost:8000/health

# 2. Créer une Tâche
curl -X POST "http://localhost:8000/tasks" \
     -H "Content-Type: application/json" \
     -d '{"title": "Tâche Test", "description": "Créé via Curl"}'

# 3. Lister les Tâches
curl http://localhost:8000/tasks
```

## Configuration

### Variables d'Environnement (`.env`)

L'application est pré-configurée pour le développement. Variables clés :

*   **Identifiants DB** : `DB_USER`, `DB_NAME` (géré via `.env`).
*   **Sécurité** : Le mot de passe de la base de données est géré via **Docker Secrets** (`secrets/db_password`).
*   **Réseau** : Le Frontend se connecte au Backend via `VITE_API_URL` (injecté au moment du build).

### Réseau Docker

Tous les services communiquent sur un réseau bridge personnalisé `app_network`.
*   DNS internes : `backend`, `db`, `frontend`.

## Fonctionnalités Implémentées

*   [x] **Conteneurisation Complète** : Dockerfiles personnalisés pour tous les services.
*   [x] **Orchestration** : `docker-compose.yml` avec gestion des dépendances.
*   [x] **Sécurité** :
    *   Backend exécuté en tant qu'utilisateur non-root.
    *   Docker Secrets pour la gestion des mots de passe.
*   [x] **Health Checks** : Implémentés pour les 3 services.
*   [x] **Optimisation** : Multi-stage builds pour le Frontend et le Backend.
*   [x] **Persistance** : Volumes Docker pour la stabilité de la base de données.

Total : 65/65 items validés

## Auteurs

*   **HUYNH**
*   **PASQUET**
*   **PILOT**

---
*ESIEA - Virtualisation S7 - 2025*