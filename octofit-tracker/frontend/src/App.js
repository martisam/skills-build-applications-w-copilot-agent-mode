import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Users from './components/Users';
import Activities from './components/Activities';
import Teams from './components/Teams';
import Workouts from './components/Workouts';
import Leaderboard from './components/Leaderboard';
import logoSmall from './logo.svg';

function App() {
  return (
    <Router>
      <div className="App">
        {/* Navigation Menu */}
        <nav className="navbar navbar-expand-lg navbar-dark">
          <div className="container">
            <div className="logo-container">
              <img src={logoSmall} alt="OctoFit Logo" className="app-logo" />
              <Link className="navbar-brand" to="/">
                🐙 OctoFit Tracker
              </Link>
            </div>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <Link className="nav-link" to="/users">
                    👥 Users
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">
                    📊 Activities
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">
                    👥 Teams
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">
                    💪 Workouts
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">
                    🏆 Leaderboard
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        {/* Main Content */}
        <main className="container mt-5">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/users" element={<Users />} />
            <Route path="/activities" element={<Activities />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/workouts" element={<Workouts />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
          </Routes>
        </main>

        {/* Footer */}
        <footer className="bg-dark text-white text-center py-4 mt-5">
          <div className="container">
            <p className="mb-2">
              🐙 OctoFit Tracker - Your Ultimate Fitness Tracking Platform
            </p>
            <small className="text-muted">
              © 2026 OctoFit. All rights reserved. | Built with React & Django
            </small>
          </div>
        </footer>
      </div>
    </Router>
  );
}

function Home() {
  return (
    <div className="text-center">
      <h1 className="mb-5">Welcome to OctoFit Tracker 🐙</h1>
      <p className="lead mb-4" style={{ fontSize: '1.3rem' }}>
        Track your fitness activities and compete with your team members!
      </p>
      <div className="card" style={{ maxWidth: '600px', margin: '0 auto' }}>
        <div className="card-body p-5">
          <h5 className="card-title mb-4">Start Exploring</h5>
          <p className="card-text mb-4">
            Use the navigation menu above to explore the features of OctoFit:
          </p>
          <ul className="list-unstyled">
            <li className="mb-3">
              <span style={{ fontSize: '1.3rem', marginRight: '10px' }}>👥</span>
              <strong>Users</strong> - View all user profiles and fitness enthusiasts
            </li>
            <li className="mb-3">
              <span style={{ fontSize: '1.3rem', marginRight: '10px' }}>📊</span>
              <strong>Activities</strong> - Track and log your daily workouts and exercises
            </li>
            <li className="mb-3">
              <span style={{ fontSize: '1.3rem', marginRight: '10px' }}>👥</span>
              <strong>Teams</strong> - Join teams and collaborate with other fitness enthusiasts
            </li>
            <li className="mb-3">
              <span style={{ fontSize: '1.3rem', marginRight: '10px' }}>💪</span>
              <strong>Workouts</strong> - Browse and discover workout plans for all fitness levels
            </li>
            <li className="mb-3">
              <span style={{ fontSize: '1.3rem', marginRight: '10px' }}>🏆</span>
              <strong>Leaderboard</strong> - Check team rankings and compete for the top spot
            </li>
          </ul>
          <div className="mt-5">
            <Link to="/users" className="btn btn-primary me-2">
              Explore Users
            </Link>
            <Link to="/teams" className="btn btn-success">
              View Teams
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
