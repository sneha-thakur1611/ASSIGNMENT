Set-up instructions:

Step 1:

Clone the Repository
git clone https://github.com/sneha-thakur1611/Assignment.git
cd Assignment

Step 2:

Create Virtual Environment

python3 -m venv venv
source venv/bin/activate


Step 3:

Install Requirements

pip install -r requirements.txt


Step 4:

Run the API Server
uvicorn app.main:app --reload

Server runs at: http://127.0.0.1:8000

API Endpoints

GET	/assets	List all tracked assets
GET	/metrics/{symbol}	Return price, 24h change, 7d average
GET	/compare?asset1=X&asset2=Y	Compare two assets
GET	/summary	Return a GenAI-generated summary
POST	/ingest	Manually trigger data ingestion
