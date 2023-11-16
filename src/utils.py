import os
import pandas as pd


def update_cols(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Change three header rows to a single header row
    Args:
        df: Raw dataframe containing 3 separate header rows
            Remove this function if the dataframe has only one header row

    Returns:
        df: Updated dataframe which has only 1 header row instead of 3
    '''
    default_cols = list(df.columns)

    # First 4 columns are initalised in 'update', Append additional columns for games Model, Clemscore, ALL(PLayed) and ALL(Main Score)
    update = ['Model', 'Clemscore', 'All(Played)', 'All(Quality Score)']
    game_metrics = default_cols[4:]

    # Change columns Names for each Game
    for i in range(len(game_metrics)):
        if i%3 == 0:
            game = game_metrics[i]
            update.append(str(game).capitalize() + "(Played)")
            update.append(str(game).capitalize() + "(Quality Score)") 
            update.append(str(game).capitalize() + "(Quality Score[std])")

    # Create a dict to change names of the columns
    map_cols = {}
    for i in range(len(default_cols)):
        map_cols[default_cols[i]] = str(update[i])

    df = df.rename(columns=map_cols)
    df = df.iloc[2:]

    return df

def process_df(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Process dataframe - Remove repition in model names, convert datatypes to sort by "float" instead of "str"
    Args:
        df: Unprocessed Dataframe (after using update_cols)
    Returns:
        df: Processed Dataframe
    '''

    # Change column type to float from str
    list_column_names = list(df.columns)
    model_col_name = list_column_names[0]
    for col in list_column_names:
        if col != model_col_name:
            df[col] = df[col].astype(float)

    # Remove repetition in model names, if any
    models_list = []
    for i in range(len(df)):
        model_name = df.iloc[i][model_col_name]
        splits = model_name.split('--')
        splits = [split.replace('-t0.0', '') for split in splits] # Comment to not remove -t0.0
        if splits[0] == splits[1]:
            models_list.append(splits[0])
        else:
            models_list.append(splits[0] + "--" + splits[1])
    df[model_col_name] = models_list
    
    return df

def get_data(path, flag):
    '''
    Get a list of all version names and respective Dataframes 
    Args: 
        path: Path to the directory containing CSVs of different versions -> v0.9.csv, v1.0.csv, ....
        flag: Set this flag to include the latest version in Details and Versions tab
    Returns: 
        latest_df: singular list containing dataframe of the latest version of the leaderboard with only 4 columns 
        latest_vname: list of the name of latest version 
        previous_df: list of dataframes for previous versions (can skip latest version if required) 
        previous_vname: list of the names for the previous versions (INCLUDED IN Details and Versions Tab)

    '''
    # Check if Directory is empty
    list_versions = os.listdir(path)
    if not list_versions:
        print("Directory is empty")

    else:
        files = [file for file in list_versions if file.endswith('.csv')]
        files.sort(reverse=True)
        file_names = [os.path.splitext(file)[0] for file in files]

        DFS = []
        for file in files:
            df = pd.read_csv(os.path.join(path, file))
            df = update_cols(df) # Remove if by default there is only one header row
            df = process_df(df) # Process Dataframe
            df = df.sort_values(by=list(df.columns)[1], ascending=False) # Sort by clemscore
            DFS.append(df)

        # Only keep relavant columns for the main leaderboard
        latest_df_dummy = DFS[0]
        all_columns = list(latest_df_dummy.columns)
        keep_columns = all_columns[0:4]
        latest_df_dummy = latest_df_dummy.drop(columns=[c for c in all_columns if c not in keep_columns])

        latest_df = [latest_df_dummy]
        latest_vname = [file_names[0]]
        previous_df = []
        previous_vname = []
        for df, name in zip(DFS, file_names):
            previous_df.append(df)
            previous_vname.append(name) 
        
        if not flag:
            previous_df.pop(0)
            previous_vname.pop(0)

        print(latest_df[0].columns, previous_df[0].columns)
        return latest_df, latest_vname, previous_df, previous_vname
    
    return None

# get_data('versions', True)