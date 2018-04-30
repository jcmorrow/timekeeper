from datetime import datetime, date


def datetime_from_time_string(time_string):
    return datetime.strptime(today_as_string() + time_string,
                             "%d/%m/%y%H:%M:%S")


def today_as_string():
    return date.today().strftime("%d/%m/%y")


def compact_work_timestamps(timestamps):
    SECONDS_IN_A_MINUTE = 60
    times = list(map(datetime_from_time_string, timestamps))
    MAX_GAP = 5 * SECONDS_IN_A_MINUTE
    current_session = []
    sessions = [current_session]

    for time in times:
        if len(current_session) == 0:
            current_session.append(time)
            current_session.append(time)
        else:
            if (time - current_session[-1]).total_seconds() > MAX_GAP:
                sessions.append(current_session)
                current_session = [time, time]
            else:
                current_session[1] = time

    return sessions
