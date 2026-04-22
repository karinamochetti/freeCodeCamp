def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    convert_b = {"B": 1, "KB": 1000, "MB": 1000000, "GB": 1000000000, "TB": 1000000000000}
    if video_unit not in ["B", "KB", "MB", "GB"]:
        return "Invalid video unit"
    if drive_unit not in ["GB", "TB"]:
        return "Invalid drive unit"
    return (drive_size*convert_b[drive_unit])//(video_size*convert_b[video_unit])

print(number_of_videos(500, "MB", 100, "GB"))
print(number_of_videos(1, "TB", 10, "TB"))
print(number_of_videos(2000, "MB", 100000, "MB"))
print(number_of_videos(500000, "KB", 2, "TB"))
print(number_of_videos(1.5, "GB", 2.2, "TB"))
