import { evaluateCompany } from './Services';

// Services.test.js

// Mock the global fetch function
global.fetch = jest.fn();

describe('evaluateCompany', () => {
    beforeEach(() => {
        // Clear all mock calls between tests
        fetch.mockClear();
    });

    test('should successfully fetch and return evaluation data', async () => {
        // Mock data
        const mockCompanyId = '123';
        const mockResponse = {
            ethics_score: 85,
            categories: {
                environmental: 80,
                social: 90,
                governance: 85
            }
        };
        
        // Mock successful fetch response
        fetch.mockResolvedValueOnce({
            ok: true,
            json: async () => mockResponse
        });

        // Call the function
        const result = await evaluateCompany(mockCompanyId);

        // Assertions
        expect(fetch).toHaveBeenCalledTimes(1);
        expect(fetch).toHaveBeenCalledWith('http://localhost:8000/evaluate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ company_id: mockCompanyId }),
        });
        expect(result).toEqual(mockResponse);
    });

    test('should throw error when API returns non-OK response', async () => {
        // Mock data
        const mockCompanyId = '123';
        
        // Mock failed fetch response
        fetch.mockResolvedValueOnce({
            ok: false,
            status: 404
        });

        // Assert that function throws error
        await expect(evaluateCompany(mockCompanyId)).rejects.toThrow('Error: 404');
        expect(fetch).toHaveBeenCalledTimes(1);
    });

    test('should handle network errors', async () => {
        // Mock data
        const mockCompanyId = '123';
        const networkError = new Error('Network failure');
        
        // Mock fetch throwing an error
        fetch.mockRejectedValueOnce(networkError);

        // Assert that function rethrows the error
        await expect(evaluateCompany(mockCompanyId)).rejects.toThrow(networkError);
        expect(fetch).toHaveBeenCalledTimes(1);
    });

    test('should handle empty company ID', async () => {
        // We should test with empty ID to verify robustness
        const mockCompanyId = '';
        
        // Mock successful fetch response with empty result
        fetch.mockResolvedValueOnce({
            ok: true,
            json: async () => ({ message: 'No data found' })
        });

        // Call the function
        const result = await evaluateCompany(mockCompanyId);

        // Verify fetch was called with empty company_id
        expect(fetch).toHaveBeenCalledWith(
            expect.any(String),
            expect.objectContaining({
                body: JSON.stringify({ company_id: '' })
            })
        );
        expect(result).toEqual({ message: 'No data found' });
    });
});