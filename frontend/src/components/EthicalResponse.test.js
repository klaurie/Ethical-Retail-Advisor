import React from 'react';
import { render, screen } from '@testing-library/react';
import EthicalCard from './EthicalResponse';

describe('EthicalCard Component', () => {
    const mockProps = {
        brand: 'Test Brand',
        rating: 7,
        sources: ['GoodOnYou', 'Ethical Consumer'],
        breakdown: ['Good labor practices', 'Uses recycled materials'],
        alternatives: ['Better Brand 1', 'Better Brand 2']
    };

    test('renders brand name correctly', () => {
        render(<EthicalCard {...mockProps} />);
        expect(screen.getByText(/Brand: Test Brand/i)).toBeInTheDocument();
    });

    test('renders rating correctly', () => {
        render(<EthicalCard {...mockProps} />);
        expect(screen.getByText('7/10')).toBeInTheDocument();
    });

    test('renders category labels', () => {
        render(<EthicalCard {...mockProps} />);
        expect(screen.getByText('🌱 Environmental')).toBeInTheDocument();
        expect(screen.getByText('💼 Labor')).toBeInTheDocument();
        expect(screen.getByText('💰 Ethics')).toBeInTheDocument();
    });

    test('renders all sources', () => {
        render(<EthicalCard {...mockProps} />);
        expect(screen.getByText('GoodOnYou')).toBeInTheDocument();
        expect(screen.getByText('Ethical Consumer')).toBeInTheDocument();
    });

    test('renders all breakdown items', () => {
        render(<EthicalCard {...mockProps} />);
        expect(screen.getByText('Good labor practices')).toBeInTheDocument();
        expect(screen.getByText('Uses recycled materials')).toBeInTheDocument();
    });

    test('renders all alternative brands', () => {
        render(<EthicalCard {...mockProps} />);
        expect(screen.getByText('Better Brand 1')).toBeInTheDocument();
        expect(screen.getByText('Better Brand 2')).toBeInTheDocument();
    });

    test('handles empty arrays gracefully', () => {
        const emptyProps = {
            brand: 'Test Brand',
            rating: 5,
            sources: [],
            breakdown: [],
            alternatives: []
        };
        render(<EthicalCard {...emptyProps} />);
        
        expect(screen.getByText('Sources Used:')).toBeInTheDocument();
        expect(screen.getByText('Breakdown:')).toBeInTheDocument();
        expect(screen.getByText('Suggested Alternatives:')).toBeInTheDocument();
        
        // Check that the lists are empty but their headers still appear
        const lists = screen.getAllByRole('list');
        expect(lists).toHaveLength(2); // Two empty lists for breakdown and alternatives
        expect(lists[0].children).toHaveLength(0);
        expect(lists[1].children).toHaveLength(0);
    });
});