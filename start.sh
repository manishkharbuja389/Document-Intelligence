#!/bin/bash

echo "Running document processing..."
python process_documents.py

echo "Starting FastAPI server..."
uvicorn app.main:app --host 0.0.0.0 --port 8000
