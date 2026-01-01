import React from 'react';
import { Bot, Clock, Heart, Brain } from 'lucide-react';

const AgentStatus = ({ isActive }) => {
    if (!isActive) return null;

    const agents = [
        { name: 'Planner', icon: <Bot size={18} />, action: 'Planning...' },
        { name: 'Time Agent', icon: <Clock size={18} />, action: 'Scheduling...' },
        { name: 'Focus Agent', icon: <Heart size={18} />, action: 'Balancing...' },
        { name: 'Motivation', icon: <Brain size={18} />, action: 'Encouraging...' },
    ];

    return (
        <div style={{ display: 'flex', gap: '1rem', justifyContent: 'center', marginTop: '2rem', flexWrap: 'wrap' }}>
            {agents.map((agent, index) => (
                <div
                    key={index}
                    className="glass-panel"
                    style={{
                        padding: '0.5rem 1rem',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '0.5rem',
                        fontSize: '0.9rem',
                        background: 'rgba(56, 189, 248, 0.1)',
                        borderColor: 'var(--accent-primary)',
                        animation: `pulse 2s infinite ${index * 0.5}s`
                    }}
                >
                    {agent.icon}
                    <span>{agent.action}</span>
                </div>
            ))}
            <style>{`
        @keyframes pulse {
          0% { box-shadow: 0 0 0 0 rgba(56, 189, 248, 0.4); }
          70% { box-shadow: 0 0 0 10px rgba(56, 189, 248, 0); }
          100% { box-shadow: 0 0 0 0 rgba(56, 189, 248, 0); }
        }
      `}</style>
        </div>
    );
};

export default AgentStatus;
