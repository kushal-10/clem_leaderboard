TITLE = """<h1 align="center" id="space-title"> 🏆 CLEM Leaderboard</h1>"""

INTRODUCTION_TEXT = """
🔝 The CLEM Leaderboard aims to track, rank and evaluate current cLLMs (chat-optimized Large Language Models, “clems”) as described in [Clembench: Using Game Play to Evaluate Chat-Optimized Language Models as Conversational Agents](https://arxiv.org/abs/2305.13455).
"""

LLM_BENCHMARKS_TEXT = f"""

# clembench: A Framework for the Systematic Evaluation of Chat-Optimized Language Models as Conversational Agents

> Chalamalasetti, K., Götze, J., Hakimov, S., Madureira, B., Sadler, P., & Schlangen, D. (2023). clembench: Using Game Play to Evaluate Chat-Optimized Language Models as Conversational Agents. [PDF](https://doi.org/10.48550/arXiv.2305.13455)


### Abstract 📌
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

### Purpose 🎯
Newly proposed benchmarks such as AlpacaEval, Chatbot Arena, and Open LLM Leaderboard focus on comparing models outputs either running them on existing datasets, employ human annotators to choose which output is preferred, or simply ask another LLM to evaluate the outputs; these benchmarks do not test the interactive dialogue aspects of chat-based LLMs. The datasets for clem-bench have been created from scratch and adding new games or new instances to the existing games is easy to ensure continued fair benchmarking.

### Evaluation of models 📏
The leaderboard tracks the performance of a variety of language models, including both traditional rule-based models and more recent machine learning-based models like GPT-3. These models are tested on a variety of benchmarks that are designed to evaluate their ability to understand and respond to natural language input in interactive game-like settings. The benchmarks include tasks like describing images, playing games, and engaging in conversation with human players.

The leaderboard works by tracking the performance of different language models on the benchmarks that are being evaluated. Scores are calculated based on a variety of factors, including accuracy, speed, and efficiency.

More information about running the benchmark and details about the games can be found [here](https://github.com/clembench/clembench)

Additional Details about the results can be found [here](https://github.com/clembench/clembench-runs)

"""