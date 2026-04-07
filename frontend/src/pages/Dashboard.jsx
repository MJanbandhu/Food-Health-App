import React, { useState, useEffect } from 'react';
import { getDashboardData } from '../services/api';

const Dashboard = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    getDashboardData()
      .then(res => setData(res.data))
      .catch(console.error);
  }, []);

  if (!data) return <div className="p-4">Loading dashboard...</div>;

  return (
    <div className="p-6">
      <h2 className="text-3xl font-bold mb-6">Your Dashboard 📊</h2>
      {data.alerts && data.alerts.length > 0 && (
        <div className="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 mb-6">
          {data.alerts.map((a, i) => <p key={i}>{a}</p>)}
        </div>
      )}
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-xl font-semibold mb-2">Calories Today</h3>
          <div className="text-4xl font-bold text-blue-600">{data.total_calories} <span className="text-lg text-gray-500 font-normal">/ {data.daily_goal} kcal</span></div>
        </div>
        
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-xl font-semibold mb-4">Recent Meals</h3>
          <ul className="space-y-3">
            {data.recent_logs && data.recent_logs.map((log, i) => (
              <li key={i} className="flex justify-between items-center border-b pb-2">
                <span className="font-medium">{log.name}</span>
                <span className="text-gray-600">{log.calories} kcal</span>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
