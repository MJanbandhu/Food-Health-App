import React, { useState } from 'react';
import { scanFood, trackFood } from '../services/api';

const Scanner = () => {
  const [detected, setDetected] = useState(null);
  const [status, setStatus] = useState('');

  const handleScan = async () => {
    try {
      setStatus('Scanning...');
      const res = await scanFood({});
      setDetected(res.data);
      setStatus('Scan complete!');
    } catch (e) {
      console.error(e);
      setStatus('Failed to scan image.');
    }
  };

  const handleTrack = async () => {
    if (!detected) return;
    try {
      await trackFood({ food_name: detected.detected_food, calories: detected.estimated_calories });
      setStatus('Successfully tracked meal!');
      setDetected(null);
    } catch(e) {
      console.error(e);
      setStatus('Failed to track.');
    }
  };

  return (
    <div className="p-6 max-w-2xl mx-auto">
      <h2 className="text-3xl font-bold mb-6 text-center">Smart Food Scanner 📸</h2>
      <div className="bg-white shadow rounded-lg p-8 text-center">
        <div className="w-full h-64 bg-gray-100 border-2 border-dashed border-gray-300 rounded mb-6 flex items-center justify-center">
          <span className="text-gray-400">Camera placeholder / Image dropzone</span>
        </div>
        <button onClick={handleScan} className="bg-blue-600 text-white font-bold py-3 px-8 rounded-full shadow-lg hover:bg-blue-700 transition">
          Simulate AI Scan
        </button>
        
        {status && <p className="mt-4 text-gray-600">{status}</p>}

        {detected && (
          <div className="mt-8 bg-green-50 p-6 rounded-lg border border-green-200">
            <h3 className="text-xl font-bold text-green-800 mb-2">Detected: {detected.detected_food}</h3>
            <p className="text-lg text-green-700 mb-4">Estimated Calories: {detected.estimated_calories} kcal</p>
            <button onClick={handleTrack} className="bg-green-600 text-white px-6 py-2 rounded shadow hover:bg-green-700">
              Log this meal
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default Scanner;
