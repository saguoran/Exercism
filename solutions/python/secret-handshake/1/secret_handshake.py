def handshake(code):
    code = int(f"{code:b}")
    secrets = list()
    if code % 10 == 1:
        secrets.append('wink')
    if int(code % 100 / 10) == 1:
        secrets.append('double blink')
    if int(code % 1000 / 100) == 1:
        secrets.append('close your eyes')
    if int(code % 10000 / 1000) == 1:
        secrets.append('jump')
    if int(code / 10000) == 1:
        secrets.reverse()
    return secrets


def secret_code(actions: list):
    sorted_actions = ['wink', 'double blink', 'close your eyes', 'jump']
    match_actions = list()
    code = list()
    for action in reversed(sorted_actions):
        if action in actions:
            code.append(1)
            match_actions.append(action)
        else:
            code.append(0)
    try:
        if actions[0] != list(reversed(match_actions))[0]:
            code = [1] + code
    except IndexError:
        pass
    return int(''.join(str(n) for n in code), 2)




