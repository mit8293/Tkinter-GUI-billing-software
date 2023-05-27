from tkinter import *
from ttkbootstrap import *

root = Window(themename="darkly")
style = Style('darkly')
root.title('Billing Software')
root.geometry('1270x685')
root.iconbitmap('icon.ico')
style.configure('warning.TLabel', font=('arial', 25, 'bold'))
headingLabel = Label(root,
                     text='Billing Software',
                     # font=('Calibri', 30, 'bold'),
                     # background='grey2',
                     # foreground='gold',
                     anchor='center',
                     style='warning.TLabel'
                     )
headingLabel.pack(fill=X)

# Customer details frame

style.configure('TLabelFrame', font=('arial', 25, 'bold'))
customer_details_frame = LabelFrame(root,
                                    text='Customer Details',
                                    style='warning.TLabelFrame'
                                    )
customer_details_frame.pack()

style.configure('CLabel', font=('arial', 15, 'bold'))
nameLabel = Label(customer_details_frame,
                  text='Name',
                  style='warning.CLabel'
                  )
nameLabel.grid_configure(row=0, column=0)

root.mainloop()
