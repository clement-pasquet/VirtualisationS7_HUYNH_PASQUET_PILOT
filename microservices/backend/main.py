# =============================================================================
# 🐍 Backend API - Microservices Project
# =============================================================================

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import time
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
from typing import List, Optional

# =============================================================================
# 🚀 INITIALISATION DE L'APPLICATION
# =============================================================================

app = FastAPI(
    title="Final  Microservices API",
    description="API REST du projet final virtualisation",
    version="1.0.0"
)

# =============================================================================
# 🌐 CONFIGURATION CORS
# =============================================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Pour le développement, autoriser tout
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================================================================
# 📊 MODÈLES DE DONNÉES (PYDANTIC)
# =============================================================================

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    created_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# =============================================================================
# 🗃️ GESTION BASE DE DONNÉES
# =============================================================================

def get_db_connection():
    """
    Établit une connexion à la base de données PostgreSQL avec réessais
    """
    retries = 5
    while retries > 0:
        try:
            # Récupération du chemin du secret via variable d'environnement (Conforme INDICATIONS.md)
            secret_path = os.getenv("DB_PASSWORD_FILE", "/run/secrets/db_password")
            
            try:
                with open(secret_path, "r") as f:
                    password = f.read().strip()
            except FileNotFoundError:
                raise Exception(f"Secret DB non trouvé à : {secret_path}")

            conn = psycopg2.connect(
                host=os.getenv("DB_HOST", "db"),
                database=os.getenv("DB_NAME", "final_project_db"),
                user=os.getenv("DB_USER", "final_project_user"),
                password=password,
                port=os.getenv("DB_PORT", "5432")
            )
            return conn
        except Exception as e:
            print(f"Erreur de connexion à la DB, nouvel essai dans 5s... ({e})")
            retries -= 1
            time.sleep(5)
    
    raise Exception("Impossible de se connecter à la base de données")



# =============================================================================
# 🏥 HEALTH CHECK
# =============================================================================

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy", "service": "backend-api"}

# =============================================================================
# 📝 ENDPOINTS TASKS
# =============================================================================

@app.get("/tasks", response_model=List[Task], tags=["Tasks"])
def read_tasks():
    """Récupérer toutes les tâches"""
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM tasks ORDER BY id DESC")
        tasks = cur.fetchall()
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

@app.post("/tasks", response_model=Task, tags=["Tasks"], status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    """Créer une nouvelle tâche"""
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute(
            "INSERT INTO tasks (title, description) VALUES (%s, %s) RETURNING *",
            (task.title, task.description)
        )
        new_task = cur.fetchone()
        conn.commit()
        return new_task
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

@app.delete("/tasks/{task_id}", tags=["Tasks"], status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    """Supprimer une tâche"""
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM tasks WHERE id = %s RETURNING id", (task_id,))
        deleted_id = cur.fetchone()
        conn.commit()
        if not deleted_id:
            raise HTTPException(status_code=404, detail="Tâche non trouvée")
        return
    except HTTPException:
        raise
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

# =============================================================================
# 🚀 POINT D'ENTRÉE
# =============================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
