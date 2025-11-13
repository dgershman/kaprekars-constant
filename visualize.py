import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def kaprekar_iterations(number):
    """
    Returns the number of iterations needed to reach 6174.
    Returns -1 for repdigits (all same digits).
    """
    digit_str = str(number).zfill(4)

    # Check for repdigits (all same digit)
    if len(set(digit_str)) == 1:
        return -1

    current = number
    iterations = 0
    max_iterations = 10  # Safety limit

    while current != 6174 and iterations < max_iterations:
        digit_str = str(current).zfill(4)
        descending = int(''.join(sorted(digit_str, reverse=True)))
        ascending = int(''.join(sorted(digit_str)))
        current = descending - ascending
        iterations += 1

    return iterations if current == 6174 else -1


def analyze_all_numbers():
    """Analyze all 4-digit numbers (0000-9999)"""
    results = {}

    for num in range(10000):
        iterations = kaprekar_iterations(num)
        results[num] = iterations

    return results


def create_visualizations(results):
    """Create multiple visualizations of the data"""

    # Filter out repdigits (-1 values)
    valid_results = {k: v for k, v in results.items() if v >= 0}

    # Count iterations
    iteration_counts = Counter(valid_results.values())

    # Create figure with multiple subplots
    fig = plt.figure(figsize=(16, 10))

    # 1. Histogram of iterations
    ax1 = plt.subplot(2, 3, 1)
    iterations = sorted(iteration_counts.keys())
    counts = [iteration_counts[i] for i in iterations]
    ax1.bar(iterations, counts, color='steelblue', edgecolor='black')
    ax1.set_xlabel('Number of Iterations')
    ax1.set_ylabel('Count of Numbers')
    ax1.set_title('Distribution of Iterations to Reach 6174')
    ax1.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for i, (iter_val, count) in enumerate(zip(iterations, counts)):
        ax1.text(iter_val, count, str(count), ha='center', va='bottom')

    # 2. Heatmap of all numbers (100x100 grid)
    ax2 = plt.subplot(2, 3, 2)
    heatmap_data = np.zeros((100, 100))
    for num, iters in valid_results.items():
        row, col = num // 100, num % 100
        heatmap_data[row, col] = iters

    im = ax2.imshow(heatmap_data, cmap='viridis', aspect='auto')
    ax2.set_xlabel('Last 2 Digits (00-99)')
    ax2.set_ylabel('First 2 Digits (00-99)')
    ax2.set_title('Heatmap: Iterations by Number (0000-9999)')
    plt.colorbar(im, ax=ax2, label='Iterations')

    # 3. Line plot showing iterations for sequential numbers
    ax3 = plt.subplot(2, 3, 3)
    nums = list(range(0, 10000, 10))  # Sample every 10th number
    iters = [results[n] if results[n] >= 0 else 0 for n in nums]
    ax3.plot(nums, iters, linewidth=0.5, alpha=0.7)
    ax3.set_xlabel('Number')
    ax3.set_ylabel('Iterations')
    ax3.set_title('Iterations vs Number (sampled every 10)')
    ax3.grid(alpha=0.3)

    # 4. Pie chart of iteration distribution
    ax4 = plt.subplot(2, 3, 4)
    ax4.pie(counts, labels=[f'{i} iter' for i in iterations], autopct='%1.1f%%',
            startangle=90, colors=plt.cm.Set3(range(len(iterations))))
    ax4.set_title('Percentage Distribution of Iterations')

    # 5. Statistics table
    ax5 = plt.subplot(2, 3, 5)
    ax5.axis('off')

    stats_text = f"""
    KAPREKAR'S 6174 STATISTICS
    {'='*40}

    Total numbers analyzed:  {len(results):,}
    Valid numbers (non-repdigits):  {len(valid_results):,}
    Repdigits (excluded):  {len(results) - len(valid_results)}

    Iteration Statistics:
    {'─'*40}
    Minimum iterations:  {min(valid_results.values())}
    Maximum iterations:  {max(valid_results.values())}
    Average iterations:  {np.mean(list(valid_results.values())):.2f}
    Median iterations:   {np.median(list(valid_results.values())):.1f}

    Most Common:
    {'─'*40}
    """

    for iters, count in sorted(iteration_counts.items(), key=lambda x: x[1], reverse=True)[:3]:
        percentage = (count / len(valid_results)) * 100
        stats_text += f"    {iters} iterations: {count:,} numbers ({percentage:.1f}%)\n"

    ax5.text(0.1, 0.9, stats_text, fontfamily='monospace',
             fontsize=10, verticalalignment='top')

    # 6. Special numbers visualization
    ax6 = plt.subplot(2, 3, 6)

    # Find numbers that take the most and least iterations
    max_iter = max(valid_results.values())
    min_iter = min(valid_results.values())

    max_nums = [k for k, v in valid_results.items() if v == max_iter]
    min_nums = [k for k, v in valid_results.items() if v == min_iter]

    special_text = f"""
    SPECIAL CASES
    {'='*40}

    Takes {max_iter} iterations (max):
    {', '.join([f'{n:04d}' for n in max_nums[:10]])}
    {'...' if len(max_nums) > 10 else ''}
    Total: {len(max_nums)} numbers

    Takes {min_iter} iteration (min):
    {', '.join([f'{n:04d}' for n in min_nums[:10]])}
    {'...' if len(min_nums) > 10 else ''}
    Total: {len(min_nums)} numbers

    The number 6174 itself takes {results[6174]} iteration
    (it maps to itself!)
    """

    ax6.axis('off')
    ax6.text(0.1, 0.9, special_text, fontfamily='monospace',
             fontsize=9, verticalalignment='top')

    plt.tight_layout()
    plt.savefig('kaprekar_6174_analysis.png', dpi=300, bbox_inches='tight')
    print("Visualization saved as 'kaprekar_6174_analysis.png'")

    return iteration_counts, valid_results


def print_summary(results):
    """Print a text summary of findings"""
    valid_results = {k: v for k, v in results.items() if v >= 0}
    iteration_counts = Counter(valid_results.values())

    print("\n" + "="*50)
    print("KAPREKAR'S 6174 - COMPLETE ANALYSIS")
    print("="*50)

    print(f"\nTotal 4-digit numbers: {len(results):,}")
    print(f"Valid numbers (converge to 6174): {len(valid_results):,}")
    print(f"Repdigits (all same digit): {len(results) - len(valid_results)}")

    print(f"\nIteration Range: {min(valid_results.values())} to {max(valid_results.values())}")
    print(f"Average iterations: {np.mean(list(valid_results.values())):.2f}")

    print("\n" + "-"*50)
    print("Iteration Distribution:")
    print("-"*50)
    for iters in sorted(iteration_counts.keys()):
        count = iteration_counts[iters]
        percentage = (count / len(valid_results)) * 100
        bar = '█' * int(percentage / 2)
        print(f"{iters} iterations: {count:4,} numbers ({percentage:5.1f}%) {bar}")


if __name__ == "__main__":
    print("Analyzing all 10,000 possible 4-digit numbers...")
    print("This may take a moment...\n")

    results = analyze_all_numbers()
    print_summary(results)

    print("\nCreating visualizations...")
    create_visualizations(results)

    print("\nDone! Check 'kaprekar_6174_analysis.png' for the full visualization.")
