from random import randint

def classifica_times(times):
    """Classifica times de acordo com os critérios de desempate."""
    times.sort(key=lambda time: (-time[1], -time[2], -time[3], -time[4], randint(0, 1000)), reverse=False)
    return times
