import pandas as pd

def update_cols(df: pd.DataFrame) -> pd.DataFrame:
    default_cols = list(df.columns)
    update = ['Model', 'Clemscore', 'All(Played)', 'All(Quality Score)']
    game_metrics = default_cols[4:]
    for i in range(len(game_metrics)):
        if i%3 == 0:
            game = game_metrics[i]
            print(game)
            update.append(str(game).capitalize() + "(Played)")
            update.append(str(game).capitalize() + "(Quality Score)") 
            update.append(str(game).capitalize() + "(Quality Score[std])")

    map_cols = {}
    for i in range(len(default_cols)):
        map_cols[default_cols[i]] = str(update[i])

    df = df.rename(columns=map_cols)
    df = df.iloc[2:]

    return df


