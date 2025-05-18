import React from 'react';

export default function FeatureColumns({ items }) {
  // Ensure items is an array and has at least one item to prevent errors
  if (!Array.isArray(items) || items.length === 0) {
    return null; // Or some fallback UI
  }

  return (
    <div className="feature-columns-container">
      {items.slice(0, 3).map((item, index) => ( // Take only the first 3 items for a 3-column layout
        <div key={index} className="feature-column">
          <div className="feature-image-row">
            {item.imageSrc && (
              <img 
                src={item.imageSrc} 
                alt={item.imageAlt || 'Feature image'} 
                className="feature-image" 
              />
            )}
          </div>
          <div className="feature-text-row">
            <p className="feature-text">{item.text}</p>
          </div>
        </div>
      ))}
    </div>
  );
}
