'''
roll parameters = {
    success_threshold: number for counting successes from,
    successes: number of successful rolls,
    failures: number of failed rolls,
    tens: number of max value rolls,
    results: array of (number of dice, [array of output rolls]
}'''

roll_parameters = {
    'success_threshold': 7,
    'successes': 0,
    'failures': 0,
    'tens': 0,
    'results': [(0, [0])]
}


def reset():
    global roll_parameters
    roll_parameters = {
        'success_threshold': 7,
        'successes': 0,
        'failures': 0,
        'tens': 0,
        'results': [(0, [0])]
    }