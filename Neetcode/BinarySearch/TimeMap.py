""" 981. Time Based Key-Value Store
Medium

Implement a time-based key-value data structure that supports:

Storing multiple values for the same key at specified time stamps
Retrieving the key's value at a specified timestamp
Implement the TimeMap class:

TimeMap() Initializes the object.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".
Note: For all calls to set, the timestamps are in strictly increasing order.

Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.

"""



from collections import defaultdict

class TimeMap:
    """
    A time-based key-value store.
    """
    def __init__(self):
        """
        Initializes the data structure.
        We use a dictionary where each key maps to a list of [timestamp, value] pairs.
        """
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the (key, value) pair with the given timestamp.
        We assume timestamps are always increasing, so we can just append.
        """
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        """
        Returns the value for a key at a time on or before the given timestamp.
        Uses binary search for an efficient O(log N) lookup.
        """
        # Retrieve the list of [timestamp, value] pairs for the key.
        # If the key doesn't exist, self.store[key] would create an empty list,
        # so the search will correctly return an empty string.
        values = self.store.get(key, [])
        if not values:
            return ""

        # Binary search setup
        result = ""
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            stored_timestamp, stored_value = values[mid]

            if stored_timestamp <= timestamp:
                # This is a valid candidate for our answer.
                # We store it and continue searching to the right
                # to see if a *more recent* valid timestamp exists.
                result = stored_value
                left = mid + 1
            else:
                # The timestamp at 'mid' is too recent.
                # We must search in the left half.
                right = mid - 1
        
        return result
        

def main():
    # Create an instance of the TimeMap
    tm = TimeMap()

    # Set some values for the key "alice"
    tm.set("alice", "online", 10)
    tm.set("alice", "busy", 30)
    tm.set("alice", "offline", 50)

    # Perform get operations
    print(f'Status at time 5:  "{tm.get("alice", 5)}"')   # Output: ""
    print(f'Status at time 10: "{tm.get("alice", 10)}"')  # Output: "online"
    print(f'Status at time 45: "{tm.get("alice", 45)}"')  # Output: "busy"
    print(f'Status at time 50: "{tm.get("alice", 50)}"')  # Output: "offline"
    print(f'Status at time 100: "{tm.get("alice", 100)}"') # Output: "offline"
  
  
if __name__ == "__main__":
    main()