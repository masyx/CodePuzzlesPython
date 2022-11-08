class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed

    # set the flag for closed/open
    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" if self.closed else "(" + str(self.start) + ", " + str(self.end) + ")"


def display(vec):
    string = "["

    if vec:
        for i in range(len(vec)):
            string += str(vec[i])
            if i + 1 < len(vec):
                string += ", "

    string += "]"

    return string

# O(n + m) time | O(1) space
def intervals_intersection(interval_list_a, interval_list_b):
    i = j = 0
    intersections = []
    while i < len(interval_list_a) and j < len(interval_list_b):
        intersect_start = max(interval_list_a[i].start, interval_list_b[j].start)
        intersect_end = min(interval_list_a[i].end, interval_list_b[j].end)
        
        if intersect_start <= intersect_end:
            intersections.append(Interval(intersect_start, intersect_end))
        
        if interval_list_a[i].end < interval_list_b[j].end:
            i += 1
        else:
            j += 1
    return intersections


# Driver code
def main():
    input_interval_list_a = [[Interval(1, 2)],
                             [Interval(1, 4), Interval(5, 6), Interval(9, 15)],
                             [Interval(3, 6), Interval(8, 16), Interval(17, 25)],
                             [Interval(4, 7), Interval(9, 16), Interval(17, 28), 
                                 Interval(39, 50), Interval(55, 66), Interval(70, 89)],
                             [Interval(1, 3), Interval(5, 6), Interval(7, 8), 
                                 Interval(12, 15)]
                             ]

    input_interval_list_b = [[Interval(1, 2)],
                             [Interval(2, 4), Interval(5, 7), Interval(9, 15)],
                             [Interval(2, 3), Interval(10, 15), Interval(18, 23)],
                             [Interval(3, 6), Interval(7, 8), Interval(9, 10),
                                 Interval(14, 19), Interval(23, 33), Interval(35, 40),
                                 Interval(45, 59), Interval(60, 64), Interval(68, 76)],
                             [Interval(2, 4), Interval(7, 10)]
                             ]

    for i in range(len(input_interval_list_a)):
        print(i + 1, '.\t Interval List A: ',
              display(input_interval_list_a[i]), sep="")
        print('\t Interval List B: ',
              display(input_interval_list_b[i]), sep="")
        print("\t Intersecting intervals in 'A' and 'B' are: ",
              display(intervals_intersection(
                  input_interval_list_a[i], input_interval_list_b[i])), sep="")

        print('-' * 100)


if __name__ == "__main__":
    main()