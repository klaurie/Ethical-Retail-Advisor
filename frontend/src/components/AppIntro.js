import React from 'react';


export default function AppIntro({ text }) {
  const defaultIntroText = "Discover how your favorite brands align with your values.";

  return (
    <div className="app-intro-container">
      <p className="app-intro-text">
        {text || defaultIntroText}
      </p>
    </div>
  );
}
