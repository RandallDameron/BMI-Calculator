#Needed for GUI
import tkinter as tk

def BMI_calc():
    height=float(height_entry.get())
    weight=float(weight_entry.get())

    if height<=0 or weight<=0:
        label.config(text="Height and Weight must be greater than 0!")

    #BMI Calculation
    bmi=(weight*703)/(height**2)

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Healty Weight"
    elif bmi < 30:
        category = "Overweight"
    elif bmi < 35:
        category = "Obesity Class I (Moderate)"
    elif bmi < 40:
        category = "Obesity Class II (Severe)"
    else:
        category = "Obesity Class II (Very Severe)"

    calculation.config(text=f"Your BMI is: {bmi:.1f} \n Category: {category}")

# Create a window
window=tk.Tk()
window.title("BMI Calculator")
window.geometry("300x250")

#Add a label
label=tk.Label(window,text="Input your information")
label.pack(pady=10)

#Input boxes
height_label = tk.Label(window, text="Height (inches):")
height_label.pack()

height_entry = tk.Entry(window)
height_entry.pack()

weight_label = tk.Label(window, text="Weight (lbs):")
weight_label.pack()

weight_entry = tk.Entry(window)
weight_entry.pack()

#Add a label
calculation=tk.Label(window,text="Results")
calculation.pack(pady=10)

#Add a button
button=tk.Button(window, text="Submit",command=BMI_calc)
button.pack()

#When the user pushes the "Enter Key", return results
window.bind("<Return>", lambda event: BMI_calc())

#Start the GUI event loop
window.mainloop()
