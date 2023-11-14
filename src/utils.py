import pandas as pd

def update_list(LIST: list) -> list:
    update = ['Model', 'Clemscore', 'All(Played)', 'All(Quality Score)']
    game_metrics = LIST[4:]
    for i in range(len(game_metrics)):
        if i%3 == 0:
            game = game_metrics[i]
            print(game)
            update.append(str(game).capitalize + "(Played)")
            update.append(str(game).capitalize + "(Quality Score)") 
            update.append(str(game).capitalize + "(Quality Score[std])")

    return update


