import React, { useState, useEffect } from 'react';
import { getRecommendations } from '../services/api';

const Recommendations = () => {
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getRecommendations()
      .then(res => {
        setRecommendations(res.data.recommendations);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h2 className="text-3xl font-bold mb-6">AI Health Recommendations 💡</h2>
      
      {loading ? (
        <p>Loading your insights...</p>
      ) : (
        <div className="space-y-4">
          {recommendations.map((rec, i) => (
            <div key={i} className="bg-white rounded-lg shadow p-6 border-l-4 border-green-500">
              <p className="text-lg text-gray-800">{rec}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Recommendations;
