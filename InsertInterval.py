# O(n) time | O(n) space
def insert_my(intervals, new_interval):
    merged = []
    start, end = 0, 1
    new_interval_used = False
    for idx in range(len(intervals)):
        if not new_interval_used:
            if new_interval[start] <= intervals[idx][end]:
                intervals[idx][start] = min(intervals[idx][start], new_interval[start])
                intervals[idx][end] = max(intervals[idx][end], new_interval[end])
                merged.append(intervals[idx])
                new_interval_used = True
            else:
                merged.append(intervals[idx])
        else:
            if intervals[idx][start] <= merged[-end][end]:
                merged[-end][end] = max(intervals[idx][end], merged[-end][end])
            else:
                merged.append(intervals[idx])
    if not new_interval_used:
        merged.append(new_interval)
    return merged


# O(n) time | O(n) space
def insert(intervals, new_interval):
  merged = []
  i, start, end = 0, 0, 1

  # skip (and add to output) all intervals which end before the start of the new interval
  while i < len(intervals) and intervals[i][end] < new_interval[start]:
    merged.append(intervals[i])
    i += 1

  # merge all intervals that overlap with 'new_interval'
  while i < len(intervals) and intervals[i][start] <= new_interval[end]:
    new_interval[start] = min(intervals[i][start], new_interval[start])
    new_interval[end] = max(intervals[i][end], new_interval[end])
    i += 1

  # insert the new_interval
  merged.append(new_interval)

  # add all the remaining intervals to the output
  while i < len(intervals):
    merged.append(intervals[i])
    i += 1
  return merged


def main():
    # print("Intervals after inserting the new interval: " + str(insert([[1, 2], [3, 4], [5, 8], [9, 15]] , [16, 17])))
    # print("Intervals after inserting the new interval: " + str(insert([[1, 2], [3, 4], [5, 8], [9, 15]] , [2, 5])))
    # print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()