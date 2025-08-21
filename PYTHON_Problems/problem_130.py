# Problem 130
# Given a list of intervals, merge overlapping intervals.
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start,end in intervals[1:]:
        last_end = merged[-1][1]
        if start<=last_end:
            merged[-1][1] = max(last_end,end)
        else:
            merged.append([start,end])
    return merged

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
