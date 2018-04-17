"""	Suppose that a disk drive has 5,000 cylinders, numbered 0 to 4,999. The
	drive is currently serving a request at cylinder 2,150, and the previous
	request was at cylinder 1,805. The queue of pending requests, in FIFO
	order, is:
	2,069, 1,212, 2,296, 2,800, 544, 1,618, 356, 1,523, 4,965, 3681
	Starting from the current head position, what is the total distance (in
	cylinders) that the disk arm moves to satisfy all the pending requests
	for each of the following disk-scheduling algorithms?

	FCFS, SSTF, SCAN, LOOK, C-SCAN, C-LOOK """
import copy
import sys
head_position = 2150
requests = [2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681]

def FCFS(requests):
	local_head_position = head_position
	distance = 0
	for i in requests:
		distance += abs(local_head_position - i)
		local_head_position = i
	return distance 

print ("The total distance that the disk arm moves for FCFS disk-scheduling is", FCFS(requests))

	
def SSTF(requests):
	local_requests = copy.copy(requests)
	local_head_position = head_position
	final_distance = 0
	distance = 0
	x = max(local_requests)
	min_distance = abs(local_head_position - x)
	while (len(local_requests) > 0):
		for i in local_requests:
			distance = abs(local_head_position - i)
			if (distance < min_distance):
				min_distance = distance
				x = i
		local_head_position = x
		local_requests.remove(x)
		final_distance += min_distance
		if (len(local_requests) > 0):
			min_distance = abs(local_head_position - max(local_requests))
			x = max(local_requests)

	return final_distance
print ("The total distance that the disk arm moves for FCFS disk-scheduling is", SSTF(requests))

"""def SCAN(requests):
	local_head_position = head_position
	end = max()"""


