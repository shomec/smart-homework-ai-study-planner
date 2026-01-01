import React from 'react';

const WeeklyCalendar = ({ plan }) => {
    if (!plan) return null;

    // Since CrewAI output is text, we'll format it as a nice document
    // In a real app, we'd enforce JSON schema to render a grid.

    return (
        <div className="glass-panel" style={{ padding: '2rem', marginTop: '2rem' }}>
            <h2 className="heading-gradient" style={{ marginBottom: '1.5rem', textAlign: 'center' }}>Your Personalized Study Plan</h2>

            <div
                style={{
                    whiteSpace: 'pre-wrap',
                    lineHeight: '1.8',
                    background: 'rgba(0,0,0,0.2)',
                    padding: '1.5rem',
                    borderRadius: 'var(--radius-md)'
                }}
            >
                {plan}
            </div>

            <div style={{ marginTop: '2rem', textAlign: 'center' }}>
                <button className="btn-primary" onClick={() => window.print()}>
                    Print / Save PDF
                </button>
            </div>
        </div>
    );
};

export default WeeklyCalendar;
