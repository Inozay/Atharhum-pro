# Product Specification — Atharhum v2

## Product DNA
SOURCE → PROVENANCE → TRUST → INTELLIGENCE → LEARNING → IMPACT → NEXT GENERATION

## Core user journey
1. Discover a trusted item.
2. Open its Content Passport.
3. Verify identity and status.
4. Trace origin, review, version and derivatives.
5. Ask the source-grounded assistant.
6. Start a learning journey.
7. Complete lessons.
8. Generate privacy-preserving impact signals.

## What is intentionally real in this build
- API-backed content and verification.
- Deterministic source-grounded retrieval with citations.
- Persistent browser learning progress.
- Event recording endpoint.
- Impact funnel backed by API data.
- Render/Docker deployment path.

## What is not claimed
The seeded impact numbers are product demonstration data, not empirical research. The current assistant is a local retrieval engine, not a production LLM. Production expansion can add document ingestion, embeddings, a vector database, knowledge graph, human review workflow, authentication, and an LLM provider.

## Evaluation alignment
- Completeness: product can be explored end-to-end.
- Usability: primary journeys are one or two clicks away.
- Innovation: provenance + grounded intelligence + learning + impact are connected.
- Technical feasibility: FastAPI, typed endpoints, Docker and Render configuration.
- Trust: source, version, review and provenance are first-class objects.
- Responsible AI: assistant exposes sources and declines unsupported questions.
- Scalability: current data layer is replaceable by PostgreSQL/vector/graph infrastructure without changing the UX contract.
