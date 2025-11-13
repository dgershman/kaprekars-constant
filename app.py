def kaprekar_routine(digits):
    """
    Performs the Kaprekar routine on a 4-digit number.
    Returns the list of steps taken to reach 6174.
    """
    steps = []
    current = digits

    while current != 6174:
        # Convert to 4-digit string (pad with zeros if needed)
        digit_str = str(current).zfill(4)

        # Sort descending
        descending = int(''.join(sorted(digit_str, reverse=True)))

        # Sort ascending
        ascending = int(''.join(sorted(digit_str)))

        # Subtract
        current = descending - ascending

        # Record the step
        steps.append({
            'descending': descending,
            'ascending': ascending,
            'result': current
        })

        # Safety check to prevent infinite loop (shouldn't happen with valid input)
        if len(steps) > 10:
            break

    return steps


def main():
    print("Kaprekar's 6174 Routine")
    print("=" * 40)

    while True:
        user_input = input("\nEnter exactly 4 digits (or 'q' to quit): ").strip()

        if user_input.lower() == 'q':
            print("Goodbye!")
            break

        # Validate input
        if len(user_input) != 4 or not user_input.isdigit():
            print("Error: Please enter exactly 4 digits.")
            continue

        # Check if all digits are the same (would result in 0)
        if len(set(user_input)) == 1:
            print("Error: All digits are the same. This would result in 0, not 6174.")
            continue

        number = int(user_input)
        print(f"\nStarting with: {user_input}")
        print("-" * 40)

        steps = kaprekar_routine(number)

        for i, step in enumerate(steps, 1):
            print(f"Step {i}: {step['descending']} - {step['ascending']} = {step['result']}")

        print(f"\nReached 6174 in {len(steps)} step(s)!")


if __name__ == "__main__":
    main()
