def bubble_sort_v1(arr):
	"""
	Bubble sort algorithm.

	Args:
		arr (list): List of elements to sort.
	
	Returns:
		list: A new sorted list.
	"""
	n = len(arr)
	sorted_arr = arr.copy()
	for i in range(n):
		for j in range(0, n - i - 1):
			if sorted_arr[j] > sorted_arr[j + 1]:
				sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
	return sorted_arr


def selection_sort(arr):
	"""
	Selection sort algorithm.

	Args:
		arr (list): List of elements to sort.
	
	Returns:
		list: A new sorted list.
	"""
	sorted_arr = arr.copy()
	n = len(sorted_arr)
	for i in range(n):
		min_index = i
		for j in range(i+1, n):
			if sorted_arr[j] < sorted_arr[min_index]:
				min_index = j
		sorted_arr[i], sorted_arr[min_index] = sorted_arr[min_index], sorted_arr[i]
	return sorted_arr


def insertion_sort(arr):
	"""
	Insertion sort algorithm.

	Args:
		arr (list): List of elements to sort.
	
	Returns:
		list: A new sorted list.
	"""
	sorted_arr = arr.copy()
	for i in range(1, len(sorted_arr)):
		key = sorted_arr[i]
		j = i - 1
		while j >= 0 and key < sorted_arr[j]:
			sorted_arr[j + 1] = sorted_arr[j]
			j -= 1
		sorted_arr[j + 1] = key
	return sorted_arr


def merge_sort(arr):
	"""
	Merge sort algorithm.

	Args:
		arr (list): List of elements to sort.
	
	Returns:
		list: A new sorted list.
	"""
	if len(arr) <= 1:
		return arr.copy()

	mid = len(arr) // 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	return _merge(left, right)


def _merge(left, right):
	"""
	Helper function to merge two sorted lists.
	"""
	merged = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			merged.append(left[i])
			i += 1
		else:
			merged.append(right[j])
			j += 1
	merged.extend(left[i:])
	merged.extend(right[j:])
	return merged


def quick_sort(arr):
	"""
	Quick sort algorithm.

	Args:
		arr (list): List of elements to sort.
	
	Returns:
		list: A new sorted list.
	"""
	if len(arr) <= 1:
		return arr.copy()
	else:
		pivot = arr[len(arr) // 2]
		left = [x for x in arr if x < pivot]
		middle = [x for x in arr if x == pivot]
		right = [x for x in arr if x > pivot]
		return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
	data = [64, 34, 25, 12, 22, 11, 90]
	print("Original data:", data)
	print("Bubble Sort:", bubble_sort(data))
	print("Selection Sort:", selection_sort(data))
	print("Insertion Sort:", insertion_sort(data))
	print("Merge Sort:", merge_sort(data))
	print("Quick Sort:", quick_sort(data))