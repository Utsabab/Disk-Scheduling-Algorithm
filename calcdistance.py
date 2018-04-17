"""	Suppose that a disk drive has 5,000 cylinders, numbered 0 to 4,999. The
	drive is currently serving a request at cylinder 2,150, and the previous
	request was at cylinder 1,805. The queue of pending requests, in FIFO
	order, is:
	2,069, 1,212, 2,296, 2,800, 544, 1,618, 356, 1,523, 4,965, 3681
	Starting from the current head position, what is the total distance (in
	cylinders) that the disk arm moves to satisfy all the pending requests
	for each of the following disk-scheduling algorithms?

	FCFS, SSTF, SCAN, LOOK, C-SCAN, C-LOOK """

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

	
