#!/usr/bin/python

#TODO: create input files and fill the arrays from that
numbers = [3, -9, 8, 9, 6, -2, 9, 1, -2, 6, 7, 3, 3, -1, 1, -3, 0, 3, 1,-3]
weights = [5, 9, 1, 10, 8, 5, 3, 10, 6, 5, 4, 2, 5, 8, 4, 3, 9, 8, 4, 7]
LIS = []
maxWeight = []
k = []
maxK = 2
pred = []

# Initially length of longest subsequence beginning at i is 1
for i in range(len(numbers)):
	LIS.append(1);

# Initially length of longest subsequence beginning at i is 1
for i in range(len(numbers)):
	maxWeight.append(weights[i]);

# Initially length of longest subsequence beginning at i is 1
for i in range(len(numbers)):
	k.append(0);

for i in range(len(numbers)):
	pred.append(-1);

for i in range(1, len(numbers)):
	for j in range(0, i):
		if numbers[j] < numbers[i] and maxWeight[i] < maxWeight[j] + weights[i]:
			maxWeight[i] = maxWeight[j] + weights[i]
			print(" adding " , maxWeight[j] , " and " , weights[i] , " for " , numbers[i] , " and " , numbers[j])
			LIS[i] = LIS[j] + 1
			k[i] = k[j]
			pred[i] = j
		elif numbers[j] >= numbers[i] and k[j] + 1 <= maxK and maxWeight[i] < maxWeight[j] + weights[i] - weights[i]*(numbers[j] - numbers[i]):
			maxWeight[i] = maxWeight[j] + weights[i] - weights[i]*(numbers[j] - numbers[i])
			k[i] = k[j] + 1
			LIS[i] = LIS[j] + 1
			pred[i] = j

print(maxWeight)
print("Solution for part b:")
# Find the maximum weight from the maxWeight matrix
maxWeightFound = max(maxWeight)
print(maxWeightFound)
index = maxWeight.index(maxWeightFound)

sequenceIndices = []
while index != -1:
	sequenceIndices.append(index)
	index = pred[index]

sequenceIndices.reverse()
print(sequenceIndices)

sequence = []
for i in range(len(sequenceIndices)):
	sequence.append(numbers[sequenceIndices[i]])

print(sequence)