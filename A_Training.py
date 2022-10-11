def lll(queries):
    queries.sort()
    waiting_times = [0]
    previous_time = 0
    for i in range(1, len(queries)):
        waiting_times.append(queries[i - 1] + waiting_times[i - 1])

    return sum(waiting_times)

def main():
    queries = [3, 2, 1, 2, 6] # 1, 2, 2, 3,6
    print(lll(queries))

if __name__ == '__main__':
    main()