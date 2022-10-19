class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        totalNumberofPassengers = [0] * 1001
        for trip in trips:
            totalNumberofPassenger, start, end = trip
            totalNumberofPassengers[start] += totalNumberofPassenger
            totalNumberofPassengers[end] -= totalNumberofPassenger
        currentPassenger=0
        for i in range(1001):
            currentPassenger+=totalNumberofPassengers[i]
            if  currentPassenger>capacity:
                return False
        return True