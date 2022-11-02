# O(n) time | O(n) space
def insert(intervals, new_interval):
    merged = []
    new_interval_used = False
    for idx in range(len(intervals)):
        if not new_interval_used:
            if new_interval[0] <= intervals[idx][1]:
                intervals[idx][0] = min(intervals[idx][0], new_interval[0])
                intervals[idx][1] = max(intervals[idx][1], new_interval[1])
                merged.append(intervals[idx])
                new_interval_used = True
            else:
                merged.append(intervals[idx])
        else:
            if intervals[idx][0] <= merged[-1][1]:
                merged[-1][1] = max(intervals[idx][1], merged[-1][1])
            else:
                merged.append(intervals[idx])
    if not new_interval_used:
        merged.append(new_interval)
    return merged


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 2], [3, 4], [5, 8], [9, 15]] , [16, 17])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 2], [3, 4], [5, 8], [9, 15]] , [2, 5])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
