import requests
import tkinter as tk
from tkinter import scrolledtext

API_KEY = "pub_e01786d969bd455ea939b8aceea71f14" 

def fetch_news():
    city = city_entry.get().strip()
    
    # Romania-only news + city keyword
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&country=ro&q={city}"
    
    response = requests.get(url)
    
    try:
        data = response.json()   # ensure JSON
    except ValueError:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "Error: Response was not valid JSON.\n")
        text_area.insert(tk.END, response.text)
        return
    
    if not isinstance(data, dict):
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, f"Unexpected response type: {type(data)}\n")
        text_area.insert(tk.END, str(data))
        return
    
    articles = data.get("results", [])
    
    # Clear previous text
    text_area.delete(1.0, tk.END)
    
    if articles:
        for article in articles:
            title = article.get("title", "No Title")
            link = article.get("link", "")
            text_area.insert(tk.END, f"• {title}\n{link}\n\n")
    else:
        text_area.insert(tk.END, f"No articles found for city: {city}")

# --- GUI setup ---
window = tk.Tk()
window.title("Romania News")

# City input field
tk.Label(window, text="Enter city name:").pack(pady=5)
city_entry = tk.Entry(window, width=30)
city_entry.pack(pady=5)

# Fetch button
fetch_button = tk.Button(window, text="Fetch News for City", command=fetch_news)
fetch_button.pack(pady=5)

# Scrollable text area
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=20)
text_area.pack(padx=10, pady=10)

window.mainloop()
