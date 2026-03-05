"""
Mock FastAPI server for RAG API endpoints.
This can be used for testing or local development.
"""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Health check endpoint
@app.get("/health")
def health():
    return {"status": "ok"}

# Metrics endpoint
@app.get("/metrics")
def metrics():
    return {"metrics": "mock_metrics"}

# Configuration endpoint
@app.get("/configuration")
def configuration():
    return {"configuration": "mock_configuration"}

# Generate response endpoint
@app.post("/generate")
def generate():
    return JSONResponse(content={
        "answer": "This is a mock generated answer.",
        "sources": ["mock_source_1", "mock_source_2"],
        "citations": [],
        "metadata": {}
    })

# Chat completions (OpenAI compatible alias)
@app.post("/chat/completions")
def chat_completions():
    return JSONResponse(content={
        "answer": "This is a mock chat completion.",
        "sources": ["mock_source_1", "mock_source_2"],
        "citations": [],
        "metadata": {}
    })

# Search endpoint
@app.post("/search")
def search():
    return JSONResponse(content={
        "citations": [
            {"doc_id": "mock_doc_1", "score": 0.99},
            {"doc_id": "mock_doc_2", "score": 0.95}
        ]
    })

# Summary endpoint
@app.get("/summary")
def summary():
    return JSONResponse(content={
        "summary": "This is a mock summary.",
        "status": "complete"
    })

# V1 endpoints (with /v1 prefix)
@app.get("/v1/health")
def v1_health():
    return {"status": "ok"}

@app.get("/v1/metrics")
def v1_metrics():
    return {"metrics": "mock_metrics"}

@app.get("/v1/configuration")
def v1_configuration():
    return {"configuration": "mock_configuration"}

@app.post("/v1/generate")
def v1_generate():
    return JSONResponse(content={
        "answer": "This is a mock generated answer.",
        "sources": ["mock_source_1", "mock_source_2"],
        "citations": [],
        "metadata": {}
    })

@app.post("/v1/chat/completions")
def v1_chat_completions():
    return JSONResponse(content={
        "answer": "This is a mock chat completion.",
        "sources": ["mock_source_1", "mock_source_2"],
        "citations": [],
        "metadata": {}
    })

@app.post("/v1/search")
def v1_search():
    return JSONResponse(content={
        "citations": [
            {"doc_id": "mock_doc_1", "score": 0.99},
            {"doc_id": "mock_doc_2", "score": 0.95}
        ]
    })

@app.get("/v1/summary")
def v1_summary():
    return JSONResponse(content={
        "summary": "This is a mock summary.",
        "status": "complete"
    })

# V2 endpoint for vector store search (OpenAI-compatible)
@app.post("/v2/vector_stores/{vector_store_id}/search")
def v2_vector_store_search(vector_store_id: str):
    return JSONResponse(content={
        "results": [
            {"id": "mock_result_1", "score": 0.98},
            {"id": "mock_result_2", "score": 0.96}
        ]
    })

# Documentation endpoints
@app.get("/v1/docs", include_in_schema=False)
def v1_docs():
    return JSONResponse(content={"docs": "mock v1 docs"})

@app.get("/v1/openapi.json", include_in_schema=False)
def v1_openapi():
    return JSONResponse(content={"openapi": "mock v1 openapi"})

@app.get("/v2/docs", include_in_schema=False)
def v2_docs():
    return JSONResponse(content={"docs": "mock v2 docs"})

@app.get("/v2/openapi.json", include_in_schema=False)
def v2_openapi():
    return JSONResponse(content={"openapi": "mock v2 openapi"})

@app.get("/docs", include_in_schema=False)
def docs():
    return JSONResponse(content={"docs": "mock docs"})

@app.get("/openapi.json", include_in_schema=False)
def openapi():
    return JSONResponse(content={"openapi": "mock openapi"})
