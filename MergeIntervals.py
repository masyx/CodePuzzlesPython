from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

# O(n log(n)) time | O(n) space
def merge(intervals):
    intervals.sort(key=lambda interval: interval.start)
    merged_intervals_counter = 0
    merged = [intervals[merged_intervals_counter]]
    for idx in range(1, len(intervals)):
        if intervals[idx].start <= merged[merged_intervals_counter].end:
            if intervals[idx].end > merged[merged_intervals_counter].end:
                merged[merged_intervals_counter].end = intervals[idx].end
                continue
        else:
            merged.append(intervals[idx])
            merged_intervals_counter += 1
    return merged

# [[1,4], [2,5], [7,9]]
def main():
    # print("Merged intervals: ", end='')
    # for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    #     i.print_interval()
    # print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()

main()