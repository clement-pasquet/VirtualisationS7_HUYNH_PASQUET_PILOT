# Projet Todo Microservices

## Description

Projet d'application Todo composée de 3 services :

- **Backend** : API FastAPI (Python)
- **Frontend** : Application React
- **Database** : PostgreSQL

Le tout orchestré avec Docker Compose.

---

## Lancement de l'application

### 1. Cloner le projet

```bash
git clone <url-du-repo>
cd todo-microservices
```

### 2. Configurer l'environnement

Vérifiez et configurez les variables d'environnement :

```bash
# Vérifier le contenu du fichier .env
cat .env
```

**Variables à vérifier/modifier si nécessaire :**

```bash
# Configuration base de données
DB_HOST=db                          # Nom du service dans docker-compose
DB_USER=todo_user                   # Utilisateur PostgreSQL  
DB_NAME=todo_db                     # Nom de la base de données
DB_PORT=5432                        # Port PostgreSQL standard

# Configuration frontend
VITE_API_URL=http://192.168.56.11:8000  # URL de l'API backend

# Configuration ports (optionnel)
BACKEND_PORT=8000                   # Port du backend
FRONTEND_PORT=3000                  # Port du frontend
```

**Vérification du mot de passe :**
```bash
# Le mot de passe est dans le fichier secrets (plus sécurisé)
cat secrets/db_password
```

### 3. Construire et lancer les services

```bash
docker-compose up --build
```

### 4. Accès aux services

- **Backend (API)** : [http://localhost:8000/docs](http://localhost:8000/docs)
- **Frontend** : [http://localhost:3000](http://localhost:3000)

---