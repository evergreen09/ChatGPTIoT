import tkinter as tk
import openai
from tkinter import messagebox

# Set your OpenAI API key
openai.api_key = ""

def get_chat_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for busy Traders. Your response should be concise and well structured with reasonings"},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message['content'], None
    except Exception as e:
        return None, str(e)

def submit_query():
    user_input = user_input_text.get()
    response, error = get_chat_response(user_input)
    
    if error:
        messagebox.showerror("Error", error)
    else:
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, response)

root = tk.Tk()
root.title("Trader Assistant")

user_input_text = tk.StringVar()

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text="Enter your query:")
input_label.pack()

input_entry = tk.Entry(input_frame, textvariable=user_input_text, width=50)
input_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_query)
submit_button.pack(pady=10)

response_label = tk.Label(root, text="Response:")
response_label.pack(pady=10)

response_text = tk.Text(root, wrap=tk.WORD, width=50, height=10)
response_text.pack(pady=10)

root.mainloop()
