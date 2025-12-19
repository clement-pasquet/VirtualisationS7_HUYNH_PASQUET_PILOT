# =============================================================================
# ⚛️ Dockerfile Frontend Template - React/Vite
# Build multi-étapes pour optimiser la taille finale
# =============================================================================

# =============================================================================
# 🏗️ ÉTAPE 1: BUILD (Compilation React)
# =============================================================================

FROM node:22-alpine AS build

# Métadonnées
LABEL maintainer="votre-nom@esiea.fr"
LABEL description="Frontend React pour projet microservices ESIEA"

# Répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances (optimisation cache Docker)
COPY package*.json ./

# Installer les dépendances
# Utilisation de npm install pour générer les binaires natifs corrects pour Linux
RUN npm install

# Copier le code source
COPY . .

# TODO: Configurer l'URL de l'API au build time
ARG VITE_API_URL=http://localhost:8000
ENV VITE_API_URL=$VITE_API_URL

# Build de production
RUN npm run build

# =============================================================================
# 🌐 ÉTAPE 2: PRODUCTION (Serveur nginx)
# =============================================================================

FROM nginx:alpine

# Copier les fichiers buildés depuis l'étape précédente
COPY --from=build /app/dist /usr/share/nginx/html

# TODO: Copier votre configuration nginx personnalisée si nécessaire
# COPY nginx.conf /etc/nginx/nginx.conf

# Port d'exposition
EXPOSE 80

# =============================================================================
# 🏥 HEALTH CHECK OBLIGATOIRE
# =============================================================================
# TODO: Créer un endpoint /health dans votre app React ou nginx
HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD wget --quiet --tries=1 --spider http://localhost/ || exit 1

# Démarrage automatique de nginx
CMD ["nginx", "-g", "daemon off;"]
