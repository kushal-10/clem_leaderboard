import pandas as pd
import os
from datetime import datetime, timezone

import gradio as gr
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from huggingface_hub import HfApi, snapshot_download

from src.assets.css_html_js import custom_css
from src.assets.text_content import TITLE, INTRODUCTION_TEXT
from src.config import MODEL_DEFINITIONS

########### PRE APPLICATION STEPS ##################
# Paths
RESULTS_PATH = os.path.join("results_eval", "results_eval")
OVERALL_SCORES = os.path.join(RESULTS_PATH, "results_eval", "episode-level", "tables", "scores_raw.csv")
TABOO_SCORES = os.path.join(RESULTS_PATH, "taboo", "results_eval", "episode-level", "tables", "tabootaboo-overview-table.csv")

# Get Overall Results Dataframe
overall_df = pd.read_csv(OVERALL_SCORES)

# Get Taboo DF for test
taboo_df = pd.read_csv(TABOO_SCORES)


# MAIN APPLICATION
demo = gr.Blocks(css=custom_css)
with demo:
    gr.HTML(TITLE)
    gr.Markdown(INTRODUCTION_TEXT, elem_classes="markdown-text")

    with gr.Tabs(elem_classes="tab-buttons") as tabs:
        with gr.TabItem("🏅 LLM Benchmark", elem_id="llm-benchmark-tab-table", id=0):
            with gr.Row():
                with gr.Column():
                    with gr.Row():
                        search_bar = gr.Textbox(
                            placeholder=" 🔍 Search for your model (separate multiple queries with `;`) and press ENTER...",
                            show_label=False,
                            elem_id="search-bar",
                        )
                    with gr.Row():
                        gr.Dropdown(
                                ["ran", "swam", "ate", "slept"], value=["swam", "slept"], multiselect=True, label="Activity", info=""
                            )
     
#             leaderboard_table = gr.components.Dataframe(
#                 value=leaderboard_df[
#                     [AutoEvalColumn.model_type_symbol.name, AutoEvalColumn.model.name]
#                     + shown_columns.value
#                     + [AutoEvalColumn.dummy.name]
#                 ],
#                 headers=[
#                     AutoEvalColumn.model_type_symbol.name,
#                     AutoEvalColumn.model.name,
#                 ]
#                 + shown_columns.value
#                 + [AutoEvalColumn.dummy.name],
#                 datatype=TYPES,
#                 max_rows=None,
#                 elem_id="leaderboard-table",
#                 interactive=False,
#                 visible=True,
#             )

#             # Dummy leaderboard for handling the case when the user uses backspace key
#             hidden_leaderboard_table_for_search = gr.components.Dataframe(
#                 value=original_df,
#                 headers=COLS,
#                 datatype=TYPES,
#                 max_rows=None,
#                 visible=False,
#             )
#             search_bar.submit(
#                 update_table,
#                 [
#                     hidden_leaderboard_table_for_search,
#                     shown_columns,
#                     filter_columns_type,
#                     filter_columns_precision,
#                     filter_columns_size,
#                     deleted_models_visibility,
#                     search_bar,
#                 ],
#                 leaderboard_table,
#             )
#             shown_columns.change(
#                 update_table,
#                 [
#                     hidden_leaderboard_table_for_search,
#                     shown_columns,
#                     filter_columns_type,
#                     filter_columns_precision,
#                     filter_columns_size,
#                     deleted_models_visibility,
#                     search_bar,
#                 ],
#                 leaderboard_table,
#                 queue=True,
#             )
#             filter_columns_type.change(
#                 update_table,
#                 [
#                     hidden_leaderboard_table_for_search,
#                     shown_columns,
#                     filter_columns_type,
#                     filter_columns_precision,
#                     filter_columns_size,
#                     deleted_models_visibility,
#                     search_bar,
#                 ],
#                 leaderboard_table,
#                 queue=True,
#             )
#             filter_columns_precision.change(
#                 update_table,
#                 [
#                     hidden_leaderboard_table_for_search,
#                     shown_columns,
#                     filter_columns_type,
#                     filter_columns_precision,
#                     filter_columns_size,
#                     deleted_models_visibility,
#                     search_bar,
#                 ],
#                 leaderboard_table,
#                 queue=True,
#             )
#             filter_columns_size.change(
#                 update_table,
#                 [
#                     hidden_leaderboard_table_for_search,
#                     shown_columns,
#                     filter_columns_type,
#                     filter_columns_precision,
#                     filter_columns_size,
#                     deleted_models_visibility,
#                     search_bar,
#                 ],
#                 leaderboard_table,
#                 queue=True,
#             )
#             deleted_models_visibility.change(
#                 update_table,
#                 [
#                     hidden_leaderboard_table_for_search,
#                     shown_columns,
#                     filter_columns_type,
#                     filter_columns_precision,
#                     filter_columns_size,
#                     deleted_models_visibility,
#                     search_bar,
#                 ],
#                 leaderboard_table,
#                 queue=True,
#             )

#         with gr.TabItem("📈 Metrics evolution through time", elem_id="llm-benchmark-tab-table", id=4):
#             with gr.Row():
#                 with gr.Column():
#                     chart = create_metric_plot_obj(
#                         plot_df,
#                         ["Average ⬆️"],
#                         HUMAN_BASELINES,
#                         title="Average of Top Scores and Human Baseline Over Time",
#                     )
#                     gr.Plot(value=chart, interactive=False, width=500, height=500)
#                 with gr.Column():
#                     chart = create_metric_plot_obj(
#                         plot_df,
#                         ["ARC", "HellaSwag", "MMLU", "TruthfulQA"],
#                         HUMAN_BASELINES,
#                         title="Top Scores and Human Baseline Over Time",
#                     )
#                     gr.Plot(value=chart, interactive=False, width=500, height=500)
#         with gr.TabItem("📝 About", elem_id="llm-benchmark-tab-table", id=2):
#             gr.Markdown(LLM_BENCHMARKS_TEXT, elem_classes="markdown-text")