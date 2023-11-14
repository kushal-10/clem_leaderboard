TITLE = """<h1 align="center" id="space-title"> CLEM Leaderboard</h1>"""

INTRODUCTION_TEXT = """
📐 The CLEM Leaderboard aims to track, rank and evaluate current cLLMs (chat-optimized Large Language Models, “clems”) as described in [Clembench: Using Game Play to Evaluate Chat-Optimized Language Models as Conversational Agents](https://arxiv.org/abs/2305.13455).
"""

LLM_BENCHMARKS_TEXT = f"""

# clembench: A Framework for the Systematic Evaluation of Chat-Optimized Language Models as Conversational Agents

> Chalamalasetti, K., Götze, J., Hakimov, S., Madureira, B., Sadler, P., & Schlangen, D. (2023). clembench: Using Game Play to Evaluate Chat-Optimized Language Models as Conversational Agents. [PDF](https://doi.org/10.48550/arXiv.2305.13455)

Recent work has proposed a methodology for
the systematic evaluation of “Situated Language Understanding Agents”—agents that
operate in rich linguistic and non-linguistic
contexts—through testing them in carefully
constructed interactive settings. Other recent
work has argued that Large Language Models
(LLMs), if suitably set up, can be understood
as (simulators of) such agents. A connection
suggests itself, which this paper explores: Can
LLMs be evaluated meaningfully by exposing
them to constrained game-like settings that are
built to challenge specific capabilities?

 As a
proof of concept, this paper investigates five
interaction settings, showing that current cLLMs (chat-optimized Large Language Models, "clems") are, 
to an extent, capable of
following game-play instructions. Both this
capability and the quality of the game play,
measured by how well the objectives of the
different games are met, follows the development cycle, with newer models generally performing better. 
The metrics even for the comparatively simple example games are far from
being saturated, suggesting that the proposed
instrument will remain to have diagnostic value.

More information about running the benchmark and details about the games can be found [here](https://github.com/clembench/clembench)

Additional Details about the results can be found [here](https://github.com/clembench/clembench-runs)


"""