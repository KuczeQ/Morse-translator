import tkinter as tk

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

reverse_morse_code = {value: key for key, value in morse_code.items()}

def translate_to_morse():
    text = input_text.get().upper()
    translated_text = ' '.join(morse_code.get(char, '') for char in text)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, translated_text)

def translate_to_text():
    text = input_text.get().split(' ')
    translated_text = ''.join(reverse_morse_code.get(char, '') for char in text)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, translated_text)

window = tk.Tk()
window.title("Morse Code Translator")
window.geometry("400x300")

input_label = tk.Label(window, text="Enter text:")
input_label.pack()
input_text = tk.Entry(window)
input_text.pack()

translate_to_morse_button = tk.Button(window, text="Translate to Morse", command=translate_to_morse)
translate_to_morse_button.pack()

translate_to_text_button = tk.Button(window, text="Translate to Text", command=translate_to_text)
translate_to_text_button.pack()

output_label = tk.Label(window, text="Result:")
output_label.pack()
output_text = tk.Text(window, height=5, width=40)
output_text.pack()

window.mainloop()
