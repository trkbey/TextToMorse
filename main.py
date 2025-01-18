import pandas as pd

def text_to_morse(input_text, csv_file='letters.csv'):
    """
    Converts a given text into Morse code using a csv file containing letters and their Morse code equivalents.

    Args:
        input_text (str): Text to be converted to Morse code.
        csv_file (str): Path to the CSV file with columns 'Letters' and 'Morsecodes'.

    Returns:
        str: Morse code representation of the input text.
    """
    try:
        # Read the CSV file into a DataFrame
        data = pd.read_csv(csv_file)

        # Initialize output string
        output = ""

        # Convert input text to uppercase and iterate through each character
        for char in input_text.upper():
            if char in data.Letters.values:
                # Find the Morse code for the char and append to the output
                morse_code = data.Morsecodes[data.Letters[data.Letters == char].index].to_string().split(" ")[-1]
                output += morse_code + " "
            else:
                # If the character is not found, add a placeholder or ignore
                output += "? "  # '?' represents unknown characters

        return output.strip()

    except FileNotFoundError:
        return "Error: The specified CSV file was not found."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_input = input("Enter any text: ")
    morse_output = text_to_morse(user_input)
    print(f"Morse code below\n {morse_output}")
