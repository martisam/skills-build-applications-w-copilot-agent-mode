import React, { useState, useEffect } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const codespaceNameEnv = process.env.REACT_APP_CODESPACE_NAME;
        
        let apiUrl;
        if (codespaceNameEnv) {
          apiUrl = `https://${codespaceNameEnv}-8000.app.github.dev/api/workouts/`;
        } else {
          apiUrl = `http://localhost:8000/api/workouts/`;
        }

        console.log('Fetching Workouts from:', apiUrl);
        console.log('REACT_APP_CODESPACE_NAME:', codespaceNameEnv);

        const response = await fetch(apiUrl);
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Workouts data received:', data);

        const workoutsList = data.results ? data.results : Array.isArray(data) ? data : [];
        console.log('Processed workouts list:', workoutsList);
        
        setWorkouts(workoutsList);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) {
    return (
      <div className="text-center mt-5">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-3 text-muted">Loading workouts...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="alert alert-danger alert-dismissible fade show" role="alert">
        <strong>Error!</strong> {error}
        <button type="button" className="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
    );
  }

  const getDifficultyColor = (difficulty) => {
    switch (difficulty?.toLowerCase()) {
      case 'beginner':
        return 'bg-success';
      case 'intermediate':
        return 'bg-warning';
      case 'advanced':
        return 'bg-danger';
      default:
        return 'bg-secondary';
    }
  };

  const getCategoryColor = (category) => {
    const colors = {
      cardio: 'bg-info',
      strength: 'bg-primary',
      flexibility: 'bg-success',
      hiit: 'bg-danger',
      sports: 'bg-warning',
      default: 'bg-secondary'
    };
    return colors[category?.toLowerCase()] || colors.default;
  };

  return (
    <div className="workouts-container">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>💪 Workouts</h2>
        <span className="badge bg-primary">{workouts.length} workouts</span>
      </div>

      {workouts.length === 0 ? (
        <div className="alert alert-warning" role="alert">
          <strong>No workouts found</strong> - Check if the API is running and populated with test data.
        </div>
      ) : (
        <div className="row g-4">
          {workouts.map((workout) => (
            <div key={workout.id} className="col-md-6 col-lg-4">
              <div className="card h-100 shadow-sm">
                <div className="card-header bg-light">
                  <h5 className="card-title mb-0">{workout.title}</h5>
                </div>
                <div className="card-body">
                  <p className="card-text text-muted">{workout.description}</p>
                  
                  <div className="workout-details mb-3">
                    <div className="mb-3">
                      <small className="text-muted d-block mb-2">Category & Difficulty</small>
                      <span className={`workout-badge ${getCategoryColor(workout.category)}`}>
                        {workout.category}
                      </span>
                      <span className={`badge ${getDifficultyColor(workout.difficulty)}`}>
                        {workout.difficulty}
                      </span>
                    </div>

                    <div className="row g-2">
                      <div className="col-6">
                        <small className="text-muted d-block">Duration</small>
                        <strong>{workout.estimated_duration_minutes}</strong> min
                      </div>
                      <div className="col-6">
                        <small className="text-muted d-block">Calories</small>
                        <strong>{workout.estimated_calories}</strong> cal
                      </div>
                    </div>
                  </div>

                  <div className="mb-3">
                    <small className="text-muted d-block mb-2">Equipment</small>
                    <span className="badge bg-light text-dark">
                      {workout.equipment_needed}
                    </span>
                  </div>

                  <div className="instructions bg-light p-2 rounded">
                    <small className="text-muted d-block fw-bold mb-1">Instructions</small>
                    <small className="text-dark">{workout.instructions}</small>
                  </div>
                </div>
                <div className="card-footer bg-light">
                  <button className="btn btn-sm btn-outline-primary w-100">
                    Start Workout
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Workouts;
