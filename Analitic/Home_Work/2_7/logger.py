from datetime import datetime as dt
path = 'log.txt'
def log(string):
    logging = f'{dt.now()} | {string}\n'
    with open(path, 'a') as data:
        data.write(logging)