import React, { useState, useEffect } from 'react';
import axios from 'axios';

const API_BASE = 'http://localhost:8000/api/v1';

function App() {
  const [dashboard, setDashboard] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const [foodInput, setFoodInput] = useState('');
  const [caloriesInput, setCaloriesInput] = useState('');

  const fetchDashboard = async () => {
    try {
      const res = await axios.get(`${API_BASE}/dashboard`);
      setDashboard(res.data);
    } catch (e) { console.error(e); }
  };

  const fetchRecommendations = async () => {
    try {
      const res = await axios.get(`${API_BASE}/recommendations`);
      setRecommendations(res.data.recommendations);
    } catch (e) { console.error(e); }
  };

  const trackFood = async (e) => {
    e.preventDefault();
    if (!foodInput || !caloriesInput) return;
    try {
      await axios.post(`${API_BASE}/track`, {
        name: foodInput,
        calories: parseInt(caloriesInput)
      });
      setFoodInput('');
      setCaloriesInput('');
      fetchDashboard();
    } catch (e) { console.error(e); }
  };

  const scanFood = async () => {
    try {
      const res = await axios.post(`${API_BASE}/scanner`);
      setFoodInput(res.data.detected_food);
      setCaloriesInput(res.data.estimated_calories.toString());
    } catch (e) { console.error(e); }
  };

  useEffect(() => {
    fetchDashboard();
    fetchRecommendations();
  }, []);

  return (
    <div className="max-w-4xl mx-auto p-4 space-y-6">
      <h1 className="text-4xl font-bold text-green-600 text-center my-6">Food & Health Smart App</h1>
      
      {/* Dashboard */}
      {dashboard && (
        <div className="bg-white p-6 rounded shadow">
          <h2 className="text-2xl font-semibold mb-4">Dashboard</h2>
          {dashboard.alerts.length > 0 && (
            <div className="bg-red-100 text-red-700 p-3 rounded mb-4">
              {dashboard.alerts.map((a, i) => <p key={i}>{a}</p>)}
            </div>
          )}
          <div className="flex justify-between items-center bg-gray-100 p-4 rounded text-xl">
            <span>Daily Goal: <span className="font-bold">{dashboard.daily_goal} kcal</span></span>
            <span>Consumed: <span className={`font-bold ${dashboard.total_calories > dashboard.daily_goal ? 'text-red-600' : 'text-green-600'}`}>
              {dashboard.total_calories} kcal
            </span></span>
          </div>
          <div className="mt-4">
            <h3 className="font-medium">Recent Logs:</h3>
            <ul className="list-disc pl-5 mt-2">
              {dashboard.recent_logs.map((log, i) => (
                <li key={i}>{log.name} - {log.calories} kcal</li>
              ))}
            </ul>
          </div>
        </div>
      )}

      {/* Tracker & Scanner */}
      <div className="bg-white p-6 rounded shadow flex flex-col md:flex-row gap-6">
        <div className="flex-1">
          <h2 className="text-2xl font-semibold mb-4">Log Food manually</h2>
          <form onSubmit={trackFood} className="flex flex-col gap-3">
            <input type="text" placeholder="Food name" className="border p-2 rounded" value={foodInput} onChange={e => setFoodInput(e.target.value)} />
            <input type="number" placeholder="Calories" className="border p-2 rounded" value={caloriesInput} onChange={e => setCaloriesInput(e.target.value)} />
            <button type="submit" className="bg-green-600 text-white p-2 rounded hover:bg-green-700">Track Meal</button>
          </form>
        </div>
        <div className="flex-1 flex flex-col items-center justify-center border-l md:pl-6 pt-6 md:pt-0">
          <h2 className="text-2xl font-semibold mb-4 text-center">Smart Scanner</h2>
          <p className="text-gray-500 mb-4 text-center">Take a picture of your food or scan to auto-detect calories using AI.</p>
          <button onClick={scanFood} className="bg-blue-600 text-white px-6 py-3 rounded shadow hover:bg-blue-700 text-lg w-full">
            📷 Scan Food Image
          </button>
        </div>
      </div>

      {/* Recommendations */}
      <div className="bg-white p-6 rounded shadow">
        <h2 className="text-2xl font-semibold mb-4">AI Recommendations</h2>
        <ul className="space-y-2">
          {recommendations.map((rec, i) => (
            <li key={i} className="flex items-center gap-2">
              <span className="text-green-500">✨</span> {rec}
            </li>
          ))}
        </ul>
      </div>

    </div>
  );
}

export default App;
