from collections import defaultdict


def tally(tournament_results):
    teams = defaultdict(list)
    matches = tournament_results.splitlines()
    results = list()
    all_teams_names = set()
    for match in matches:
        m = match.split(';')
        results.append([m[0], m[1], m[2]])
        all_teams_names = all_teams_names.union({m[0], m[1]})
    # initialize the teams
    for team in all_teams_names:
        teams[team] = (list(map(int, '00000')))
    # tallying the scores
    for res in results:
        teams[res[0]][0] += 1
        teams[res[1]][0] += 1
        if res[-1] == 'win':
            teams[res[0]][1] += 1
            teams[res[0]][4] += 3
            teams[res[1]][3] += 1
        elif res[-1] == 'loss':
            teams[res[0]][3] += 1
            teams[res[1]][1] += 1
            teams[res[1]][4] += 3
        else:
            teams[res[0]][2] += 1
            teams[res[1]][2] += 1
            teams[res[0]][4] += 1
            teams[res[1]][4] += 1
    # sort the teams by teams' name first , then sort teams by Points
    team_names = sorted(sorted(teams), key=lambda x: teams[x][4], reverse=True)
    table = 'Team                           | MP |  W |  D |  L |  P'
    for team in team_names:
        table += f'\n{team:31}|  {teams[team][0]} |  {teams[team][1]} |' \
            fr'  {teams[team][2]} |  {teams[team][3]} |  {teams[team][4]}'
    return table

