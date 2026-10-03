# Issachar System Architecture

Issachar is a deterministic system with bounded model assistance.

## Layers
1. Storage: prospects, evidence, opportunities, buyers, outreach, outcomes, research runs.
2. Deterministic core: validation, qualification, deduplication, state transitions, rate limits, approvals.
3. Model layer: local-model adapter, extraction, classification, hypothesis generation, summarization and drafting.
4. Orchestration: research jobs, queues, retries, run state and agent/task boundaries.
5. External adapters: web research, email, CRM/Asana, GitHub and future integrations.

## Hard boundary
The model proposes structured outputs. The deterministic layer decides whether outputs are valid and actionable.

The model must not bypass qualification, invent evidence, send outreach directly, mutate external systems without an explicit adapter, or decide its own permissions.

## Execution
discover -> verify -> evidence -> qualify -> model -> validate -> opportunity -> human review -> outreach queue -> transport

## Local model
The adapter is provider-neutral so the existing local Ollama/llama-server setup can be used without coupling the core to one runtime.

## Deterministic responsibilities
Identity, deduplication, qualification, source checks, timestamps, contact validation, approval, send limits, retries and audit events.

## Model responsibilities
Messy-text extraction, evidence summarization, hypothesis generation, personalized draft language, workflow classification and validation-question suggestions.

## Next infrastructure
SQLite/PostgreSQL persistence, typed serialization, Ollama adapter, structured output validation, research queue, email transport adapter and audit/event log.
