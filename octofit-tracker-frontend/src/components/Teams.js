import React, { useState, useEffect } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const codespaceNameEnv = process.env.REACT_APP_CODESPACE_NAME;
        
        let apiUrl;
        if (codespaceNameEnv) {
          apiUrl = `https://${codespaceNameEnv}-8000.app.github.dev/api/teams/`;
        } else {
          apiUrl = `http://localhost:8000/api/teams/`;
        }

        console.log('Fetching Teams from:', apiUrl);
        console.log('REACT_APP_CODESPACE_NAME:', codespaceNameEnv);

        const response = await fetch(apiUrl);
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Teams data received:', data);

        const teamsList = data.results ? data.results : Array.isArray(data) ? data : [];
        console.log('Processed teams list:', teamsList);
        
        setTeams(teamsList);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching teams:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchTeams();
  }, []);

  if (loading) {
    return (
      <div className="text-center mt-5">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-3 text-muted">Loading teams...</p>
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

  return (
    <div className="teams-container">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>👥 Teams</h2>
        <span className="badge bg-primary">{teams.length} teams</span>
      </div>

      {teams.length === 0 ? (
        <div className="alert alert-warning" role="alert">
          <strong>No teams found</strong> - Check if the API is running and populated with test data.
        </div>
      ) : (
        <div className="row g-4">
          {teams.map((team) => (
            <div key={team.id} className="col-md-6 col-lg-4">
              <div className="card h-100 shadow-sm">
                <div className="card-header bg-light">
                  <h5 className="card-title mb-0">
                    {team.name.charAt(0).toUpperCase() + team.name.slice(1)}
                  </h5>
                </div>
                <div className="card-body">
                  <p className="card-text text-muted">{team.description}</p>
                  
                  <div className="team-details mt-3">
                    <div className="mb-2">
                      <small className="text-muted d-block">Team Owner</small>
                      <span className="team-badge">
                        {team.owner_name || `Owner #${team.owner}`}
                      </span>
                    </div>
                    <div className="mb-2">
                      <small className="text-muted d-block">Members</small>
                      <span className="badge bg-success">
                        {team.members_count || 0} members
                      </span>
                    </div>
                  </div>
                </div>
                <div className="card-footer bg-light d-flex justify-content-between">
                  <small className="text-muted">ID: {team.id}</small>
                  <button className="btn btn-sm btn-outline-primary">View Details</button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Teams;
