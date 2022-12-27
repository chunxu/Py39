# Rank Keys by Values
# Description
# Build a function RankK which takes a dictionary as input returns a list of keys which sorted by their values.

# Examples
# RankK({"a": 7, "b": 5, "c": 9}) returns ["b", "a", "c"]

def RankK(d):
    mydic= {k:v for k, v in sorted(d.items(), key=lambda item: item[1])}
    return list(mydic.keys())
    
    
    # easy
