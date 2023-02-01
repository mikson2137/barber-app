from datetime import timedelta

time_str = "0:144:10.014953"
time_components = time_str.split(":")

if len(time_components) == 3:
    hours = int(time_components[0])
    minutes = int(time_components[1])
    seconds = float(time_components[2])
    time_delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
elif len(time_components) == 2:
    minutes = int(time_components[0])
    seconds = float(time_components[1])
    time_delta = timedelta(minutes=minutes, seconds=seconds)
else:
    seconds = float(time_components[0])
    time_delta = timedelta(seconds=seconds)

if time_delta.days > 0:
    print(f"{time_delta.days} days")
elif time_delta.seconds >= 3600:
    print(f"{int(time_delta.seconds / 3600)} hours")
elif time_delta.seconds >= 60:
    print(f"{int(time_delta.seconds / 60)} minutes")
else:
    print(f"{time_delta.seconds} seconds")