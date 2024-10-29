import tkinter as tk

# Function to run the age guessing logic
def guess_age():
    try:
        # Get the age entered by the user
        age = int(age_entry.get())
        
        # Display "Thinking..." and set a delay before showing the final result
        result_label.config(text="Thinking...")
        
        # After a 2-second delay (2000 milliseconds), display the age guess
        window.after(2000, lambda: result_label.config(text=f"Are you {age} years old?"))
        
    except ValueError:
        # Display an error if the input is not a valid number
        result_label.config(text="Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Age Guesser")
window.geometry("400x200")

# Create an instruction label
instruction_label = tk.Label(window, text="I will try to guess your age.")
instruction_label.pack(pady=10)

# Create an entry widget for age input
age_entry = tk.Entry(window)
age_entry.pack(pady=5)

# Create a button to submit age
guess_button = tk.Button(window, text="Submit Age", command=guess_age)
guess_button.pack(pady=5)

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run the application
window.mainloop()