import pandas as pd
import os
import numpy as np
import gradio as gr

from src.assets.text_content import TITLE, INTRODUCTION_TEXT, LLM_BENCHMARKS_TEXT
from src.utils import update_cols, split_cols, outbreak

########### PRE APPLICATION STEPS ##################
# Get Overall Results Dataframe
global overall_df
overall_df = pd.read_csv('results.csv')
overall_df = update_cols(overall_df)


# Divide columns
ALL_COLS = list(overall_df.columns)
SHOW_COLS, PL_COLS, MS_COLS, SD_COLS, AVG_COLS = split_cols(ALL_COLS)
# Initially select only the Averaged scores
SELECTED_COLS = AVG_COLS
global COLS

#Default sort by clemscore
overall_df = overall_df.sort_values(by=[ALL_COLS[1]], ascending=False)

# Update the dataframe based on selected columns
def update_table(avg_cols: list, sd_cols: list, pl_cols: list, ms_cols: list) -> pd.DataFrame:
    add_model_col = [ALL_COLS[0]]
    # Maintain order of the table
    COLS = add_model_col + avg_cols + ms_cols + pl_cols + sd_cols
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
                        avg_columns = gr.CheckboxGroup(
                            choices=AVG_COLS,
                            value=SELECTED_COLS,
                            label="Select columns to show : Averaged over all games",
                            elem_id="column-select",
                            interactive=True,
                        )  
                    with gr.Row():
                        ms_columns = gr.CheckboxGroup(
                            choices=MS_COLS,
                            value=[],
                            label="Select columns to show : Main Scores for each game",
                            elem_id="column-select",
                            interactive=True,
                        )  
                with gr.Column():                
                    with gr.Row():
                        pl_columns = gr.CheckboxGroup(
                            choices=PL_COLS,
                            value=[],
                            label="Select columns to show : %Played for each game",
                            elem_id="column-select",
                            interactive=True,
                        )  
                    with gr.Row():
                        sd_columns = gr.CheckboxGroup(
                            choices=SD_COLS,
                            value=[],
                            label="Select columns to show : Standard Deviation of Main Scores for each game",
                            elem_id="column-select",
                            interactive=True,
                        )     
            leaderboard_table = gr.components.Dataframe(
                value=overall_df[
                    [ALL_COLS[0]] + avg_columns.value + sd_columns.value + ms_columns.value + pl_columns.value
                ],
                elem_id="leaderboard-table",
                interactive=False,
                visible=True,
            )

            avg_columns.change(
                update_table,
                [avg_columns, sd_columns, pl_columns, ms_columns],
                leaderboard_table,
                queue=True,
            )

            ms_columns.change(
                update_table,
                [avg_columns, sd_columns, pl_columns, ms_columns],
                leaderboard_table,
                queue=True,
            )

            pl_columns.change(
                update_table,
                [avg_columns, sd_columns, pl_columns, ms_columns],
                leaderboard_table,
                queue=True,
            )

            sd_columns.change(
                update_table,
                [avg_columns, sd_columns, pl_columns, ms_columns],
                leaderboard_table,
                queue=True,
            )
                
        with gr.TabItem("📝 About", elem_id="llm-benchmark-tab-table", id=2):
            gr.Markdown(LLM_BENCHMARKS_TEXT, elem_classes="markdown-text")

        with gr.TabItem("📊 Plotting", id=3):
            with gr.Row():
                selected_columns = gr.CheckboxGroup(
                    ["USA", "Canada", "Mexico", "UK"], label="Countries", value=[]
                )

            with gr.Row():
                # Output block for the plot
                plot_output = gr.Plot()

            # Attach the plot_handler to the button click event
            selected_columns.change(
                outbreak,
                [selected_columns],
                plot_output,
                queue=True,
            )


        


    demo.load()
demo.queue()
demo.launch()