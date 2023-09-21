def word_lengths(input_string):
    # Extract words from the input string
    words = input_string[1:].split()  # Exclude '@' and split by space

    # Calculate the lengths of each word
    word_lengths = [str(len(word)) for word in words]

    # Join the lengths with commas
    return ','.join(word_lengths)

# Main function to handle input and output
def main():
    T = int(input().strip())  # Number of test cases

    for _ in range(T):
        input_str = input().strip()  # Read the input string
        lengths_str = word_lengths(input_str)  # Calculate word lengths
        print(lengths_str)  # Print the word lengths as a comma-separated string

if __name__ == "__main__":
    main()

