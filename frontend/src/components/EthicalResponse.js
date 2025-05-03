/*
 * EthicalCard Component:
 *
 *  This component is designed to display the ethical rating of a brand,
 *  along with its breakdown, sources, and suggested alternatives.
*/
import React from 'react';

export default function EthicalCard({ brand, rating, sources, breakdown, alternatives }) {
  return (
    <div className="card">
      <h2 className="card-title">Brand: {brand}</h2>

      <div className="rating-row">
        <span>Ethical Rating:</span>
        <span className="rating-badge">{rating}/10</span>
      </div>

      <div className="categories">
        <span>🌱 Environmental</span>
        <span>💼 Labor</span>
        <span>💰 Ethics</span>
      </div>

      <div className="sources">
        <strong>Sources Used:</strong>
        {sources.map((src, i) => (
          <span className="source-badge" key={i}>{src}</span>
        ))}
      </div>

      <div className="breakdown">
        <strong>Breakdown:</strong>
        <ul>
          {breakdown.map((item, i) => <li key={i}>{item}</li>)}
        </ul>
      </div>

      <div className="alternatives">
        <strong>Suggested Alternatives:</strong>
        <ul>
          {alternatives.map((alt, i) => <li key={i}>{alt}</li>)}
        </ul>
      </div>
    </div>
  );
};
