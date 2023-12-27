import tkinter as tk

root = tk.Tk()
root.title("Vending Machine")

# coke label
coke_label = tk.Label(root, text = "Product Code for Coke - 1001 ($2.50)")
coke_label.pack()

#KitKat label
kitkat_label = tk.Label(root, text = "Product Code for Kitkat - 1002 ($1.75)")
kitkat_label.pack()



#product code label
product_code_label = tk.Label(root, text = "Enter Product Code:")
product_code_label.pack()

#product code entry
user_code = tk.Entry(root)
user_code.pack()

#product price label
product_price_label = tk.Label(root, text = "Enter Inserted Money ($):")
product_price_label.pack()

#product price entry
user_amount = tk.Entry(root)
user_amount.pack()

#Process button
process_button = tk.Button(root, text = "Process")
process_button.pack()

# display label 
display_label = tk.Label(root,text="")
display_label.pack()

def price_calculation():
  code = int(user_code.get())
  money = float(user_amount.get())
  # if the user wants coke
  if code == 1001 and money == 2.50:
    display_label.config(text="Paid!Coke is dispensing!")
  #if the user wants kitkat
  elif code == 1002 and money == 1.75:
    display_label.config(text="Paid!KitKat is dispensing!")
  # if the user does not type the code or amount correctly 
  else:
    display_label.config(text="Sorry, incorrect amount/code. Try again!")
    


# the process button will call the function 
process_button.config(command=price_calculation)


#Mainloop
root.mainloop()
