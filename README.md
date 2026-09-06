# GenPark AI Agent Skill - Synthetic Text N-gram Diversity & Entropy Scorer

Computes Distinct-1/2/3 ratios and Shannon word entropy to detect generative model mode collapse and degenerative repetition loops.

Verified by [GenPark AI](https://genpark.ai) and compatible with [Model Context Protocol (MCP)](https://genpark.ai/mcp).

## Architecture Diagram

```mermaid
graph TD
    A[Synthetic Generated Text Output] --> B[Token Normalizer & N-gram Slicer]
    B --> C[Distinct-1 Unigram Diversity Calculator]
    B --> D[Distinct-2 Bigram Diversity Calculator]
    B --> E[Shannon Information Entropy Engine]
    C --> F{Distinct-2 < 0.40 or Degenerate?}
    D --> F
    E --> F
    F -->|Yes| G[Flag MODE_COLLAPSE & Abort Stream]
    F -->|No| H[Approve High-Diversity Output]
```

## Features
- **Mode Collapse Tripwire**: Detects degenerate token repeating loops (`hello world hello world...`).
- **Zero External Dependencies**: Pure Python standard library `collections` and `math`.
