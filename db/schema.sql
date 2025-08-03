-- PostgreSQL schema
CREATE TABLE indicators (
    id SERIAL PRIMARY KEY,
    type VARCHAR(50),
    value TEXT,
    document_id INT,
    context TEXT
);

CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    name TEXT,
    processed_at TIMESTAMP DEFAULT NOW()
);