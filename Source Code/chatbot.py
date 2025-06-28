import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import PhotoImage
import requests
import threading
import json
import os
import ollama

# Clear the chat history file at the start of the program
open("chat_history.json", "w").write("[]")

OLLAMA_API_URL = "http://localhost:11434/api/generate"

chat_log_file = "chat_history.json"
chat_history_list = []

# Load existing chat history if it exists
if os.path.exists(chat_log_file):
    with open(chat_log_file, "r", encoding="utf-8") as f:
        try:
            chat_history_list = json.load(f)
        except json.JSONDecodeError:
            chat_history_list = []

def send_to_ollama(prompt):
    system_prompt = (
    "You are an AI assistant. Respond in **English only**, in a friendly and helpful way. "
    "Keep answers short and clear. Do not use any other language."
    )

    data = {
        "model": "tinyllama",  # or whatever model you used
        "prompt": f"{system_prompt}\n\nUser: {prompt}\nAssistant:",
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=data)
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"Error: {response.text}"
    except Exception as e:
        return f"Connection error: {e}"

def on_send():
    user_input = input_box.get()
    if not user_input.strip():
        return

    # Show user's message
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"🤵🏻 : {user_input}\n", "user") # Apply user tag
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)
    input_box.delete(0, tk.END)

    # Add to chat history
    chat_history_list.append({"role": "user", "message": user_input})

    # Call the model
    response = ollama.chat(
        model="tinyllama",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful and intelligent assistant. Always respond in English using the shortest, clearest replies. "
                    "Keep your answers polite and to the point. Do not add extra information unless asked. Continue chatting naturally. "
                    "Keep the reply as shortest as possible."
                )
            }
        ] + [{"role": msg["role"], "content": msg["message"]} for msg in chat_history_list],
        options={
            "num_predict": 50
        }
    )

    bot_reply = response['message']['content'].strip()

    # Show bot reply
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"💬 : {bot_reply}\n", "bot")  # Apply bot tag
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)

    # Add bot reply to history
    chat_history_list.append({"role": "assistant", "message": bot_reply})

    # Save updated history
    with open(chat_log_file, "w", encoding="utf-8") as f:
        json.dump(chat_history_list, f, indent=2)

def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete(1.0, tk.END)
    chat_area.config(state=tk.DISABLED)

    # Clear the chat history file
    open("chat_history.json", "w").write("[]")





# GUI Setup

# Initialize main window
window = tk.Tk()
window.title("Personal Assistant")
window.geometry("600x600")
window.configure(bg="#f5f5f5")
window.resizable(True, True)

# ✅ Optional: Set a logo/icon
try:
    window.iconbitmap("Chatbot icon.ico")  # Only works with .ico files
except Exception as e:
    print(f"Icon load error: {e}")

# ✅ Load image AFTER creating window & KEEP reference
try:
    logo_img = PhotoImage(file="Logo image.png")
    logo_label = tk.Label(window, image=logo_img, bg="#f5f5f5")
    logo_label.image = logo_img  # ✅ Prevent garbage collection
    logo_label.pack(pady=(10, 0))
except Exception as e:
    print(f"Logo image load error: {e}")

# Chat area
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Segoe UI", 11), bg="#ffffff", fg="#333333")
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.config(state=tk.DISABLED)

# ✅ Tag configurations here (do this only once)
chat_area.tag_config("user", foreground="#7030A0")  # Soft peach for user
chat_area.tag_config("bot", foreground="#F20E55")   # Sky blue for bot

# Input frame
input_frame = tk.Frame(window, bg="#f5f5f5")
input_frame.pack(fill=tk.X, pady=(0, 10))

input_box = tk.Entry(input_frame, font=("Segoe UI", 11), width=50, bg="#ffffff", fg="#000000")
input_box.pack(side=tk.LEFT, padx=(10, 5), ipady=4)
# ✅ Bind Enter key to send message
input_box.bind("<Return>", lambda event: on_send())

send_button = ttk.Button(input_frame, text="Send", command=on_send)
send_button.pack(side=tk.LEFT, padx=(0, 5))

clear_button = tk.Button(input_frame, text="Clear", command=clear_chat, bg="#f44336", fg="white", font=("Segoe UI", 10, "bold"))
clear_button.pack(side=tk.RIGHT, padx=(0, 10))

# Start main loop
window.mainloop()
