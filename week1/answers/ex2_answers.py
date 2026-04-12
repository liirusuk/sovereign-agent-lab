"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ['check_pub_availability', 'check_pub_availability', 'get_edinburgh_weather', 'calculate_catering_cost', 'generate_event_flyer']

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = False

TASK_A_NOTES = "Needed to change a model and a code a bit, because the tools were not called. It's an indoor event :)"   # optional — anything unexpected

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True   # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "file:///C:/Users/user/Downloads/text2img-e45a5239-c77a-4314-b3d0-52453b78ef8d_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
Okay, let's see. The user wanted to check The Bow Bar for 160 vegan guests. The response from the tool says that The Bow Bar has a capacity of 80, which is less than the required 160. So it doesn't meet the capacity requirement. The vegan option is available, but since the capacity isn't enough, the overall status is "full" and meets_all_constraints is false.
Now, the user's instruction was to check The Bow Bar first, and if it doesn't work, check any other available venue. So I need to move on to the next venue. The known venues are The Albanach, The Haymarket Vaults, The Guilford Arms, and The Bow Bar. Since The Bow Bar is already checked, I should check the others in order. Let's start with The Albanach. 
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
None of the known Edinburgh venues can accommodate 300 people while meeting all requirements. The maximum capacity among the checked venues is 200 (The Guilford Arms), but it lacks vegan options. The other venues with vegan options (The Albanach, Haymarket Vaults, Bow Bar) have capacities of 180, 160, and 80 respectively. Would you like to consider alternative solutions like splitting the event across multiple venues or adjusting the guest count?
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = """I don't have access to real-time train schedules or transportation data. For the most accurate information about the last train from Edinburgh Waverley to London, I recommend checking:
1. The National Rail website (www.nationalrail.co.uk)
2. Train service apps like Citymapper or Trainline
3. The specific train operator's website (e.g., LNER)
Would you like help with anything related to Edinburgh pubs, event planning, or local weather instead?"""

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
I think this is very good. It recommended the websites and tools to try and did not try to go for the tooling when not needed. I'm very impressed but it going an extra mile and recommending additional tooling it knows about without asking.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
graph TD;
	__start__([<p>__start__</p>]):::first
	agent(agent)
	tools(tools)
	__end__([<p>__end__</p>]):::last
	__start__ --> agent;
	agent -.-> __end__;
	agent -.-> tools;
	tools --> agent;
	classDef default fill:#f2f0ff,line-height:1.2
	classDef first fill-opacity:0
	classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/flows.yml. Min 30 words.
TASK_D_COMPARISON = """
In LangGraph it seems that the flow is determined by the agent every time: depending on what it thinks - it will choose either to use an additional tool and go into the loop or to return an answer. 
Rasa Pro CALM is more deterministic: it has all steps defined and doesn't decide when to stop and when to proceed.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
I was mostly surprised how the model handled the out of scope scenario: it did not hallucinate, did not keep trying to solve the task - in a straight manner it returned basically an out of scope message, but suggested workarounds. That was pleasant, that we did not have to think about it while programming the agent.
"""
