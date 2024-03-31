import timeit

def solve_cryptarithmetic(operand, result):
    # Space Complexity: O(L) where L is the total number of unique letters in the input
    #Time is O(10^L)
    letter_used = set(letter for word in operand + [result] for letter in word if letter.isalpha())
    digit_map = {}

    def is_valid_assignment():
        # Check if leading digits are not zero
        if any(digit_map[word[0]] == 0 for word in operand + [result]):
            return False
        # Evaluate the equation
        return sum(int("".join(str(digit_map[letter]) for letter in word)) for word in operand) == int("".join(str(digit_map[letter]) for letter in result))

    def solve(idx):
        if idx == len(letter_used):
            return is_valid_assignment()

        letter = list(letter_used)[idx]
        for digit in range(10):
            if digit not in digit_map.values():
                digit_map[letter] = digit
                if solve(idx + 1):
                    return True
                digit_map.pop(letter)
        return False

    start = timeit.default_timer()
    if solve(0):
        stop = timeit.default_timer()
        print("Solution found:")
        for letter, digit in digit_map.items():
            print(f"{letter}: {digit}")
        print("Time Execution =", stop - start, "second")
    else:
        print("No solution found.")

def main():
    problems = [
        (["SEND", "MORE"], "MONEY"),
        (["TWO", "TWO"], "FOUR"),
        (["SEND", "MORE"], "SMART"),
        (["ELEVEN", "NINE"], "TWENTY"),
        (["FIVE", "FIVE"], "TEN"),
        (["CROSS", "ROADS"], "DANGER")
    ]

    for idx, (operand, result) in enumerate(problems, start=1):
        print(f"Problem {idx}:")
        print(f"Operand: {operand}")
        print(f"Result: {result}")
        solve_cryptarithmetic(operand, result)
        print(50 * "=")

if __name__ == "__main__":
    main()
