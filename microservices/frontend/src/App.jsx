import { useEffect, useState } from "react";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export default function App() {
    const [tasks, setTasks] = useState([]);
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [loading, setLoading] = useState(false);
    const [submitting, setSubmitting] = useState(false);
    const [error, setError] = useState("");

    // Chargement initial des tâches
    useEffect(() => {
        fetchTasks();
    }, []);

    async function fetchTasks() {
        try {
            setLoading(true);
            setError("");
            const res = await fetch(`${API_URL}/tasks`);
            if (!res.ok) throw new Error(`Erreur API (${res.status})`);
            const data = await res.json();
            setTasks(data);
        } catch (err) {
            console.error(err);
            setError("Impossible de récupérer les tâches.");
        } finally {
            setLoading(false);
        }
    }

    async function handleSubmit(e) {
        e.preventDefault();
        if (!title.trim()) return;

        try {
            setSubmitting(true);
            setError("");
            const res = await fetch(`${API_URL}/tasks`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    title: title.trim(),
                    description: description.trim() || null,
                }),
            });
            if (!res.ok) throw new Error(`Erreur API (${res.status})`);
            const newTask = await res.json();
            setTasks((prev) => [newTask, ...prev]);
            setTitle("");
            setDescription("");
        } catch (err) {
            console.error(err);
            setError("Impossible d’ajouter la tâche.");
        } finally {
            setSubmitting(false);
        }
    }

    async function handleDelete(id) {
        if (!window.confirm("Supprimer cette tâche ?")) return;

        try {
            setError("");
            const res = await fetch(`${API_URL}/tasks/${id}`, {
                method: "DELETE",
            });
            if (!res.ok && res.status !== 204) {
                throw new Error(`Erreur API (${res.status})`);
            }
            setTasks((prev) => prev.filter((t) => t.id !== id));
        } catch (err) {
            console.error(err);
            setError("Impossible de supprimer la tâche.");
        }
    }

    return (
        <div className="app-root">
            <header className="app-header">
                <h1 className="app-title">Microservices Todo App</h1>
                <p className="app-subtitle">
                    React + FastAPI + PostgreSQL + Docker
                </p>
            </header>

            <main className="app-main">
                {/* Carte : Add New Task */}
                <section className="card card-new-task">
                    <div className="card-header">
                        <div className="icon-circle">+</div>
                        <h2>Add New Task</h2>
                    </div>

                    <form className="task-form" onSubmit={handleSubmit}>
                        <input
                            className="input"
                            type="text"
                            placeholder="Task title *"
                            value={title}
                            onChange={(e) => setTitle(e.target.value)}
                            disabled={submitting}
                            required
                        />
                        <textarea
                            className="textarea"
                            placeholder="Description (optional)"
                            value={description}
                            onChange={(e) => setDescription(e.target.value)}
                            disabled={submitting}
                        />
                        <button className="btn btn-primary" type="submit" disabled={submitting}>
                            {submitting ? "Adding..." : "Add Task"}
                        </button>
                    </form>
                </section>

                {/* Liste des tâches */}
                <section className="card card-tasks">
                    <div className="tasks-header">
                        <div className="tasks-title">
                            <span className="tasks-icon" aria-hidden="true">
                                📋
                            </span>
                            <h3>
                                Tasks ({tasks.length})
                            </h3>
                        </div>
                        {loading && <span className="badge">Loading...</span>}
                    </div>

                    {error && <p className="error">{error}</p>}

                    {!loading && tasks.length === 0 && !error && (
                        <p className="empty">Aucune tâche pour l’instant.</p>
                    )}

                    <ul className="task-list">
                        {tasks.map((task) => (
                            <li key={task.id} className="task-item">
                                <div className="task-info">
                                    <h4 className="task-title">{task.title}</h4>
                                    {task.description && (
                                        <p className="task-description">{task.description}</p>
                                    )}
                                </div>
                                <button
                                    className="btn btn-danger"
                                    onClick={() => handleDelete(task.id)}
                                >
                                    🗑 Delete
                                </button>
                            </li>
                        ))}
                    </ul>
                </section>
            </main>
        </div>
    );
}
