import os
import datetime
from datetime import datetime, timezone, timedelta

LOGGER_PATH = os.path.join(".","modules", "logger", "log")

def log(msg, specie="INFO"):
    with open(LOGGER_PATH, 'a') as file:
        time_act = datetime.now().astimezone(timezone(timedelta(hours=-3)))
        time_act = time_act.strftime('%d/%m/%Y %H:%M:%S')
        final_msg = f"{time_act} - [{specie.upper()}]: {msg}\n"
        file.write(final_msg)
        
def clear(reason, specie="INFO"):
    with open(LOGGER_PATH, 'w') as file:
        time_act = datetime.now().astimezone(timezone(timedelta(hours=-3)))
        time_act = time_act.strftime('%d/%m/%Y %H:%M:%S')
        final_msg = f"{time_act} - [{specie.upper()}]: {reason}\n"
        file.write(final_msg)