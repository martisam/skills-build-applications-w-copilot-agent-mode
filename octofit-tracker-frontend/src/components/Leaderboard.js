import React, { useState, useEffect } from 'react';

const Leaderboard = () => {
  const [leaderboards, setLeaderboards] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboards = async () => {
      try {
        const codespaceNameEnv = process.env.REACT_APP_CODESPACE_NAME;
        
        let apiUrl;
        if (codespaceNameEnv) {
          apiUrl = `https://${codespaceNameEnv}-8000.app.github.dev/api/teams/`;
        } else {
          apiUrl = `http://localhost:8000/api/teams/`;
        }

        console.log('Fetching Leaderboards from:', apiUrl);
        console.log('REACT_APP_CODESPACE_NAME:', codespaceNameEnv);

        const response = await fetch(apiUrl);
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Leaderboard data received:', data);

        const leaderboardList = data.results ? data.results : Array.isArray(data) ? data : [];
        console.log('Processed leaderboard list:', leaderboardList);
        
        setLeaderboards(leaderboardList);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching leaderboards:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchLeaderboards();
  }, []);

  if (loading) {
    return (
      <div className="text-center mt-5">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-3 text-muted">Loading leaderboards...</p>
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

  const getMedalEmoji = (rank) => {
    switch (rank) {
      case 1:
        return '🥇';
      case 2:
        return '🥈';
      case 3:
        return '🥉';
      default:
        return '•';
    }
  };

  const getRankClass = (rank) => {
    switch (rank) {
      case 1:
        return 'leaderboard-rank first';
      case 2:
        return 'leaderboard-rank second';
      case 3:
        return 'leaderboard-rank third';
      default:
        return 'leaderboard-rank';
    }
  };

  return (
    <div className="leaderboard-container">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>🏆 Leaderboard</h2>
        <span className="badge bg-primary">{leaderboards.length} teams</span>
      </div>

      {leaderboards.length === 0 ? (
        <div className="alert alert-warning" role="alert">
          <strong>No leaderboards found</strong> - Check if the API is running and populated with test data.
        </div>
      ) : (
        <div className="row g-4">
          {leaderboards.map((leaderboard) => (
            <div key={leaderboard.id} className="col-md-6 col-lg-12">
              <div className="card shadow-sm">
                <div className="card-header bg-gradient" style={{ backgroundColor: '#0d6efd' }}>
                  <h5 className="mb-0 text-white">
                    <span style={{ marginRight: '10px' }}>🏅</span>
                    Team: {leaderboard.name ? leaderboard.name.charAt(0).toUpperCase() + leaderboard.name.slice(1) : `Team ${leaderboard.id}`}
                  </h5>
                </div>
                <div className="card-body p-0">
                  {leaderboard.leaderboard_entries && leaderboard.leaderboard_entries.length > 0 ? (
                    <div className="table-responsive">
                      <table className="table table-hover mb-0">
                        <thead className="table-light">
                          <tr>
                            <th style={{ width: '80px' }} className="text-center">Rank</th>
                            <th>User</th>
                            <th className="text-center">Points</th>
                            <th className="text-center">Activities</th>
                            <th className="text-center">Duration</th>
                            <th className="text-center">Calories</th>
                          </tr>
                        </thead>
                        <tbody>
                          {leaderboard.leaderboard_entries.sort((a, b) => a.rank - b.rank).map((entry) => (
                            <tr key={entry.id} style={{ backgroundColor: entry.rank <= 3 ? '#f8f9fa' : '' }}>
                              <td className="text-center">
                                <span className={getRankClass(entry.rank)}>
                                  {getMedalEmoji(entry.rank)} {entry.rank}
                                </span>
                              </td>
                              <td>
                                <strong>{entry.user_name || `User #${entry.user}`}</strong>
                              </td>
                              <td className="text-center">
                                <span className="badge bg-warning text-dark">
                                  {entry.points}
                                </span>
                              </td>
                              <td className="text-center">{entry.activities_count}</td>
                              <td className="text-center">
                                <small className="text-muted">
                                  {entry.total_duration_minutes || 0} min
                                </small>
                              </td>
                              <td className="text-center">
                                <small className="text-muted">
                                  {entry.total_calories_burned || 0} cal
                                </small>
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  ) : (
                    <div className="p-4 text-center text-muted">
                      <p>No entries in this leaderboard</p>
                    </div>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Leaderboard;
