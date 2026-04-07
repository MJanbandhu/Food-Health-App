import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="flex flex-col items-center justify-center py-20 px-4 text-center">
      <h1 className="text-5xl font-extrabold text-green-700 tracking-tight sm:text-6xl mb-6">
        Eat Smart, Live Better.
      </h1>
      <p className="mt-4 max-w-2xl text-xl text-gray-500 mb-10">
        Track your food, automatically estimate calories with our smart AI scanner, and receive personalized health recommendations based on your unique habits.
      </p>
      <div className="flex flex-col sm:flex-row gap-4">
        <Link to="/scanner" className="bg-green-600 text-white font-bold py-3 px-8 rounded-full shadow-lg hover:bg-green-700 transition">
          Try the Scanner
        </Link>
        <Link to="/dashboard" className="bg-white text-green-600 font-bold py-3 px-8 rounded-full border border-green-200 shadow-sm hover:bg-green-50 transition">
          View Dashboard
        </Link>
      </div>
    </div>
  );
};

export default Home;
