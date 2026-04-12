"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS =   "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  =  """There are currently no Edinburgh venues available that can accommodate 300 people with vegan menu options. Would you like to:

1. Search for venues with a lower minimum capacity?
2. Consider venues without vegan menu requirements?
3. Check availability for a different date?

Let me know how you'd like to adjust your search criteria."""

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
The result came back with only 1 choice, so the model went for that venue. the chosen venue stayed the same, no change there, so the files didn't have to be updated
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 283   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 220   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
1. One source, many consumers. The same MCP server can be called by LangGraph agent and a CLI script simultaneously, without any of them sharing code.
2. Dynamic discovery. Add a new @mcp.tool() to mcp_venue_server.py and every client picks it up automatically on next connection — no changes to exercise4_mcp_client.py.
3. The experiment proves the real point. When I changed The Albanach's status to full, the agent's answer changed accordingly without touching any agent code. 
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- FILL ME IN
- FILL ME IN
- FILL ME IN
- FILL ME IN
- FILL ME IN
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
FILL ME IN
"""
