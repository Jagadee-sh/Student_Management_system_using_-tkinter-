import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Management System")

title_label = tk.Label(win, text="Student Management System", font=("times new roman", 20, "bold"), border=12, relief=tk.GROOVE, bg="black", fg="white")
title_label.pack(side=tk.TOP, fill=tk.X)

detail_frame = tk.LabelFrame(win, text="Student Details", font=("times new roman", 15, "bold"), bd=12, relief=tk.GROOVE, bg="lightgrey", fg="white")
detail_frame.place(x=20, y=100, width=420, height=575)

data_frame = tk.Frame(win, bd=12, bg="lightgrey", relief=tk.GROOVE)
data_frame.place(x=475, y=100, width=810, height=575)

# Variables
rollno = tk.StringVar()
name = tk.StringVar()
year = tk.StringVar()
branch = tk.StringVar()
contact = tk.StringVar()
email = tk.StringVar()
address = tk.StringVar()
cgpa = tk.StringVar()
dob = tk.StringVar()
gender = tk.StringVar()
search_by = tk.StringVar()
search_txt = tk.StringVar()

# Labels and Entries
rollno_lbl = tk.Label(detail_frame, text="Roll No", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black")
rollno_lbl.grid(row=0, column=0, padx=2, pady=2)
rollno_ent = tk.Entry(detail_frame, font=("times new roman", 15, "bold"), bg="white", fg="black", textvariable=rollno)
rollno_ent.grid(row=0, column=1, padx=2, pady=2)

name_lbl = tk.Label(detail_frame, text="Name", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black")
name_lbl.grid(row=1, column=0, padx=2, pady=2)
name_ent = tk.Entry(detail_frame, font=("times new roman", 15, "bold"), bg="white", fg="black", textvariable=name)
name_ent.grid(row=1, column=1, padx=2, pady=2)

year_lbl = tk.Label(detail_frame, text="Year", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black")
year_lbl.grid(row=2, column=0, padx=2, pady=2)
year_ent = tk.Entry(detail_frame, font=("times new roman", 15, "bold"), bg="white", fg="black", textvariable=year)
year_ent.grid(row=2, column=1, padx=2, pady=2)

branch_lbl = tk.Label(detail_frame, text="Branch", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black")
branch_lbl.grid(row=3, column=0, padx=2, pady=2)
branch_ent = tk.Entry(detail_frame, font=("times new roman", 15, "bold"), bg="white", fg="black", textvariable=branch)
branch_ent.grid(row=3, column=1, padx=2, pady=2)

contact_lbl = tk.Label(detail_frame, text="Contact", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black")
contact_lbl.grid(row=4, column=0, padx=2, pady=2)
contact_ent = tk.Entry(detail_frame, font=("times new roman", 15, "bold"), bg="white", fg="black", textvariable=contact)
contact_ent.grid(row=4, column=1, padx=2, pady=2)

email_lbl = tk.Label(detail_frame, text="Email", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black")
email_lbl.grid(row=5, column=0, padx=2, pady=2)
email_ent = tk.Entry(detail_frame, font=("times new roman", 15, "bold"), bg="white", fg="black", textvariable=email)
email_ent.grid(row=5, column=1, padx=2, pady=2)

address_lbl = tk.Label(detail_frame, text="Address", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black")
address_lbl.grid(row=6, column=0, padx=2, pady=2)
address_ent = tk.Text(detail_frame, width=28, height=2, font=("times new roman", 15, "bold"), bg="white", fg="black")
address_ent.grid(row=6, column=1, padx=2, pady=2)

cgpa_lbl = tk.Label(detail_frame, text="Cgpa", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black")
cgpa_lbl.grid(row=7, column=0, padx=2, pady=2)
cgpa_ent = tk.Entry(detail_frame, font=("times new roman", 15, "bold"), bg="white", fg="black", textvariable=cgpa)
cgpa_ent.grid(row=7, column=1, padx=2, pady=2)

gender_lbl = tk.Label(detail_frame, text="Gender", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black")
gender_lbl.grid(row=8, column=0, padx=2, pady=2)
gender_ent = ttk.Combobox(detail_frame, font=("times new roman", 15, "bold"), state="readonly", textvariable=gender)
gender_ent['values'] = ('male', 'female', 'other')
gender_ent.grid(row=8, column=1, padx=2, pady=2)

dob_lbl = tk.Label(detail_frame, text="D.O.B", font=("times new roman", 15, "bold"), bg="lightgrey", fg="black")
dob_lbl.grid(row=9, column=0, padx=2, pady=2)
dob_ent = tk.Entry(detail_frame, font=("times new roman", 15, "bold"), bg="white", fg="black", textvariable=dob)
dob_ent.grid(row=9, column=1, padx=2, pady=2)

# Functions
def fetch_data():
    con = pymysql.connect(host="localhost", user="root", password="", database="sms1")
    cur = con.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    if len(rows) != 0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('', tk.END, values=row)
        con.commit()
    con.close()

def add_func():
    if rollno.get() == "" or name.get() == "" or year.get() == "" or branch.get() == "" or contact.get() == "" or email.get() == "" or address_ent.get("1.0", tk.END).strip() == "" or cgpa.get() == "" or dob.get() == "" or gender.get() == "":  
        messagebox.showerror("Error", "All fields are required")
    else:
        con = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        cur = con.cursor()
        cur.execute("INSERT INTO data(rollno, name, year, branch, contact, email, address, dob, cgpa, gender) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                    (rollno.get(), name.get(), year.get(), branch.get(), contact.get(), email.get(), address_ent.get("1.0", tk.END).strip(), dob.get(), cgpa.get(), gender.get()))
        con.commit()
        con.close()
        fetch_data()

def get_cursor(event):
    cursor_row = student_table.focus()
    content = student_table.item(cursor_row)
    row = content['values']
    rollno.set(row[0])
    name.set(row[1])
    year.set(row[2])
    branch.set(row[3])
    contact.set(row[4])
    email.set(row[5])
    address_ent.delete("1.0", tk.END)
    address_ent.insert(tk.END, row[6])
    dob.set(row[7])
    cgpa.set(row[8])
    gender.set(row[9])

def clear():
    rollno.set("")
    name.set("")
    year.set("")
    branch.set("")
    contact.set("")
    email.set("")
    address_ent.delete("1.0", tk.END)
    dob.set("")
    cgpa.set("")
    gender.set("")

def update_func():
    if rollno.get() == "" or name.get() == "" or year.get() == "" or branch.get() == "" or contact.get() == "" or email.get() == "" or address_ent.get("1.0", tk.END).strip() == "" or cgpa.get() == "" or dob.get() == "" or gender.get() == "":  
        messagebox.showerror("Error", "All fields are required")
    else:
        con = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        cur = con.cursor()
        cur.execute("UPDATE data SET name=%s, year=%s, branch=%s, contact=%s, email=%s, address=%s, dob=%s, cgpa=%s, gender=%s WHERE rollno=%s", 
                    (name.get(), year.get(), branch.get(), contact.get(), email.get(), address_ent.get("1.0", tk.END).strip(), dob.get(), cgpa.get(), gender.get(), rollno.get()))
        con.commit()
        con.close()
        fetch_data()
        clear()

def delete_func():
    if rollno.get() == "":
        messagebox.showerror("Error", "Roll No is required to delete a record")
    else:
        con = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        cur = con.cursor()
        cur.execute("DELETE FROM data WHERE rollno=%s", rollno.get())
        con.commit()
        con.close()
        fetch_data()
        clear()

def search_data():
    if search_by.get() == "" or search_txt.get() == "":
        messagebox.showerror("Error", "Please select a search criteria and enter a search term")
    else:
        con = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        cur = con.cursor()
        query = f"SELECT * FROM data WHERE {search_by.get()} LIKE '%{search_txt.get()}%'"
        cur.execute(query)
        rows = cur.fetchall()
        if len(rows) != 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('', tk.END, values=row)
            con.commit()
        con.close()

# Buttons
btn_frame = tk.Frame(detail_frame, bd=12, bg="lightgrey", relief=tk.GROOVE)
btn_frame.place(x=18, y=390, width=354, height=120)

add_btn = tk.Button(btn_frame, text="Add", font=("times new roman", 13, "bold"), bd=5, width=15, bg="lightgrey", fg="white", command=add_func)
add_btn.grid(row=0, column=0, padx=2, pady=2)

delete_btn = tk.Button(btn_frame, text="Delete", font=("times new roman", 13, "bold"), bd=5, width=14, bg="lightgrey", fg="white", command=delete_func)
delete_btn.grid(row=0, column=1, padx=2, pady=2)

update_btn = tk.Button(btn_frame, text="Update", font=("times new roman", 13, "bold"), bd=5, width=15, bg="lightgrey", fg="white", command=update_func)
update_btn.grid(row=1, column=0, padx=2, pady=2)

clear_btn = tk.Button(btn_frame, text="Clear", font=("times new roman", 13, "bold"), bd=5, width=14, bg="lightgrey", fg="white", command=clear)
clear_btn.grid(row=1, column=1, padx=2, pady=2)

# Adding widgets to data frame
search_frame = tk.Frame(data_frame, bd=12, bg="lightgrey", relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_lbl = tk.Label(search_frame, text="Search By", font=("times new roman", 13, "bold"), bg="lightgrey", fg="black")
search_lbl.grid(row=0, column=0, padx=12, pady=2)

search_in = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), state="readonly", textvariable=search_by)
search_in['values'] = ('rollno', 'name', 'contact', 'email', 'branch', 'year')
search_in.grid(row=0, column=1, padx=12, pady=2)

search_txt_ent = tk.Entry(search_frame, font=("times new roman", 13, "bold"), bg="white", fg="black", textvariable=search_txt)
search_txt_ent.grid(row=0, column=2, padx=12, pady=2)

search_btn = tk.Button(search_frame, text="Search", font=("times new roman", 13, "bold"), bd=8, width=10, bg="lightgrey", fg="white", command=search_data)
search_btn.grid(row=0, column=3, padx=0.1, pady=2)

showall_btn = tk.Button(search_frame, text="Show All", font=("times new roman", 13, "bold"), bd=8, width=10, bg="lightgrey", fg="white", command=fetch_data)
showall_btn.grid(row=0, column=4, padx=0.1, pady=2)

# Table frame by database
main_frame = tk.Frame(data_frame, bd=12, bg="lightgrey", relief=tk.GROOVE)
main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

student_table = ttk.Treeview(main_frame, columns=('rollno', 'name', 'year', 'branch', 'contact', 'email', 'address', 'dob', 'cgpa', 'gender'), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_table.heading('rollno', text='Roll No')
student_table.heading('name', text='Name')
student_table.heading('year', text='Year')
student_table.heading('branch', text='Branch')
student_table.heading('contact', text='Contact')
student_table.heading('email', text='Email')
student_table.heading('address', text='Address')
student_table.heading('dob', text='D.O.B')
student_table.heading('cgpa', text='Cgpa')
student_table.heading('gender', text='Gender')

student_table['show'] = 'headings'
student_table.pack(fill=tk.BOTH, expand=1)

student_table.column('rollno', width=100)
student_table.column('name', width=100)
student_table.column('year', width=100)
student_table.column('branch', width=100)
student_table.column('contact', width=100)
student_table.column('email', width=100)
student_table.column('address', width=100)
student_table.column('dob', width=100)
student_table.column('cgpa', width=100)
student_table.column('gender', width=100)

student_table.pack(fill=tk.BOTH, expand=1)

fetch_data()

student_table.bind("<ButtonRelease-1>", get_cursor)

win.mainloop()