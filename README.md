# Morse Code Translator

This Python script provides a simple graphical user interface (GUI) for translating text to Morse code and vice versa using the tkinter library. You can enter a text message, and the program will convert it to Morse code or decode Morse code back to text.

## How to Use

1. **Launching the Application**
   - Make sure you have Python installed on your computer.
   - Run the script to launch the Morse Code Translator application.

2. **Using the Translator**
   - You will see a window with two input fields, buttons, and an output area.
   - **Enter text**: In the "Enter text" field, input the text you want to translate to Morse code or the Morse code you want to decode.
   - **Translate to Morse**: Click this button to translate the entered text into Morse code.
   - **Translate to Text**: Click this button to decode Morse code into text.
   - The translation result will be displayed in the "Result" area below.

3. **Translating to Morse Code**
   - To translate text to Morse code, enter your text in the "Enter text" field.
   - Click the "Translate to Morse" button.
   - The Morse code translation will be displayed in the "Result" area.

4. **Translating to Text**
   - To decode Morse code into text, input the Morse code in the "Enter text" field, separating characters with spaces.
   - Click the "Translate to Text" button.
   - The decoded text will be displayed in the "Result" area.

## Morse Code Conversion

The translation is performed based on the following Morse code dictionary:

```
{
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}
```

## Dependencies

The script uses the `tkinter` library for the graphical user interface, which is usually included with Python. If you encounter any issues related to missing libraries, please ensure you have Python installed on your system.

## Feedback and Contributions

If you encounter any issues, have suggestions, or want to contribute to this project, feel free to submit an issue or pull request on the project's GitHub repository.

Thank you for using the Morse Code Translator!
