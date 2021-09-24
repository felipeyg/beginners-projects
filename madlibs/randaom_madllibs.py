from samples_madlibs import anitta, bolsonaro, latino
import random

if __name__ == '__main__':
    m = random.choice([anitta, bolsonaro, latino])
    m.madlib()