# Data Model: Cohere to Gemini Embedding Migration

## Entities

### Textbook Content
- **Description**: Represents the Physical AI & Humanoid Robotics textbook content
- **Fields**:
  - url (string): Source URL from sitemap.xml
  - content (string): Text content extracted from HTML
  - chunk_id (string): Unique identifier for content chunk
  - created_at (datetime): Timestamp of ingestion
- **Relationships**: Contains multiple Vector Embeddings

### Vector Embeddings
- **Description**: 768-dimensional numerical representations of text chunks
- **Fields**:
  - vector_id (string): Unique identifier for the vector
  - embedding (list[float]): 768-dimensional vector array
  - chunk_id (string): Reference to source content chunk
  - metadata (dict): Additional information including source URL
- **Validation**: Must be exactly 768 dimensions for Gemini embeddings
- **Relationships**: Belongs to Textbook Content

### Qdrant Collection
- **Description**: Vector database collection storing embeddings with metadata
- **Fields**:
  - collection_name (string): Name of the Qdrant collection
  - vector_size (int): Size of vectors (768 for Gemini, was 1024 for Cohere)
  - distance_metric (string): Distance calculation method (typically cosine)
- **State transitions**: Recreated during migration to accommodate new vector dimensions

### Chat Query
- **Description**: User input question that gets converted to embedding for similarity search
- **Fields**:
  - query_text (string): Original user question
  - query_embedding (list[float]): 768-dimensional query vector
  - timestamp (datetime): When the query was processed
- **Relationships**: Used to search Vector Embeddings for relevant context