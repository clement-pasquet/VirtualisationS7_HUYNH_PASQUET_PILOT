
# Projet : Application en microservices avec Docker

## Objectif

Vous allez développer une application web composée de plusieurs services conteneurisés. Ce projet en groupe vise à vous faire comprendre comment créer, containeriser, et orchestrer des services avec **Docker** et **Docker Compose**. Vous serez également amené(e) à gérer les interactions entre les différents services et à fournir une documentation complète.

---

## Description du projet

Votre application devra comporter les éléments suivants :

1. **Un backend (API)** :

   - Une **API REST** permettant de gérer des données **(exemple : gestion des utilisateurs, des produits ou des tâches)**.
   - Connexion à une base de données pour stocker les informations.

2. **Une base de données** :
   
   - Une base de données relationnelle **(MySQL, PostgreSQL)** ou **NoSQL (MongoDB)** pour gérer les données.

3. **Un frontend** :
   
   - Une interface utilisateur simple, interagissant avec l'**API** pour afficher, ajouter, ou modifier des données.

4. **Orchestration** :
   
   - Utilisation de **Docker Compose** pour orchestrer tous les services de l'application.

---

## Contraintes du projet

1. **En groupe** : Ce projet doit être réalisé en groupe.
2. **Technologies imposées** :
   
   - Backend : **Python (Flask ou FastAPI)** ou **Node.js (Express.js)**.
   - Base de données : **MySQL**, **PostgreSQL**, ou **MongoDB**.
   - Frontend : **HTML/CSS/JavaScript ou un framework (React, Vue.js)**.

3. **Docker** :

   - Chaque service doit être conteneurisé avec un `Dockerfile` spécifique.
   - L'ensemble de l'application doit être orchestré avec `docker-compose.yml`.
   - Chaque service doit implémenter un endpoint `/health` et un `healthcheck` dans Docker Compose.
   - Créer un réseau personnalisé pour permettre la communication entre les services.

4. **Fonctionnalités minimales** :

   - **Backend :** Au moins **3** endpoints **(POST, GET, DELETE)**.
   - **Frontend :** Une interface utilisateur capable d’interagir avec les endpoints du backend.

5. **Respect des bonnes pratiques** :

   - Code clair et organisé avec des commentaires.
   - Utilisation de variables d’environnement pour les configurations sensibles (exemple : **mots de passe**, **connexions**).

6. **Deadline** : Le projet doit être remis au plus tard le **Dimanche 21 décembre 2025, à 23h59**.

---

## Structure proposée du projet

Voici une structure suggérée pour organiser votre projet :

```
project/
│
├── backend/
│   ├── app/              # Code source du backend
│   ├── Dockerfile        # Conteneurisation du backend
│   └── requirements.txt  # Dépendances (si Python)
│
├── frontend/
│   ├── src/              # Code source du frontend
│   └── Dockerfile        # Conteneurisation du frontend
│
├── database/
│   └── Dockerfile        # Conteneurisation de la base de données
│
├── docker-compose.yml    # Orchestration des services
└── README.md             # Documentation du projet
```

---

## Étapes de réalisation

### 1. Planification

- Choisissez le thème de votre application **(par exemple : gestion de tâches, gestion d'utilisateurs, e-commerce, etc.)**.
- Définissez les fonctionnalités principales.

### 2. Développement du backend

- Implémentez une **API REST** avec les fonctionnalités suivantes :

  - **POST** : Ajouter des données.
  - **GET** : Récupérer des données.
  - **DELETE** : Supprimer des données.

- Ajoutez une connexion à la base de données pour stocker et gérer les données.

### 3. Développement du frontend

- Créez une interface utilisateur qui permet d’interagir avec l’**API**.
- Implémentez au moins :

  - Un formulaire pour ajouter des données.
  - Une liste affichant les données récupérées depuis l'**API**.

### 4. Conteneurisation avec Docker

- Écrivez un `Dockerfile` pour chaque service **(backend, frontend, base de données)**.
- Testez chaque service indépendamment dans un conteneur Docker.

### 5. Orchestration avec Docker Compose

- Configurez un **réseau Docker personnalisé** pour permettre aux conteneurs de communiquer entre eux.
- Implémentez des **health checks** pour chaque service (endpoint `/health` + configuration `healthcheck`).
- Testez l'interaction entre les différents services.
- Vérifiez que tous les services passent au statut `(healthy)` avec `docker compose ps`.

### 6. Documentation

- Rédigez un fichier `README.md` détaillant :

  - Les prérequis pour exécuter le projet.
  - Les étapes pour exécuter l'application.
  - La liste des endpoints de l'**API** (y compris `/health`).
  - Les fonctionnalités de l'interface utilisateur.
  - La configuration du réseau Docker et des health checks.

---

## Contraintes supplémentaires

- Les variables sensibles (comme les mots de passe) doivent être configurées dans un fichier `.env` et non dans le code source.
- La documentation doit inclure des captures d’écran ou des exemples d’exécution.

---

## Instructions pour tester l’application

### 1. Pré-requis

- Assurez-vous d'avoir **Docker** et **Docker Compose** installés sur votre machine.

### 2. Étapes pour exécuter le projet

1. Clonez le projet :

   ```bash
   git clone <url-du-repo>
   cd project
   ```

2. Construisez les images **Docker** :

   ```bash
   docker-compose build
   ```

3. Lancez l’application :
   
   ```bash
   docker-compose up
   ```

4. Testez les fonctionnalités :
   
   - **Backend :** Utilisez des outils comme `curl` ou **Postman** pour tester les endpoints.
   - **Frontend :** Ouvrez votre navigateur et interagissez avec l’application.

5. Nettoyez l’environnement :
   
   ```bash
   docker-compose down
   ```

---

## Critères d’évaluation

Votre projet sera évalué selon les critères suivants :

1. **Fonctionnalité** : L'application est fonctionnelle et respecte les consignes.
2. **Conteneurisation** : Chaque service est correctement conteneurisé avec un `Dockerfile`.
3. **Orchestration** : Les services fonctionnent ensemble grâce à **Docker Compose**.
4. **Documentation** : Un fichier `README.md` clair et complet est fourni.
5. **Qualité du code** : Le code est organisé, commenté, et suit les bonnes pratiques.

## Livrables

Vous avez jusqu'au Dimanche 21 Décembre 2025 à 23h59 pour votre rendu complet
Le rendu se compose de deux éléments : l'ensemble de fichier contenant tout le code et un Rapport Technique au format PDF

---

## Contenu du Rapport Technique (PDF)

Ce document ne doit pas être un simple copier-coller de votre code (le code est déjà sur Git). Il doit synthétiser votre compréhension et votre démarche d'ingénieur.

**Format :** PDF, 5 à 10 pages maximum (hors annexes/captures d'écran).

Le rapport doit impérativement contenir les sections suivantes :

### 1. Architecture et Choix Techniques

- **Schéma d'architecture** montrant les interactions entre :
  - Votre machine hôte
  - Le repository Git (source du code)
  - Les services conteneurisés (flux réseaux, ports ouverts, volumes)
  
- **Justification des choix techniques** :
  - Quelle image de base Docker avez-vous choisie pour chaque service et pourquoi ? (ex: `python:3.11-slim` vs `python:3.11-alpine`)
  - Pourquoi cette base de données (MySQL, PostgreSQL, MongoDB) ?
  - Pourquoi ce framework backend (Flask, FastAPI, Express.js) ? Quels avantages par rapport aux alternatives ?

### 2. Démarche de Mise en Œuvre

- **Grandes étapes de la réalisation** :
  - Planification initiale et répartition des tâches au sein du groupe
  - Ordre de développement des services
  - Stratégie de test et d'intégration
  
- **Optimisation des images Docker** :
  - Utilisation de **Multi-stage builds** 
  
- **Configuration Docker Compose** :
  - Comment avez-vous configuré la communication entre les services ?
  - Réseau personnalisé : avantages et configuration
  - Health checks : endpoints implémentés et leur utilité
  - Gestion des dépendances entre services (`depends_on`)
  
- **Logique d'orchestration** :
  - Variables d'environnement et fichier `.env`
  - Volumes et persistance des données
  - Stratégie de restart des conteneurs

### 3. Difficultés Rencontrées et Solutions Apportées

Si vous avez rencontré des problèmes techniques, décrivez-les dans cette section. Pour chaque problème, suivez ce format :

| Problème     | Description de l'erreur ou du blocage                             |
|--------------|-------------------------------------------------------------------|
| **Analyse**  | Comment avez-vous diagnostiqué la cause ? (logs, debugging, etc.) |
| **Solution** | Quelle correction avez-vous appliquée ?                           |

### 4. Usage de l'IA Générative (Transparence)

L'utilisation d'assistants IA (ChatGPT, Claude, Copilot, etc.) est **autorisée et valorisée si bien explicitée**.

- **Usage** : 
  - Avez-vous utilisé l'IA pour générer des squelettes de code ?
  - Pour expliquer une erreur obscure ?
  - Pour optimiser un script ou un Dockerfile ?
  - Pour la documentation ?
  
- **Critique** :
  - L'IA a-t-elle fait des erreurs que vous avez dû corriger ?
  - Qu'avez-vous dû adapter ou améliorer ?
  - Avez-vous validé les suggestions de l'IA ?

### 5. Démonstration (Preuves de Fonctionnement)

Cette section doit contenir des captures d'écran commentées prouvant que le TP est fonctionnel :

| Critère | Preuve requise |
|---------|----------------|
| **Services lancés** | Screenshot de `docker-compose ps` montrant tous les services en status `healthy` |
| **Réseau Docker** | Screenshot de `docker network inspect <network-name>` ou `docker network ls` |
| **Images construites** | Screenshot de `docker images` listant toutes vos images custom |
| **Backend API** | Screenshot de `curl http://localhost:PORT/health` ou d'un appel API réussi (avec Postman/Insomnia) |
| **Frontend** | Screenshot de votre navigateur affichant l'application finale fonctionnelle |
| **Logs** | Screenshot de `docker-compose logs` ou des logs d'un service spécifique en cas de débogage |

---

**Good Luck** 🚀

---