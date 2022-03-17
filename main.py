from tkinter import *  # imports everything from tkinter(classes and constants)
from tkinter import messagebox  # this is used for pop-ups
import random
import pyperclip  # to copy/paste text in/from clipboard


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	# choose random symbols from lists above and add them in another list
	nr_letters = random.randint(8, 10)
	nr_numbers = random.randint(2, 4)
	nr_symbols = random.randint(2, 4)

	password_list = [random.choice(letters) for _ in range(nr_letters)]  # these lines are same es for loops below
	password_list += [random.choice(numbers) for _ in range(nr_numbers)]
	password_list += [random.choice(symbols) for _ in range(nr_symbols)]

	# for char in range(nr_letters):
	# 	password_list.append(random.choice(letters))
	#
	# for char in range(nr_symbols):
	# 	password_list += random.choice(symbols)
	#
	# for char in range(nr_numbers):
	# 	password_list += random.choice(numbers)

	random.shuffle(password_list)  # shuffle new list to randomize character order

	password = "".join(password_list)  # join all members of list togather
	password_entry.insert(END, string=f"{password}")
	pyperclip.copy(password)  # copies the password in clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
	# get hold of text user typed
	web = website_entry.get()
	user_name = username_entry.get()
	pass_word = password_entry.get()

	# pop_ups
	if len(web) <= 0 or len(user_name) <= 0 or len(pass_word) <= 0:  # tell user if he/she left field unfilled
		messagebox.showwarning(title="Warning!", message="please fill all the fields first.")
	else:
		want_to_save = messagebox.askyesno(title=web, message="Do you want to save password for this site? ")  # ask user -
		# if they want to save password, returns boolean
		if want_to_save:
			# write that data to a .txt file
			data = open("data.txt", "a")  # "a" stands for append, text will be added to the end of the existing text
			data.write(f"{web} // {user_name} // {pass_word} \n")
			data.close()  # file needs to be closed

			# delete text from entry fields
			website_entry.delete(0, END)
			password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# create window
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

# create canvas with photo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)  # to show canvas on the screen

# create labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)


username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# create entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2,  sticky="EW")  # "sticky" parameter, the "EW" part is the compass -
# - directions (E)ast and (W)est and the sticky basically "sticks" the widget to the edges of the column
website_entry.focus()  # Puts cursor in textbox

username_entry = Entry(width=35)
username_entry.insert(END, string="Example@gmail.com")  # Adds some text to begin with
username_entry.grid(column=1, row=2, columnspan=2,  sticky="EW")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3,  sticky="EW")

# create buttons
gen_password = Button(text="Generate Password", command=generate_password)
gen_password.grid(column=2, row=3)

add_but = Button(text="Add", width=36, command=save)
add_but.grid(column=1, row=4, columnspan=2,  sticky="EW")


window.mainloop()
