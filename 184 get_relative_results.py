def get_relative_results(results):

    def convert_to_sec(value):
        return int(value[0])*3600 + int(value[2:4])*60 + int(value[5:7])
    
    def convert_to_min(sec):
        return f"{(sec//60):01d}:{(sec%60):02d}"
    
    time_behind = ["0"]
    first_play = convert_to_sec(results[0])
    for result in results[1:]:
        time_behind.append("+" + convert_to_min(convert_to_sec(result)-first_play))

    return time_behind

print(get_relative_results(["1:25:32", "1:26:10", "1:27:05"]))
print(get_relative_results(["1:00:01", "1:00:05", "1:00:10"]))
print(get_relative_results(["1:10:06", "1:10:23", "1:10:48", "1:12:11"]))
print(get_relative_results(["0:49:13", "0:49:15", "0:50:14", "0:51:30", "0:51:58", "0:52:16", "0:53:12", "0:53:31", "0:56:19", "1:02:20"]))
print(get_relative_results(["2:01:15", "2:10:45", "2:10:53", "2:11:04", "2:11:55", "2:13:27", "2:14:30", "2:15:10"]))
