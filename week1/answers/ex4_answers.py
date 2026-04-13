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
- The MCP Venue Server (mcp_venue_server.py) acts as the shared tool layer for all
  agent components, exposing venue lookup, weather, and booking capabilities over a
  stable interface so that both the planner and Rasa action server can consume the
  same tools without duplicating logic.

- The Planner (planner.py) uses DeepSeek R1 as a dedicated thinking model to
  decompose an incoming task — such as a WhatsApp booking request — into an ordered
  sequence of sub-goals, because separating high-level reasoning from execution
  keeps the planning step auditable and prevents the fast worker from wasting tokens
  on strategy.

- The Executor (executor.py) runs a Llama 70B model in a ReAct loop to carry out
  each step the Planner emits, invoking real tools like web search, file I/O, and
  booking confirmation, because a fast and cheap model is appropriate for
  deterministic tool-calling once the plan is already fixed.

- The Memory layer (claude_md.py and vector_store.py) persists the agent's knowledge
  across sessions — CLAUDE.md for structured filesystem memory and a vector store for
  RAG retrieval — so the agent can recall previous Edinburgh searches and past booking
  outcomes rather than starting from scratch on every invocation.

- The Trigger and Notification layer (WhatsApp / file watch / API call + summary
  dispatch) serves as both the entry point and the exit point of the autonomous loop,
  receiving the user's task while they sleep and delivering a structured summary upon
  completion, making the agent genuinely headless rather than requiring a human in
  the loop at either end.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """

"""
