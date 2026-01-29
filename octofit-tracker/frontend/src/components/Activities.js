import React, { useState, useEffect } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchActivities = async () => {
      try {
        const codespaceNameEnv = process.env.REACT_APP_CODESPACE_NAME;
        
        let apiUrl;
        if (codespaceNameEnv) {
          apiUrl = `https://${codespaceNameEnv}-8000.app.github.dev/api/activities/`;
        } else {
          apiUrl = `http://localhost:8000/api/activities/`;
        }

        console.log('Fetching Activities from:', apiUrl);
        console.log('REACT_APP_CODESPACE_NAME:', codespaceNameEnv);

        const response = await fetch(apiUrl);
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Activities data received:', data);

        const activitiesList = data.results ? data.results : Array.isArray(data) ? data : [];
        console.log('Processed activities list:', activitiesList);
        
        setActivities(activitiesList);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching activities:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchActivities();
  }, []);

  if (loading) {
    return (
      <div className="text-center mt-5">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-3 text-muted">Loading activities...</p>
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

  const getIntensityColor = (intensity) => {
    switch (intensity?.toLowerCase()) {
      case 'low':
        return 'bg-success';
      case 'moderate':
        return 'bg-warning';
      case 'high':
        return 'bg-danger';
      default:
        return 'bg-secondary';
    }
  };

  return (
    <div className="activities-container">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>📊 Activities</h2>
        <span className="badge bg-primary">{activities.length} activities</span>
      </div>

      {activities.length === 0 ? (
        <div className="alert alert-warning" role="alert">
          <strong>No activities found</strong> - Check if the API is running and populated with test data.
        </div>
      ) : (
        <div className="row g-4">
          {activities.map((activity) => (
            <div key={activity.id} className="col-md-6 col-lg-4">
              <div className="card h-100 shadow-sm">
                <div className="card-header bg-light">
                  <h5 className="card-title mb-0">{activity.title}</h5>
                </div>
                <div className="card-body">
                  <p className="card-text text-muted">{activity.description}</p>
                  
                  <div className="activity-details">
                    <div className="row g-2">
                      <div className="col-6">
                        <small className="text-muted d-block">Type</small>
                        <span className="badge bg-info">{activity.activity_type}</span>
                      </div>
                      <div className="col-6">
                        <small className="text-muted d-block">Duration</small>
                        <strong>{activity.duration_minutes}</strong> min
                      </div>
                      <div className="col-6">
                        <small className="text-muted d-block">Calories</small>
                        <strong>{activity.calories_burned}</strong> cal
                      </div>
                      <div className="col-6">
                        <small className="text-muted d-block">Distance</small>
                        <strong>{activity.distance_km}</strong> km
                      </div>
                      <div className="col-6">
                        <small className="text-muted d-block">Intensity</small>
                        <span className={`badge ${getIntensityColor(activity.intensity)}`}>
                          {activity.intensity}
                        </span>
                      </div>
                      <div className="col-6">
                        <small className="text-muted d-block">Location</small>
                        <span className="badge bg-light text-dark">{activity.location}</span>
                      </div>
                    </div>
                  </div>
                </div>
                <div className="card-footer bg-light text-muted">
                  <small>
                    📅 {new Date(activity.activity_date).toLocaleDateString('en-US', {
                      weekday: 'short',
                      year: 'numeric',
                      month: 'short',
                      day: 'numeric'
                    })}
                  </small>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Activities;
