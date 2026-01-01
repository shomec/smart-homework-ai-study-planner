import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import InputForm from './components/InputForm';
import AgentStatus from './components/AgentStatus';
import WeeklyCalendar from './components/WeeklyCalendar';

function App() {
    const [loading, setLoading] = useState(false);
    const [plan, setPlan] = useState(null);

    const handlePlanCreate = async (data) => {
        setLoading(true);
        setPlan(null);
        try {
            // 1. Trigger Plan Creation
            const response = await fetch('http://localhost:8000/plan/create', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });
            const { plan_id } = await response.json();

            // 2. Poll for status
            const pollInterval = setInterval(async () => {
                const statusRes = await fetch(`http://localhost:8000/plan/${plan_id}`);
                const statusData = await statusRes.json();

                if (statusData.status === 'completed') {
                    clearInterval(pollInterval);
                    setPlan(statusData.result);
                    setLoading(false);
                }
            }, 2000);

        } catch (error) {
            console.error("Error creating plan:", error);
            setLoading(false);
            alert("Failed to start planning. Ensure backend is running.");
        }
    };

    return (
        <Router>
            <div className="app-container">
                <header style={{ marginBottom: '3rem', textAlign: 'center' }}>
                    <div style={{ display: 'inline-block', padding: '0.5rem 1.5rem', background: 'rgba(56, 189, 248, 0.1)', borderRadius: '50px', marginBottom: '1rem', border: '1px solid var(--accent-primary)' }}>
                        <span style={{ color: 'var(--accent-primary)', fontWeight: '600' }}>AI Powered</span>
                    </div>
                    <h1 className="heading-gradient" style={{ fontSize: '3.5rem', marginBottom: '0.5rem', letterSpacing: '-1px' }}>
                        Smart Study
                    </h1>
                    <p style={{ color: 'var(--text-secondary)', fontSize: '1.2rem' }}>
                        Your personal team of AI agents to help streamline your academic life
                    </p>
                </header>

                <main style={{ minHeight: '60vh' }}>
                    {!plan && (
                        <>
                            <InputForm onSubmit={handlePlanCreate} loading={loading} />
                            <AgentStatus isActive={loading} />
                        </>
                    )}

                    {plan && (
                        <div className="animate-fade-in">
                            <WeeklyCalendar plan={plan} />
                            <div style={{ textAlign: 'center', marginTop: '2rem' }}>
                                <button className="btn-primary" style={{ background: 'var(--bg-secondary)' }} onClick={() => setPlan(null)}>
                                    Create New Plan
                                </button>
                            </div>
                        </div>
                    )}
                </main>
            </div>
        </Router>
    );
}

export default App;
