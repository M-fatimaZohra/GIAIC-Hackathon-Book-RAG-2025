# Research: Cohere to Gemini Embedding Migration

## Decision: Google Generative AI SDK for Embeddings
**Rationale**: Google's text-embedding-004 model provides 768-dimensional vectors with improved rate limits (1500 requests/day vs 1000/month for Cohere) and better performance (0.5s delay vs 2s). The SDK provides reliable access to the embedding service with proper error handling.

**Alternatives considered**:
- OpenAI embeddings: Would require different dimensional vectors (1536-dim) which would complicate the migration
- Self-hosted embeddings: Would require infrastructure changes beyond the scope of this migration
- Other providers: Gemini provides the best balance of cost, performance, and rate limits for this use case

## Decision: Qdrant Collection Recreation Strategy
**Rationale**: The create_collection() function in the existing code will automatically recreate the collection with new dimensions if it doesn't match the expected configuration. This simplifies the migration process by handling the dimension change automatically.

**Alternatives considered**:
- Manual deletion of existing collection: Risk of data loss if migration fails
- Dual collection approach: Would require more complex logic and additional storage costs

## Decision: Rate Limit Management
**Rationale**: The new rate limits (1500 requests/day) require changing from monthly to daily tracking with appropriate delays. This provides significantly more capacity than the previous 1000 requests/month while maintaining appropriate API usage patterns.

**Alternatives considered**:
- No rate limiting: Would risk exceeding API quotas
- Complex adaptive rate limiting: Over-engineering for this specific migration

## Decision: Rollback Strategy
**Rationale**: File backups and dependency restoration provide the most straightforward rollback mechanism. This ensures the system can return to working state within 30 minutes as required.

**Alternatives considered**:
- Git-based rollback: Would require more complex git operations and might not handle dependency changes well
- Docker container rollback: Not applicable as this is a direct code change without containerization

## Technical Decision Points Resolved

1. **Gemini API quota**: 1500 requests/day is sufficient for the textbook chatbot usage patterns
2. **Error handling**: Will implement appropriate try-catch blocks around Gemini API calls with fallback mechanisms
3. **Qdrant collection deletion**: Will use automatic recreation via create_collection() which handles dimension mismatches
4. **Rollback triggers**: Migration will abort if ingestion fails or if response quality degrades significantly during testing phase