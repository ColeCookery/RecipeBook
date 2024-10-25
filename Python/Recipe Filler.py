import tkinter as tk
from tkinter import messagebox
import os


def write_to_file(recipe_title, ingredients, instructions, image_url):
    # Ensure recipe_title is a string and strip it of extra spaces
    recipe_title_value = recipe_title.strip().replace(" ", "_")  # Remove spaces from title for filename
    filename = f"{recipe_title_value}.html"
    
    try:
        # Get the absolute path to the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the full path to the template file
        template_path = os.path.join(script_dir, "template_file.txt")

        # Open the template file
        with open(template_path, "r") as file:
            content = file.read()

        # Replace placeholders with user inputs
        content = content.replace("{Recipe Title}", recipe_title)
        content = content.replace("{Ingredients}", ingredients)
        content = content.replace("{Instructions}", instructions)
        content = content.replace("{Image URL}", image_url)

        # Write the updated content to a new file using the Recipe Title as the filename
        with open(filename, "w") as file:
            file.write(content)

        # Show a success message
        messagebox.showinfo("Success", f"Recipe has been saved as {filename}!")
    except FileNotFoundError:
        messagebox.showerror("Error", "Template file not found!")



# Function to handle "Next" button and input switching
def next_step():
    global current_step

    # Save the current input and move to the next step
    if current_step == 0:
        recipe_title.set(entry.get())
        label.config(text="Enter Ingredients:")
        entry.pack_forget()  # Hide the single-line entry widget

        # Show the ingredients multiline text box
        ingredients_text.pack(pady=10)
        current_step += 1
    elif current_step == 1:
        ingredients.set(ingredients_text.get("1.0", tk.END).strip())  # Get multiline input
        label.config(text="Enter Instructions:")
        ingredients_text.pack_forget()  # Hide the ingredients text box

        # Show the instructions multiline text box
        instructions_text.pack(pady=10)
        current_step += 1
    elif current_step == 2:
        instructions.set(instructions_text.get("1.0", tk.END).strip())  # Get multiline input
        label.config(text="Enter Image URL:")
        instructions_text.pack_forget()  # Hide the instructions text box

        # Show the Image URL single-line entry
        image_url_entry.pack(pady=10)
        current_step += 1
    elif current_step == 3:
        image_url.set(image_url_entry.get())
        # Write the data into the file
        write_to_file(recipe_title.get(), ingredients.get(), instructions.get(), image_url.get())
        root.quit()  # Close the window after saving


# Create the main window
root = tk.Tk()
root.title("Recipe Input")

# Styling
root.geometry("400x400")  # Set window size
root.configure(bg="#f0f0f0")  # Background color

# Variables to store user input
recipe_title = tk.StringVar()
ingredients = tk.StringVar()
instructions = tk.StringVar()
image_url = tk.StringVar()

# Initialize the first step
current_step = 0

# Font styles
label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 10)
button_font = ("Helvetica", 10, "bold")

# Create and place widgets
label = tk.Label(root, text="Enter Recipe Title:", font=label_font, bg="#f0f0f0", fg="#333")
label.pack(pady=15)

# Entry widget for single-line input (Recipe Title)
entry = tk.Entry(root, width=50, font=entry_font, relief="flat", highlightbackground="#cccccc", highlightthickness=1)
entry.pack(pady=10)

# Multiline Text widgets for Ingredients and Instructions
ingredients_text = tk.Text(root, width=50, height=5, font=entry_font, relief="flat", highlightbackground="#cccccc", highlightthickness=1)
instructions_text = tk.Text(root, width=50, height=5, font=entry_font, relief="flat", highlightbackground="#cccccc", highlightthickness=1)

# Entry widget for Image URL (single-line input)
image_url_entry = tk.Entry(root, width=50, font=entry_font, relief="flat", highlightbackground="#cccccc", highlightthickness=1)

# "Next" button
next_button = tk.Button(root, text="Next", command=next_step, font=button_font, bg="#4CAF50", fg="white", relief="flat", padx=10, pady=5)
next_button.pack(pady=15)

# Run the main loop
root.mainloop()
