import pandas as pd
import os
from datetime import datetime, timezone

import gradio as gr
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from huggingface_hub import HfApi, snapshot_download

from src.assets.css_html_js import custom_css, get_window_url_params
from src.assets.text_content import TITLE, INTRODUCTION_TEXT
from src.config import MODEL_DEFINITIONS

import numpy as np

########### PRE APPLICATION STEPS ##################
# Paths
RESULTS_PATH = os.path.join("results_eval", "results_eval")
OVERALL_SCORES = os.path.join(RESULTS_PATH, "results_eval", "episode-level", "tables", "bench-paper-table.csv")

# Get list of games
list_games = os.listdir(RESULTS_PATH)
if os.path.exists(os.path.join(RESULTS_PATH, ".DS_Store")):
    list_games.remove(".DS_Store")
if os.path.exists(os.path.join(RESULTS_PATH, "results_eval")):
    list_games.remove("results_eval")
#Save a copy
LIST_GAMES = list_games
LIST_GAMES.append("All")

# Format dataframe to change two rows per model to a single row
def format_df(dataframe, col):
    unique_cols = dataframe[col].unique()
    unique_blocks = []
    new_cols = ['model']
    for u in unique_cols:
        unique_df = dataframe[dataframe[col]==u]
        unique_df = unique_df.drop(columns=['model', col])
        unique_df_cols = unique_df.columns
        [new_cols.append(str(c) + " (" + str(u) + ")" )for c in unique_df_cols]
        unique_arr = unique_df.to_numpy()
        unique_blocks.append(unique_arr)

    init_arr = dataframe['model'].unique()
    init_arr = init_arr.reshape((len(init_arr), 1))

    for block in unique_blocks:
        init_arr = np.hstack((init_arr, block))

    formatted_df = pd.DataFrame(data=init_arr, columns=new_cols)

    return formatted_df

# Get Overall Results Dataframe
global overall_df
# overall_df = pd.read_csv(OVERALL_SCORES)
overall_df = pd.read_csv('results.csv')
# TOTAL_COLS = len(list(overall_df.columns)[2:])
# overall_df = overall_df.replace()
# combine_col = 'metric'
# overall_df = format_df(overall_df, combine_col)
# show_cols = list(overall_df.columns)[1:]
# show_cols = list(overall_df.columns)


    
# Update the dataframe based on selected columns
def update_table(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    add_model_col = ['model']
    # Maintain order of the table
    cols = add_model_col + cols
    return overall_df[cols]
    
# Get last metric for all games
# selected_cols = show_cols[-TOTAL_COLS:]
############# MAIN APPLICATION ######################
demo = gr.Blocks()
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

                    # with gr.Row():
                    #     shown_columns = gr.CheckboxGroup(
                    #         choices=show_cols,
                    #         value=selected_cols,
                    #         label="Select columns to show",
                    #         elem_id="column-select",
                    #         interactive=True,
                    #     )     
            # leaderboard_table = gr.components.Dataframe(
            #     value=overall_df[
            #         ['model'] + shown_columns.value
            #     ],
            #     elem_id="leaderboard-table",
            #     interactive=False,
            #     visible=True,
            # )
            leaderboard_table = gr.components.Dataframe(
                value=overall_df,
                elem_id="leaderboard-table",
                interactive=False,
                visible=True,
            )

            # shown_columns.change(
            #     update_table,
            #     [leaderboard_table, shown_columns],
            #     leaderboard_table,
            #     queue=True,
            # )


    demo.load()
demo.queue()
demo.launch()