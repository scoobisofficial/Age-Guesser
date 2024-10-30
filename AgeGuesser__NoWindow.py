import time

while True:
    try:
        age = int(input("I will try to guess your age. Please enter your age: "))
        
        # Check if age is within a reasonable range
        if 0 <= age <= 120:
            print("Thinking...")
            time.sleep(2)  # Delay to simulate thinking
            print("Are you", age, "years old?")
            break  # Exit the loop if the age is valid
        else:
            print("Ok dinosaur, Enter your REAL AGE.")
    except ValueError:
        print("Thats... not a number. Please enter a real one.")