import React from 'react';

const App: React.FC = () => {
  return (
    <div className="flex flex-col items-center min-h-screen pt-16 bg-white">
      {/* Logo */}
      <img
        src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
        alt="Google"
        className="w-64 mb-8"
      />

      {/* Search Bar */}
      <div className="flex items-center border border-gray-300 rounded-full px-6 py-3 w-3/5 max-w-2xl shadow-lg hover:shadow-2xl transition-shadow duration-300">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="h-5 w-5 text-gray-500 mr-3"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
          />
        </svg>
        <input
          type="text"
          className="flex-grow outline-none"
          autoFocus
        />
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="h-5 w-5 text-gray-500 ml-3 cursor-pointer"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </div>

      {/* Buttons */}
      <div className="flex space-x-4 mt-8 text-blue-700">
        <button className="bg-gray-100 hover:bg-gray-200 px-6 py-2 rounded">
          Google Search
        </button>
        <button className="bg-gray-100 hover:bg-gray-200 px-6 py-2 rounded">
          I'm Feeling Lucky
        </button>
      </div>

      {/* Language Links */}
      <div className="mt-12 text-sm text-gray-600">
        <p>
          Google offered in:{" "}
          <a href="#" className="text-blue-600">Hausa</a>
          {" "} <a href="#" className="text-blue-600">Igbo</a>
          {" "} <a href="#" className="text-blue-600">Yoruba</a>
        </p>
      </div>

      {/* Footer */}
      <div className="absolute bottom-4 w-full text-center text-sm text-gray-500 space-y-2">
        <div className="space-x-6">
          <a href="#" className="hover:underline">About</a>
          <a href="#" className="hover:underline">Advertising</a>
          <a href="#" className="hover:underline">Business</a>
          <a href="#" className="hover:underline">How Search works</a>
        </div>
        <div className="space-x-6">
          <a href="#" className="hover:underline">Privacy</a>
          <a href="#" className="hover:underline">Terms</a>
          <a href="#" className="hover:underline">Settings</a>
        </div>
      </div>
    </div>
  );
};

export default App;