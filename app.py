import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gradio as gr
import os

from src.assets.text_content import TITLE, INTRODUCTION_TEXT
from src.utils import get_data, compare_plots

############################ For Leaderboards #############################
DATA_PATH = 'versions'
latest_flag = True #Set flag to iclude latest data in Details and Versions Tab
latest_df, latest_vname, previous_df, previous_vname = get_data(DATA_PATH, latest_flag)

global prev_df
prev_df = previous_df[0]
def select_prev_df(name):
    ind = previous_vname.index(name)
    prev_df = previous_df[ind]
    return prev_df

############################ For Plots ####################################
global plot_df, MODEL_COLS
plot_df = latest_df[0]
MODEL_COLS = list(plot_df['Model'].unique())

# compare_plots(plot_df, ['claude-v1.3', 'falcon-40b', 'gpt-4', 'gpt-3.5-turbo--gpt-4', 'gpt-4--gpt-3.5-turbo', 'koala-13b', 'text-davinci-003'])

############# MAIN APPLICATION ######################
demo = gr.Blocks()
with demo:
    gr.HTML(TITLE)
    gr.Markdown(INTRODUCTION_TEXT, elem_classes="markdown-text")

    with gr.Tabs(elem_classes="tab-buttons") as tabs:
        with gr.TabItem("🥇 Clem Leaderboard", elem_id="llm-benchmark-tab-table", id=0):
                        
            leaderboard_table = gr.components.Dataframe(
                value=latest_df[0],
                elem_id="leaderboard-table",
                interactive=False,
                visible=True,
            )
                
        with gr.TabItem("📈 Plot", id=3):
            with gr.Row():
                model_cols = gr.CheckboxGroup(
                    MODEL_COLS, 
                    label="Select Models 🤖", 
                    value=[],
                    elem_id="column-select",
                    interactive=True,
                )

            with gr.Row():
                plot_grdf = gr.DataFrame(
                    value=plot_df,
                    visible=False
                )
            with gr.Row():
                # Output block for the plot
                plot_output = gr.Plot()

            model_cols.change(
                compare_plots,
                [plot_grdf, model_cols],
                plot_output,
                queue=True
            )

        with gr.TabItem("🔄 Versions and Details", elem_id="details", id=2):
            with gr.Row():
                ver_selection = gr.Dropdown(
                    previous_vname, label="Select Version 🕹️", value=previous_vname[0]
                )
            prev_table = gr.components.Dataframe(
                value=prev_df,
                elem_id="leaderboard-table",
                interactive=False,
                visible=True,
            )

            ver_selection.change(
                select_prev_df,
                [ver_selection],
                prev_table,
                queue=True
            )


    demo.load()
demo.queue()
demo.launch()