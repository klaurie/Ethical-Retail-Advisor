import React from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import SearchBar from './SearchBar';

test('renders SearchBar component', () => {
    render(<SearchBar onSearch={() => {}}/>);
    const inputElement = screen.getByPlaceholderText(/search/i);
    expect(inputElement).toBeInTheDocument();
});

test('calls onSearch prop when input changes', async () => {
    const onSearchMock = jest.fn();
    render(<SearchBar onSearch={onSearchMock} />);

    // Get the input and type a value
    const inputElement = screen.getByPlaceholderText(/search/i);
    await userEvent.type(inputElement, 'test');

    // Submit form
    const button = screen.getByRole('button', { name: /search/i });
    await userEvent.click(button);

    // Check if onSearch was called with the correct argument
    expect(onSearchMock).toHaveBeenCalledTimes(1);
    // Check if the correct value was passed
    expect(onSearchMock).toHaveBeenCalledWith('test');
});