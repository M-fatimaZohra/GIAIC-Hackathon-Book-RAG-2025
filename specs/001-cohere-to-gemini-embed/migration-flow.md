# Migration Flow Diagram

## Current vs New Architecture

```mermaid
graph LR
    subgraph "Current Cohere-Based System"
        A1[User Query] --> B1[Cohere API<br/>embed-english-v3.0<br/>1024-dim]
        B1 --> C1[Qdrant DB<br/>1024-dim vectors]
        C1 --> D1[Context Retrieval]
        D1 --> E1[Chat Response]
        F1[Content Ingestion] --> G1[Cohere API<br/>embed-english-v3.0<br/>1024-dim]
        G1 --> C1
        F1 --> G1
    end

    subgraph "New Gemini-Based System"
        A2[User Query] --> B2[Gemini API<br/>text-embedding-004<br/>768-dim]
        B2 --> C2[Qdrant DB<br/>768-dim vectors]
        C2 --> D2[Context Retrieval]
        D2 --> E2[Chat Response]
        F2[Content Ingestion] --> G2[Gemini API<br/>text-embedding-004<br/>768-dim]
        G2 --> C2
        F2 --> G2
    end

    style A1 fill:#e1f5fe
    style A2 fill:#e8f5e8
    style B1 fill:#fff3e0
    style B2 fill:#e8f5e8
    style C1 fill:#f3e5f5
    style C2 fill:#e8f5e8
    style E1 fill:#ffebee
    style E2 fill:#e8f5e8
</mermaid>

## Migration Process Flow

```mermaid
graph TD
    A[Pre-Migration Audit] --> B[Dependency Migration]
    B --> C[Code Migration - ingest.py]
    C --> D[Code Migration - retrieve.py]
    D --> E[Data Re-ingestion]
    E --> F[Testing & Validation]
    F --> G[Cleanup & Documentation]

    style A fill:#fff3e0
    style B fill:#fff3e0
    style C fill:#fff3e0
    style D fill:#fff3e0
    style E fill:#e8f5e8
    style F fill:#e8f5e8
    style G fill:#e8f5e8
```