import pandas as pd
import os
import numpy as np
import gradio as gr

from src.assets.text_content import TITLE, INTRODUCTION_TEXT
from src.utils import update_cols

########### PRE APPLICATION STEPS ##################


# Get Overall Results Dataframe
global overall_df
overall_df = pd.read_csv('results.csv')
overall_df = update_cols(overall_df)
ALL_COLS = list(overall_df.columns)
SHOW_COLS = ALL_COLS[1:] 
SELECTED_COLS = SHOW_COLS[:3]
global COLS

# Update the dataframe based on selected columns
def update_table(cols: list) -> pd.DataFrame:
    add_model_col = [ALL_COLS[0]]
    # Maintain order of the table
    COLS = add_model_col + cols
    return overall_df[COLS]

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
                        shown_columns = gr.CheckboxGroup(
                            choices=SHOW_COLS,
                            value=SELECTED_COLS,
                            label="Select columns to show",
                            elem_id="column-select",
                            interactive=True,
                        )     
            leaderboard_table = gr.components.Dataframe(
                value=overall_df[
                    [ALL_COLS[0]] + shown_columns.value
                ],
                elem_id="leaderboard-table",
                interactive=False,
                visible=True,
            )

            shown_columns.change(
                update_table,
                [shown_columns],
                leaderboard_table,
                queue=True,
            )


    demo.load()
demo.queue()
demo.launch()