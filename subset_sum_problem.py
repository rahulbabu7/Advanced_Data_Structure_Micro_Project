def trim_with_paths(lst, delta):
    """Trim the list of (sum, subset) pairs to remove close values."""
    trimmed = [lst[0]]
    for val in lst[1:]:
        if val[0] > trimmed[-1][0] * (1 + delta):
            trimmed.append(val)
    return trimmed

def approximate_subset_sum(S, t, epsilon):
    """
    Approximate Subset Sum using FPTAS
    S: list of positive integers (the set)
    t: target sum
    epsilon: approximation factor (0 < epsilon < 1)
    Returns: (approximate sum, subset that forms the sum)
    """
    n = len(S)
    L = [(0, [])]  # List of tuples: (sum, subset)
    
    for i in range(n):
        new_L = []
        for (total, subset) in L:
            new_sum = total + S[i]
            new_subset = subset + [S[i]]
            new_L.append((new_sum, new_subset))
        L += new_L
        # Remove duplicates and sort by sum
        L = list({x[0]: x for x in L}.values())  # Keep the latest subset for each unique sum
        L.sort(key=lambda x: x[0])
        delta = epsilon / (2 * n)
        L = trim_with_paths(L, delta)
        # Keep only those with sum <= t
        L = [x for x in L if x[0] <= t]

    if L:
        best = max(L, key=lambda x: x[0])
        return best  # (sum, subset)
    else:
        return (0, [])

# Example Usage
if __name__ == "__main__":
    S = [1, 2, 3, 4, 5, 6]
    t = 9
    epsilon = 0.001

    approx_sum, subset = approximate_subset_sum(S, t, epsilon)
    print("Approximate subset sum ≤", t, "is:", approx_sum)
    print("Subset:", subset)
