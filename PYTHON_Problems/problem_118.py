# Problem 118: Given a list of intervals, merge all overlapping intervals.
# Example: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
