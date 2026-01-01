import React, { useState } from 'react';

const InputForm = ({ onSubmit, loading }) => {
    const [assignments, setAssignments] = useState('');
    const [hours, setHours] = useState(2);

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({ assignments, hours_per_day: parseFloat(hours) });
    };

    return (
        <div className="glass-panel" style={{ padding: '2rem', maxWidth: '600px', margin: '0 auto' }}>
            <h2 className="heading-gradient" style={{ marginBottom: '1.5rem' }}>Plan Your Study Week</h2>
            <form onSubmit={handleSubmit}>
                <div style={{ marginBottom: '1.5rem' }}>
                    <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: '500' }}>
                        Assignments, Tests & Deadlines
                    </label>
                    <textarea
                        className="input-field"
                        rows="5"
                        placeholder="e.g. Math test Friday, History essay Thursday..."
                        value={assignments}
                        onChange={(e) => setAssignments(e.target.value)}
                        required
                        style={{ resize: 'vertical' }}
                    />
                </div>

                <div style={{ marginBottom: '2rem' }}>
                    <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: '500' }}>
                        Daily Study Hours
                    </label>
                    <input
                        type="number"
                        className="input-field"
                        min="0.5"
                        max="12"
                        step="0.5"
                        value={hours}
                        onChange={(e) => setHours(e.target.value)}
                        required
                    />
                </div>

                <button
                    type="submit"
                    className="btn-primary"
                    style={{ width: '100%', opacity: loading ? 0.7 : 1 }}
                    disabled={loading}
                >
                    {loading ? 'AI Agents Working...' : 'Generate Plan'}
                </button>
            </form>
        </div>
    );
};

export default InputForm;
