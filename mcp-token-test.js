#!/usr/bin/env node

/**
 * MCP Token Usage Experiment Runner
 *
 * This script helps you run controlled tests of each MCP server
 * and track token usage. You'll need to manually record tokens
 * from Claude Code UI after each test.
 */

const fs = require('fs');
const path = require('path');

const TEST_QUERIES = {
  libraryDocs: [
    "How to use React useState hook with TypeScript",
    "Express.js middleware setup and error handling",
    "Next.js app router data fetching methods"
  ],
  generalSearch: [
    "Latest JavaScript framework trends 2025",
    "Best practices for web performance optimization",
    "What is WebAssembly and current browser support"
  ],
  webScraping: [
    "https://developer.mozilla.org/en-US/docs/Web/JavaScript",
    "https://nodejs.org/en/about"
  ],
  overlapping: [
    "Tailwind CSS grid layout examples",
    "How to deploy Node.js app to production",
    "TypeScript generics best practices"
  ]
};

const MCP_SERVERS = ['context7', 'brave-search', 'firecrawl'];

class MCPTokenTest {
  constructor() {
    this.results = [];
    this.currentTest = 0;
    this.totalTests = 0;
    this.resultsFile = path.join(__dirname, 'mcp-test-results.json');

    // Load existing results if any
    if (fs.existsSync(this.resultsFile)) {
      this.results = JSON.parse(fs.readFileSync(this.resultsFile, 'utf8'));
    }
  }

  generateTestPlan() {
    const plan = [];
    let testId = 1;

    // Phase 1: Individual tool testing
    Object.entries(TEST_QUERIES).forEach(([category, queries]) => {
      queries.forEach(query => {
        MCP_SERVERS.forEach(server => {
          plan.push({
            id: testId++,
            phase: 1,
            category,
            query,
            server,
            status: 'pending'
          });
        });
      });
    });

    // Phase 2: Head-to-head for overlapping queries
    TEST_QUERIES.overlapping.forEach(query => {
      plan.push({
        id: testId++,
        phase: 2,
        category: 'head-to-head',
        query,
        servers: MCP_SERVERS,
        status: 'pending'
      });
    });

    this.totalTests = plan.length;
    return plan;
  }

  displayNextTest(plan) {
    const nextTest = plan.find(t => t.status === 'pending');

    if (!nextTest) {
      console.log('\n✅ All tests complete!');
      this.generateReport();
      return null;
    }

    console.log('\n' + '='.repeat(60));
    console.log(`📝 TEST ${nextTest.id}/${this.totalTests}`);
    console.log('='.repeat(60));
    console.log(`Category: ${nextTest.category}`);
    console.log(`Query: "${nextTest.query}"`);

    if (nextTest.phase === 1) {
      console.log(`MCP Server: ${nextTest.server}`);
      console.log('\n🔍 INSTRUCTIONS:');
      console.log(`1. Ask Claude: "Using ONLY ${nextTest.server}, ${nextTest.query}"`);
      console.log('2. Wait for response');
      console.log('3. Record token usage from Claude Code UI');
      console.log('4. Rate the quality (1-5)');
      console.log('5. Run: node mcp-token-test.js record <inputTokens> <outputTokens> <quality>');
    } else {
      console.log(`MCP Servers: ${nextTest.servers.join(', ')}`);
      console.log('\n🔍 INSTRUCTIONS:');
      console.log(`1. Ask Claude: "${nextTest.query}" (let it choose the best MCP server)`);
      console.log('2. Note which server(s) it used');
      console.log('3. Record token usage and quality');
      console.log('4. Run: node mcp-token-test.js record <inputTokens> <outputTokens> <quality> <serverUsed>');
    }

    console.log('\n' + '='.repeat(60) + '\n');

    return nextTest;
  }

  recordResult(inputTokens, outputTokens, quality, serverUsed = null) {
    const plan = this.generateTestPlan();
    const currentTest = plan.find(t => t.status === 'pending');

    if (!currentTest) {
      console.log('❌ No pending tests to record results for');
      return;
    }

    const result = {
      ...currentTest,
      inputTokens: parseInt(inputTokens),
      outputTokens: parseInt(outputTokens),
      totalTokens: parseInt(inputTokens) + parseInt(outputTokens),
      quality: parseInt(quality),
      efficiency: (parseInt(quality) / (parseInt(inputTokens) + parseInt(outputTokens))) * 1000,
      serverUsed: serverUsed || currentTest.server,
      timestamp: new Date().toISOString(),
      status: 'completed'
    };

    this.results.push(result);
    fs.writeFileSync(this.resultsFile, JSON.stringify(this.results, null, 2));

    console.log('\n✅ Result recorded!');
    console.log(`   Tokens: ${result.totalTokens} (${result.inputTokens} in, ${result.outputTokens} out)`);
    console.log(`   Quality: ${result.quality}/5`);
    console.log(`   Efficiency: ${result.efficiency.toFixed(2)}`);

    // Show next test
    setTimeout(() => {
      this.displayNextTest(plan);
    }, 1000);
  }

  generateReport() {
    if (this.results.length === 0) {
      console.log('No results to report yet.');
      return;
    }

    console.log('\n' + '='.repeat(60));
    console.log('📊 MCP TOKEN USAGE REPORT');
    console.log('='.repeat(60) + '\n');

    // Group by server
    const byServer = {};
    this.results.forEach(r => {
      const server = r.serverUsed || r.server;
      if (!byServer[server]) {
        byServer[server] = [];
      }
      byServer[server].push(r);
    });

    // Calculate stats per server
    Object.entries(byServer).forEach(([server, results]) => {
      const totalTokens = results.reduce((sum, r) => sum + r.totalTokens, 0);
      const avgTokens = totalTokens / results.length;
      const avgQuality = results.reduce((sum, r) => sum + r.quality, 0) / results.length;
      const avgEfficiency = results.reduce((sum, r) => sum + r.efficiency, 0) / results.length;

      console.log(`\n🔧 ${server.toUpperCase()}`);
      console.log(`   Tests run: ${results.length}`);
      console.log(`   Total tokens: ${totalTokens.toLocaleString()}`);
      console.log(`   Avg tokens/query: ${Math.round(avgTokens).toLocaleString()}`);
      console.log(`   Avg quality: ${avgQuality.toFixed(2)}/5`);
      console.log(`   Avg efficiency: ${avgEfficiency.toFixed(2)}`);
      console.log(`   Cost estimate: $${((totalTokens / 1000000) * 3).toFixed(4)}`); // Assuming $3/1M tokens
    });

    // Best performers
    console.log('\n\n🏆 BEST PERFORMERS\n');

    const bestEfficiency = this.results.sort((a, b) => b.efficiency - a.efficiency)[0];
    console.log(`   Most efficient: ${bestEfficiency.serverUsed || bestEfficiency.server}`);
    console.log(`   Query: "${bestEfficiency.query}"`);
    console.log(`   Efficiency: ${bestEfficiency.efficiency.toFixed(2)}\n`);

    const bestQuality = this.results.sort((a, b) => b.quality - a.quality)[0];
    console.log(`   Highest quality: ${bestQuality.serverUsed || bestQuality.server}`);
    console.log(`   Query: "${bestQuality.query}"`);
    console.log(`   Quality: ${bestQuality.quality}/5\n`);

    const leastTokens = this.results.sort((a, b) => a.totalTokens - b.totalTokens)[0];
    console.log(`   Least tokens: ${leastTokens.serverUsed || leastTokens.server}`);
    console.log(`   Query: "${leastTokens.query}"`);
    console.log(`   Tokens: ${leastTokens.totalTokens}\n`);

    // Export CSV
    this.exportCSV();
    console.log('\n📁 Full results saved to: mcp-test-results.json');
    console.log('📁 CSV exported to: mcp-test-results.csv\n');
  }

  exportCSV() {
    const csv = [
      ['Test ID', 'Phase', 'Category', 'Query', 'Server', 'Input Tokens', 'Output Tokens', 'Total Tokens', 'Quality', 'Efficiency', 'Timestamp'].join(','),
      ...this.results.map(r => [
        r.id,
        r.phase,
        r.category,
        `"${r.query}"`,
        r.serverUsed || r.server,
        r.inputTokens,
        r.outputTokens,
        r.totalTokens,
        r.quality,
        r.efficiency.toFixed(2),
        r.timestamp
      ].join(','))
    ].join('\n');

    fs.writeFileSync(path.join(__dirname, 'mcp-test-results.csv'), csv);
  }

  reset() {
    if (fs.existsSync(this.resultsFile)) {
      fs.unlinkSync(this.resultsFile);
    }
    this.results = [];
    console.log('✅ Test results reset');
  }
}

// CLI
const tester = new MCPTokenTest();
const args = process.argv.slice(2);
const command = args[0];

switch (command) {
  case 'start':
    console.log('🚀 Starting MCP Token Usage Experiment...\n');
    const plan = tester.generateTestPlan();
    console.log(`Total tests to run: ${plan.length}\n`);
    tester.displayNextTest(plan);
    break;

  case 'record':
    const [inputTokens, outputTokens, quality, serverUsed] = args.slice(1);
    if (!inputTokens || !outputTokens || !quality) {
      console.log('❌ Usage: node mcp-token-test.js record <inputTokens> <outputTokens> <quality> [serverUsed]');
      process.exit(1);
    }
    tester.recordResult(inputTokens, outputTokens, quality, serverUsed);
    break;

  case 'report':
    tester.generateReport();
    break;

  case 'reset':
    tester.reset();
    break;

  case 'next':
    const nextPlan = tester.generateTestPlan();
    tester.displayNextTest(nextPlan);
    break;

  default:
    console.log('MCP Token Usage Experiment');
    console.log('\nCommands:');
    console.log('  start           - Start the experiment and show first test');
    console.log('  record <i> <o> <q> [s] - Record result (input tokens, output tokens, quality 1-5, optional server)');
    console.log('  next            - Show next test');
    console.log('  report          - Generate final report');
    console.log('  reset           - Clear all results and start over');
    console.log('\nExample workflow:');
    console.log('  1. node mcp-token-test.js start');
    console.log('  2. Run the test query in Claude Code');
    console.log('  3. node mcp-token-test.js record 1500 3200 5');
    console.log('  4. Repeat for each test');
    console.log('  5. node mcp-token-test.js report');
}
