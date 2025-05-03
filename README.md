# Ethical Retail Advisor

## API Base URL
`http://localhost:8000`

## Endpoints

### 1. **Evaluate Ethics** - `POST /evaluate`

Evaluate the ethics of a company by its ID.

#### Example Request
``bash
curl -X POST http://localhost:8000/evaluate 
  -H "Content-Type: application/json" 
  -d '{"company_id": "cmp-001"}'
``

#### Example Response
``json
{
  "overall_score": 7.2,
  "categories": {
    "sustainability": 6.5,
    "politics": 8.0
  }
}
``

### 2. **Search by Text** - `POST /search/text`

Search for a company by name and optionally evaluate its ethics.

#### Example Request
``bash
curl -X POST http://localhost:8000/search/text?eval=true 
  -H "Content-Type: application/json" 
  -d '{"query": "apple"}'
``

#### Example Response
``json
{
  "name": "Apple Inc.",
  "company_id": "cmp-001",
  "ethics_score": {
    "overall_score": 7.2,
    "categories": {
      "sustainability": 6.5,
      "politics": 8.0
    }
  }
}
``

## Development

1. Install dependencies:
   ``bash
   pip install -r requirements.txt
   ``

2. Run the application:
   ``bash
   uvicorn main:app --reload
   ``

   or

   ``bash
   python3 -m main
   ``

3. Test the API with:
   ``bash
   curl -X POST http://localhost:8000/evaluate -H "Content-Type: application/json" -d '{"company_id": "cmp-001"}'
   ``

4. Run frontend:

  Prerequisites
  Node.js (v14.0.0 or higher)
  npm (v6.0.0 or higher)
  
  Installation
  Navigate to the frontend directory: cd frontend

  Install dependencies: npm install

  Development Server
  Start the development server: npm start

  This will run the app in development mode and open it in your browser at http://localhost:3000.

  Running Both Frontend and Backend
  You can run both services simultaneously by:

  Start the backend in one terminal as described above
  Start the frontend in another terminal using the steps in this section

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
