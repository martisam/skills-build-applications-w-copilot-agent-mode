import React, { useState, useEffect } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const codespaceNameEnv = process.env.REACT_APP_CODESPACE_NAME;
        
        let apiUrl;
        if (codespaceNameEnv) {
          apiUrl = `https://${codespaceNameEnv}-8000.app.github.dev/api/users/`;
        } else {
          apiUrl = `http://localhost:8000/api/users/`;
        }

        console.log('Fetching Users from:', apiUrl);
        console.log('REACT_APP_CODESPACE_NAME:', codespaceNameEnv);

        const response = await fetch(apiUrl);
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Users data received:', data);

        const usersList = data.results ? data.results : Array.isArray(data) ? data : [];
        console.log('Processed users list:', usersList);
        
        setUsers(usersList);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching users:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  if (loading) {
    return (
      <div className="text-center mt-5">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-3 text-muted">Loading users...</p>
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
    <div className="users-container">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>👥 Users</h2>
        <span className="badge bg-primary">{users.length} users</span>
      </div>

      {users.length === 0 ? (
        <div className="alert alert-warning" role="alert">
          <strong>No users found</strong> - Check if the API is running and populated with test data.
        </div>
      ) : (
        <div className="card">
          <div className="table-responsive">
            <table className="table table-hover table-striped mb-0">
              <thead className="table-dark">
                <tr>
                  <th>ID</th>
                  <th>Username</th>
                  <th>Email</th>
                  <th>First Name</th>
                  <th>Last Name</th>
                </tr>
              </thead>
              <tbody>
                {users.map((user) => (
                  <tr key={user.id}>
                    <td>
                      <span className="badge bg-secondary">{user.id}</span>
                    </td>
                    <td>
                      <strong>{user.username}</strong>
                    </td>
                    <td>
                      <a href={`mailto:${user.email}`} className="link-primary">
                        {user.email}
                      </a>
                    </td>
                    <td>{user.first_name}</td>
                    <td>{user.last_name}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
};

export default Users;
                  <td>{user.email}</td>
                  <td>{user.first_name}</td>
                  <td>{user.last_name}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default Users;
