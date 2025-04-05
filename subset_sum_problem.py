import matplotlib.pyplot as plt

def subset_sum_fptas_with_graph(S, T, epsilon=0.01):
    L = [(0, [])]  # (sum, subset)
    all_steps = []  # For graphing

    for x in S:
        new_sums = [(val + x, subset + [x]) for val, subset in L]
        merged = merge_and_trim(L + new_sums, epsilon)
        L = [item for item in merged if item[0] <= T]
        all_steps.append((x, [val for val, _ in L]))  # record current values

    max_sum = max(val for val, _ in L)
    valid_subsets = [subset for val, subset in L if val == max_sum]
    best_subset = min(valid_subsets, key=len)

    plot_growth(all_steps, T)

    return max_sum, valid_subsets, best_subset


def merge_and_trim(L, epsilon):
    L.sort()
    trimmed = [L[0]]
    for current in L[1:]:
        if current[0] > trimmed[-1][0] * (1 + epsilon):
            trimmed.append(current)
    return trimmed


def plot_growth(all_steps, T):
    plt.figure(figsize=(10, 6))
    for i, (x, sums) in enumerate(all_steps):
        plt.plot(sums, marker='o', label=f"Step {i+1}: Add {x}")
    plt.axhline(y=T, color='red', linestyle='--', label=f"Target T = {T}")
    plt.title("Subset Sum Growth Over Steps (FPTAS)")
    plt.xlabel("Index in trimmed list")
    plt.ylabel("Subset Sum Values")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# 🔍 Example usage
S = [4, 3, 2, 5]
T = 10
epsilon = 0.01

max_sum, valid_subsets, best_subset = subset_sum_fptas_with_graph(S, T, epsilon)

print("✅ Approximate Max Sum Found:", max_sum)
print("\n📋 All Subsets with Max Sum:")
for i, subset in enumerate(valid_subsets, 1):
    print(f"  {i}. {subset}")
print("\n🏆 Best Subset (Shortest):", best_subset)
