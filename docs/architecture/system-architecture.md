# AegisTrace System Architecture

## Overview

AegisTrace is a continuous security provenance and attack-path
verification platform.

The platform correlates:

- Software provenance
- Dependency relationships
- Security policies
- Runtime behavior
- Security telemetry
- Attack-path relationships
- Cryptographically verifiable evidence

## Core Pipeline

Developer
    ↓
Source Repository
    ↓
Build Pipeline
    ↓
Artifact
    ↓
Deployment
    ↓
Runtime Telemetry
    ↓
Evidence Correlation
    ↓
Security Graph
    ↓
Attack-Path Analysis
    ↓
Policy Evaluation
    ↓
Incident Response

## Core Components

### Web Application

Provides the security dashboard and investigation interface.

### API

Provides authentication, project management, API endpoints,
and orchestration.

### Ingestion Service

Receives security and runtime events.

### Graph Engine

Builds relationships between software components,
dependencies, identities, processes, files, and network endpoints.

### Detection Engine

Identifies deviations and newly formed attack paths.

### Policy Engine

Evaluates observed behavior against defined security policies.

### Evidence Engine

Creates tamper-evident security evidence and maintains
event relationships.

### Runtime Agent

Collects runtime security telemetry from monitored workloads.

## Primary Data Stores

PostgreSQL:
Transactional application data.

Neo4j:
Security relationship graph.

ClickHouse:
High-volume security telemetry.

Redpanda:
Event streaming.

## Design Principles

1. Security evidence must be traceable.
2. Detection must be explainable.
3. Runtime observations must be correlated with software identity.
4. Security policies must be machine-readable.
5. Services should communicate through well-defined contracts.
6. Production security controls must fail safely.
7. Destructive automated actions require explicit policy authorization.