def insert(intervals, new_interval):
    merged = []
    for interval in intervals:
        if new_interval[0] <= interval[1]:
            interval[0] = min(interval[0], new_interval[0])
            interval[1] = max(interval[1], new_interval[1])
            return mergeOverlappingIntervals(intervals)
        else:
            merged.append(interval)
    return merged


def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda interval: interval[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        merged_end = merged[-1][1]
        if start <= merged_end:
            merged[-1][1] = max(merged_end, end)
        else:
            merged.append([start, end])
    return merged

def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
