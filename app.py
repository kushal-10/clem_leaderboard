import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gradio as gr

from src.assets.text_content import TITLE, INTRODUCTION_TEXT, LLM_BENCHMARKS_TEXT
from src.utils import update_cols, split_cols

########### OVERALL LEADERBOARD ##################
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

############# PLOTS ######################
global plot_df
plot_df = pd.read_csv('detailed-bench-stats.csv')
GAME_COLS = list(plot_df['game'].unique())
global MODEL_COLS
MODEL_COLS = list(plot_df['model'].unique())


def plot_line(models, game):
    df = plot_df
    df = df[df['metric'] == 'Main Score']
    df = df[df['game'] == game]
    df = df[df['model'].isin(models)]

    X = df['experiment'].unique()
    Y = []
    labels = []
    for m in models:
        model_df = df[df['model'] == m]
        y = list(model_df['mean'])
        nan_flag = False
        for val in y:
            if np.isnan(val):
                nan_flag = True
        if not nan_flag:
            Y.append(y)
            labels.append(str(m))

    fig = plt.figure()
    for i in range(len(Y)):
        if len(Y[i]) != 0:
            plt.plot(X, Y[i], label=labels[i], marker='o')
    
    title_str = "Main Scores of each experiment in " + str(game) 
    plt.xlabel('Experiments')
    plt.ylabel('Main Score')
    plt.title(title_str)
    plt.legend()
    plt.show()
    return fig


############# MAIN APPLICATION ######################
demo = gr.Blocks()
with demo:
    gr.HTML(TITLE)
    gr.Markdown(INTRODUCTION_TEXT, elem_classes="markdown-text")

    with gr.Tabs(elem_classes="tab-buttons") as tabs:
        with gr.TabItem("🥇 Clem Leaderboard", elem_id="llm-benchmark-tab-table", id=0):
                        
            leaderboard_table = gr.components.Dataframe(
                value=overall_df,
                elem_id="leaderboard-table",
                interactive=False,
                visible=True,
            )
                
        with gr.TabItem("📈 Plot Lines", id=4):
            with gr.Row():
                game_cols = gr.Radio(
                    GAME_COLS, label="Select Game 🎮"
                )
            with gr.Row():
                model_cols = gr.CheckboxGroup(
                    MODEL_COLS, 
                    label="Select Models 🤖", 
                    value=[],
                    elem_id="column-select",
                    interactive=True,
                )

            with gr.Row():
                # Output block for the plot
                plot_output = gr.Plot()

            model_cols.change(
                plot_line,
                [model_cols, game_cols],
                plot_output,
                queue=True
            )

            game_cols.change(
                plot_line,
                [model_cols, game_cols],
                plot_output,
                queue=True
            )

        with gr.TabItem("📋 About", elem_id="llm-benchmark-tab-table", id=2):
            gr.Markdown(LLM_BENCHMARKS_TEXT, elem_classes="markdown-text")

    demo.load()
demo.queue()
demo.launch()