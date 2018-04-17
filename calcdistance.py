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

head_position = 2150
requests = [2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681]

def FCFS(requests):
	local_head_position = head_position   			#local head 
	distance = 0
	for i in requests:								#for every cylinder calculate the distance and change the head position
		distance += abs(local_head_position - i)
		local_head_position = i
	return distance 

print ("The total distance that the disk arm moves for FCFS disk-scheduling is", FCFS(requests))

	
def SSTF(requests):
	local_requests = copy.copy(requests)		
	local_head_position = head_position
	final_distance = 0
	distance = 0
	
	end = max(local_requests)												#maximum cylinder accessed 
	min_distance = abs(local_head_position - end)							#calculate distance between highest cylinder and current head position for a reference distance 
	while (len(local_requests) > 0):										#until the array is empty
		for i in local_requests:
			distance = abs(local_head_position - i)	
			if (distance < min_distance):			
				min_distance = distance
				end = i
		
		local_head_position = end											#change the current head position
		local_requests.remove(end)
		final_distance += min_distance										#add to the total distance
		if (len(local_requests) > 0):				
			min_distance = abs(local_head_position - max(local_requests))	#Generate new min_distance from updated local_requests for comparison
			end = max(local_requests)

	return final_distance
print ("The total distance that the disk arm moves for SSTF disk-scheduling is", SSTF(requests))

def SCAN(requests):
	local_head_position = head_position
	local_requests = copy.copy(requests)
	total_distance = 0

	end = max(local_requests)								#maximum cylinder accessed
	max_queue = 4999										#the total size of cylinder

	for i in range(local_head_position, end+1):				#this function adds all the distance from current to the max value of cylinder in array
		if (i in local_requests):
			total_distance += abs(local_head_position - i)
			local_head_position = i
			local_requests.remove(i)

	total_distance += abs(local_head_position - max_queue)	#add the distance from max value of cylinder in array to the end of cylinder
	local_head_position = max_queue							#set current head to end of cylinder

	count = end 	
	while count >= 0:										#calculate the distance from the end of the cylinder to the opposite direction
		if (count in local_requests):
			total_distance += abs(local_head_position - count)
			local_head_position = count 
			local_requests.remove(count)
		count -= 1

	return total_distance
print ("The total distance that the disk arm moves for SCAN disk-scheduling is", SCAN(requests))

def CSCAN(requests):
	local_head_position = head_position
	local_requests = copy.copy(requests)
	total_distance = 0

	end = max(local_requests)
	max_queue = 4999

	for i in range(local_head_position, end+1):				#this function adds all the distance from current to the max value of cylinder in array
		if (i in local_requests):
			total_distance += abs(local_head_position - i)
			local_head_position = i
			local_requests.remove(i)

	total_distance += abs(local_head_position - max_queue)	#add the distance from max value of cylinder in array to the end of cylinder
	local_head_position = 0									#set current head to start of cylinder

	end = max(local_requests)								#calculate the distance from the start of the cylinder to the value less and close to the initial head position
	for y in range (0, end+1):
		if (y in local_requests):
			total_distance += abs(local_head_position - y)
			local_head_position = y
			local_requests.remove(y)

	return total_distance
print ("The total distance that the disk arm moves for CSCAN disk-scheduling is", CSCAN(requests))

def LOOK(requests):
	local_head_position = head_position
	local_requests = copy.copy(requests)
	total_distance = 0

	end = max(local_requests)

	for i in range(local_head_position, end+1):				#this function adds all the distance from current to the max value of cylinder in array
		if (i in local_requests):
			total_distance += abs(local_head_position - i)
			local_head_position = i
			local_requests.remove(i)

	count = end 											#calculate the distance from the max value of the cylinder to the opposite direction
	while count >= 0:										
		if (count in local_requests):
			total_distance += abs(local_head_position - count)
			local_head_position = count 
			local_requests.remove(count)
		count -= 1

	return total_distance
print ("The total distance that the disk arm moves for LOOK disk-scheduling is", LOOK(requests))

def CLOOK(requests):
	local_head_position = head_position
	local_requests = copy.copy(requests)
	total_distance = 0

	end = max(local_requests)

	for i in range(local_head_position, end+1):				#this function adds all the distance from current to the max value of cylinder in array
		if (i in local_requests):
			total_distance += abs(local_head_position - i)
			local_head_position = i
			local_requests.remove(i)

	local_head_position = min(local_requests)				#set current head to the minimum in local_requests array

	end = max(local_requests)
	for y in range (local_head_position, end+1):			#calculate the distance from the minimum value of cylinder to the value less and close to the initial value of head 
		if (y in local_requests):
			total_distance += abs(local_head_position - y)
			local_head_position = y
			local_requests.remove(y)

	return total_distance
print ("The total distance that the disk arm moves for CLOOK disk-scheduling is", CLOOK(requests))