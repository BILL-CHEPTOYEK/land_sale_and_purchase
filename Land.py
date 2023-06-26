import tkinter as tk
import webbrowser

# Dictionary containing plot details
plot_details = {
    "P000": {"owner": "Bill", "for_sale": True, "number": "0785521231", "location": {"District": "Mbale", "street": "123_half_london"}},
    "P001": {"owner": "Johnny walker", "for_sale": True, "number": "0785555231", "location": {"District": "Mukono", "street": "231_nabuti"}},
    "P002": {"owner": "Jane Smith", "for_sale": False, "number": "0785347273", "location": {"District": "Jinja", "street": "161_Jinja_College_road"}},
    "P003": {"owner": "Robert debuk", "for_sale": True, "number": "0785560157", "location": {"District": "Kapchorwa", "street": "891_senior_quaters"}},
}

def open_google_maps(location):
    maps_url = f"https://www.google.com/maps/search/?api=1&query={location}"
    webbrowser.open_new(maps_url)

def get_plot_details():
    plot_number = entry.get()
    if plot_number in plot_details:
        details = plot_details[plot_number]
        owner = details["owner"]
        location = details["location"]

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Plot Number: {plot_number}\n")
        result_text.insert(tk.END, f"Owner: {owner}\n")
        result_text.insert(tk.END, f"Location: {location['District']}, {location['street']}\n")

        if details["for_sale"]:
            result_text.insert(tk.END, f"Phone Number: {details['number']}\n")
            google_maps_button.config(state=tk.NORMAL)
            google_maps_button.bind("<Button-1>", lambda e: open_google_maps(location))
        else:
            result_text.insert(tk.END, "This plot is not for sale\n")
            google_maps_button.config(state=tk.DISABLED)
            google_maps_button.unbind("<Button-1>")
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Invalid plot number\n")
        google_maps_button.config(state=tk.DISABLED)
        google_maps_button.unbind("<Button-1>")

# GUI window
window = tk.Tk()
window.title("Plot Details")
window.geometry("400x300")

# Creating and position the UI elements
label = tk.Label(window, text="Enter plot number:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()

submit_button = tk.Button(window, text="Submit", command=get_plot_details)
submit_button.pack(pady=10)

result_text = tk.Text(window, height=8, width=40)
result_text.pack(pady=10)

google_maps_button = tk.Button(window, text="Open in Google Maps", state=tk.DISABLED)
google_maps_button.pack(pady=10)

# Run the GUI event loop
window.mainloop()
