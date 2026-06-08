def get_movie_night_cost(day, showtime, number_of_tickets):

    SALEDAY = ["Tuesday"]
    WEEKDAY = ["Monday", "Wednesday", "Thursday"]
    WEEKEND = ["Friday", "Saturday", "Sunday"]

    if day in SALEDAY:
        cost = 5.0
    if day in WEEKDAY:
        cost = 10.0
    if day in WEEKEND:
        cost = 12.0

    time = showtime.split(":")
    hour = int(time[0])
    if time[1][2] == "p":
        hour += 12

    if hour < 17 and day not in SALEDAY:
        cost -= 2

    return f"${cost*number_of_tickets:.2f}"

print(get_movie_night_cost("Saturday", "10:00pm", 1))
print(get_movie_night_cost("Sunday", "10:00am", 1))
print(get_movie_night_cost("Tuesday", "7:20pm", 2))
print(get_movie_night_cost("Wednesday", "5:40pm", 3))
print(get_movie_night_cost("Monday", "11:50am", 4))
print(get_movie_night_cost("Friday", "4:30pm", 5))
print(get_movie_night_cost("Tuesday", "11:30am", 1))
