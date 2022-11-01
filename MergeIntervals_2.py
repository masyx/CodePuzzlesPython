# O(n log(n)) time | O(n) space
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
    intervals = [
                [1, 2],
                [3, 5],
                [4, 7],
                [6, 8],
                [9, 10]
                ]

    print(mergeOverlappingIntervals(intervals))


if __name__ == "__main__":
    main()