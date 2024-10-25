def min_jumps(arr):
    if len(arr) <= 1:
        return 0
    
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(len(arr) - 1):  # We don't need to check the last index
        farthest = max(farthest, i + arr[i])  # Update the farthest point we can reach
        
        if i == current_end:  # Need to jump
            jumps += 1
            current_end = farthest  # Update the current end
            
            if current_end >= len(arr) - 1:  # If we can reach the end
                break
    
    return jumps

# Example usage
input_array = [2, 3, 1, 1, 4]
result = min_jumps(input_array)
print(f"Minimum number of jumps to reach the end: {result}")  # Output: 2

