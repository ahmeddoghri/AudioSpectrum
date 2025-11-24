# MCP Server Token Usage Experiment

## Objective
Measure token consumption vs value provided by each MCP server (brave-search, context7, firecrawl)

## Test Queries

### Category 1: Library Documentation (context7's strength)
1. **Query**: "How to use React useState hook with TypeScript"
2. **Query**: "Express.js middleware setup and error handling"
3. **Query**: "Next.js app router data fetching methods"

### Category 2: General Web Search (brave-search's strength)
1. **Query**: "Latest JavaScript framework trends 2025"
2. **Query**: "Best practices for web performance optimization"
3. **Query**: "What is WebAssembly and current browser support"

### Category 3: Web Scraping/Content Extraction (firecrawl's strength)
1. **URL**: https://developer.mozilla.org/en-US/docs/Web/JavaScript
2. **URL**: https://nodejs.org/en/about
3. **Task**: Map and extract structured data from a documentation site

### Category 4: Overlapping Queries (all could work)
1. **Query**: "Tailwind CSS grid layout examples"
2. **Query**: "How to deploy Node.js app to production"
3. **Query**: "TypeScript generics best practices"

## Metrics to Track

For each test run:
- **Input Tokens**: Tokens sent to the MCP server
- **Output Tokens**: Tokens returned by the MCP server
- **Total Tokens**: Sum of input + output
- **Time**: Response time
- **Quality Score** (1-5): How useful was the result?
  - 5 = Perfect, exactly what was needed
  - 4 = Very good, minor gaps
  - 3 = Adequate, usable but incomplete
  - 2 = Weak, some relevant info
  - 1 = Poor, not helpful
- **Token Efficiency**: Quality / Total Tokens × 1000

## Test Protocol

### Phase 1: Individual Tool Testing
Run each query through ONE MCP server at a time in isolated conversations to get clean token measurements.

**For each query:**
1. Start fresh conversation (to isolate token usage)
2. Ask Claude to use ONLY the specified MCP server
3. Record tokens used (check Claude Code UI or API response)
4. Rate the quality of results
5. Document findings

### Phase 2: Head-to-Head Comparison
Run "overlapping queries" through ALL three servers and compare:
- Which gave best results?
- Which used fewest tokens?
- Which had best token efficiency?

### Phase 3: Fallback Chain Testing
Test the fallback strategy:
1. Use context7 → if fails/poor → brave-search → if fails/poor → firecrawl
2. Measure cumulative token usage
3. Determine if fallback chains are worth it

## Expected Results

| MCP Server | Expected Token Range | Best Use Case | Efficiency Prediction |
|------------|---------------------|---------------|----------------------|
| context7 | 1k-5k per query | Library docs | High (focused results) |
| brave-search | 500-2k per query | General search | Very High (concise) |
| firecrawl | 2k-20k per query | Full content extraction | Medium (comprehensive) |

## Analysis Questions

1. **Value Threshold**: What's the acceptable token/quality ratio?
2. **Redundancy**: Are we paying for overlapping capabilities?
3. **Optimization**: Should we adjust which server we default to?
4. **Cost**: At current token prices, what's the $ cost per query type?

## Automated Test Script

Run this experiment programmatically (see: `mcp-token-test.js`)
