def solution(players, callings):
    answer = []
    player_dict = {}
    for index, name in enumerate(players):
        player_dict[name] = index
    
    for name in callings:
        idx = player_dict[name]
        pass_name = players[idx-1]
        player_dict[name] -= 1
        player_dict[pass_name] += 1
        
        players[idx-1], players[idx] = players[idx], players[idx-1]
    
    answer=players
    return answer