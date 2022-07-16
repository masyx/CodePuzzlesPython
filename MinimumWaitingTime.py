def main():
    queries = [1, 2, 2, 3,6]
    print(minimumWaitingTime(queries))

# O(n log(n)) time | O(n) space
def minimumWaitingTimeBrut(queries):
    queries.sort()
    currentWaitingTime = 0
    times = []
    for i in range(1, len(queries)):
        currentWaitingTime += queries[i - 1]
        times.append(currentWaitingTime)
    return sum(times)

# O(n log(n)) time | O(1) space
def minimumWaitingTime(queries):
    queries.sort()
    currentWaitingTime = 0
    totalWaitingTime = 0
    for i in range(1, len(queries)):
        currentWaitingTime += queries[i - 1]
        totalWaitingTime += currentWaitingTime

    return totalWaitingTime

# O(n log(n)) time | O(1) space
def minimumWaitingTimeAlgo(queries):
    queries.sort()
    totalWT = 0
    for i in range(len(queries)):
        totalWT += queries[i] * (len(queries) - 1 - i)
    return totalWT

if __name__ == "__main__":
    main()