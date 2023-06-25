import tkinter as tk

# Słownik mapujący litery na ich odpowiedniki w alfabecie morsa
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

# Odwrócenie kluczy i wartości w słowniku morse_code
reverse_morse_code = {value: key for key, value in morse_code.items()}

# Funkcja do tłumaczenia z języka naturalnego na język morsa
def translate_to_morse():
    text = input_text.get().upper()
    translated_text = ' '.join(morse_code.get(char, '') for char in text)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, translated_text)

# Funkcja do tłumaczenia z języka morsa na język naturalny
def translate_to_text():
    text = input_text.get().split(' ')
    translated_text = ''.join(reverse_morse_code.get(char, '') for char in text)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, translated_text)

# Tworzenie okna głównego
window = tk.Tk()
window.title("Tłumacz języka morsa")
window.geometry("400x300")

# Etykieta i pole tekstowe do wprowadzania tekstu
input_label = tk.Label(window, text="Wprowadź tekst:")
input_label.pack()
input_text = tk.Entry(window)
input_text.pack()

# Przyciski do tłumaczenia
translate_to_morse_button = tk.Button(window, text="Tłumacz na Morse'a", command=translate_to_morse)
translate_to_morse_button.pack()

translate_to_text_button = tk.Button(window, text="Tłumacz na tekst", command=translate_to_text)
translate_to_text_button.pack()

# Pole tekstowe na wynik tłumaczenia
output_label = tk.Label(window, text="Wynik:")
output_label.pack()
output_text = tk.Text(window, height=5, width=40)
output_text.pack()

# Uruchomienie pętli głównej aplikacji
window.mainloop()
