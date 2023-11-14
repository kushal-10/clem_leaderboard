import pandas as pd

def update_cols(df: pd.DataFrame) -> pd.DataFrame:
    default_cols = list(df.columns)
    update = ['Model', 'Clemscore', 'All(Played)', 'All(Quality Score)']
    game_metrics = default_cols[4:]
    for i in range(len(game_metrics)):
        if i%3 == 0:
            game = game_metrics[i]
            update.append(str(game).capitalize() + "(Played)")
            update.append(str(game).capitalize() + "(Quality Score)") 
            update.append(str(game).capitalize() + "(Quality Score[std])")

    map_cols = {}
    for i in range(len(default_cols)):
        map_cols[default_cols[i]] = str(update[i])

    df = df.rename(columns=map_cols)
    df = df.iloc[2:]

    return df

def split_cols(LIST: list):
    PL_COLS = []
    MS_COLS = []
    SD_COLS = []
    dummy = LIST[4:]
    for i in range(len(dummy)):
        if i%3 == 0:
            PL_COLS.append(dummy[i])
            MS_COLS.append(dummy[i+1])
            SD_COLS.append(dummy[i+2])

    AVG_COLS = LIST[1:4]
    SHOW_COLS = LIST[1:]

    return SHOW_COLS, PL_COLS, MS_COLS, SD_COLS, AVG_COLS


