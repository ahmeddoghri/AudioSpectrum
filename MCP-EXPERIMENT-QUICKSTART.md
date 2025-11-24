# Quick Start: MCP Token Experiment

## 🎯 Goal
Find out which MCP server gives you the best bang for your buck (tokens).

## 📋 What You'll Need
- 30-60 minutes
- Claude Code UI (to see token usage)
- Terminal

## 🚀 Run the Experiment

### Step 1: Start the experiment
```bash
node mcp-token-test.js start
```

This will show you the first test query.

### Step 2: Run each test

For each test shown:

1. **Copy the query** from the terminal
2. **Paste into Claude Code** (new conversation for clean results)
3. **Wait for response**
4. **Check token usage** in Claude Code UI (should show something like "Token usage: 1234/200000")
5. **Rate the quality** (1-5):
   - 5 = Perfect, exactly what I needed
   - 4 = Very good
   - 3 = Okay, usable
   - 2 = Meh, some gaps
   - 1 = Not helpful
6. **Record the result**:
   ```bash
   node mcp-token-test.js record <input_tokens> <output_tokens> <quality>
   ```

### Step 3: View results anytime
```bash
node mcp-token-test.js report
```

## 💡 Example Test Flow

```bash
# Terminal shows:
# TEST 1/30
# Query: "How to use React useState hook with TypeScript"
# MCP Server: context7

# You run in Claude Code:
"Using ONLY context7, how to use React useState hook with TypeScript"

# Claude responds, you see: Token usage: 2847/200000

# You record:
node mcp-token-test.js record 847 2000 5
```

## 📊 What You'll Learn

The report will show:

✅ **Average tokens per server** - Who's using the most?
✅ **Average quality per server** - Who gives best results?
✅ **Efficiency score** - Best quality-to-token ratio
✅ **Cost estimates** - Actual $ at current token prices
✅ **Best use cases** - Which server for which task?

## ⚡ Quick Test (5 minutes)

Don't have time for 30 tests? Run a quick version:

```bash
# Test 1: Library docs with context7
"Using ONLY context7, how to use React useState hook"
node mcp-token-test.js record <tokens_in> <tokens_out> <quality>

# Test 2: Same query with brave-search
"Using ONLY brave-search, how to use React useState hook"
node mcp-token-test.js record <tokens_in> <tokens_out> <quality>

# Test 3: Same query with firecrawl
"Using ONLY firecrawl search, how to use React useState hook"
node mcp-token-test.js record <tokens_in> <tokens_out> <quality>

# Compare
node mcp-token-test.js report
```

## 🔄 Commands Reference

| Command | What it does |
|---------|-------------|
| `start` | Begin experiment, show first test |
| `record <i> <o> <q>` | Save test result (input, output, quality) |
| `next` | Show next pending test |
| `report` | Generate full analysis |
| `reset` | Start over (clears all data) |

## 📈 Reading the Report

**Efficiency Score**: Higher is better
- `> 2.0` = Excellent token efficiency
- `1.0-2.0` = Good efficiency
- `< 1.0` = Poor efficiency (high token cost)

**Cost Estimate**: Based on $3/1M tokens (adjust for your pricing)

## 🎓 Decision Framework

After the experiment, ask:

1. **Is the value worth the tokens?**
   - If efficiency < 1.0 and quality < 3 → Consider disabling

2. **Are servers redundant?**
   - If two servers score similarly → Keep the cheaper one

3. **Should I change defaults?**
   - Route library questions → highest efficiency for that category
   - Route general search → lowest token usage with acceptable quality

## 📁 Output Files

- `mcp-test-results.json` - Full structured data
- `mcp-test-results.csv` - Import to Excel/Sheets
- This data persists, so you can pause and resume anytime

---

**Pro tip**: Run this experiment monthly as MCP servers update their models and pricing changes!
