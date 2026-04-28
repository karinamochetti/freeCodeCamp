def favorite_songs(playlist):
    sorted_playlist = sorted(playlist, key=lambda x: x['plays'])
    top2 = [sorted_playlist[-1]["title"], sorted_playlist[-2]["title"]]
    return top2

print(favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]))
print(favorite_songs([{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100} ]))
print(favorite_songs([{"title": "Song A", "plays": 42}, {"title": "Song B", "plays": 99}, {"title": "Song C", "plays": 75} ]))
