import tkinter as tk 
from tkinter import messagebox

class Management: 
    #main window
    def __init__(self, root):
        self.window = root
        self.window.title("Computer Store Information Management")
        self.window.geometry("800x600")
        self.window.resizable(False, False)


# #FFFFFA: trắng, #A41623: đỏ, #141204: đen
# ========================== Top Menu ==========================

        # overall bg
        self.data_frame=tk.Label(self.window, relief = tk.GROOVE,  bg = '#FFFFFA')
        self.data_frame.place(x = 0, y = 0, width = 800, height = 600)

        #main title frame
        self.title_label  = tk.Label(
            self.data_frame,
            text = "Computer Store Information Management",
            font = ("Franklin Gothic Medium",13,"bold"),
            foreground = "white",
            padx = 100,
            pady = 20,
            bg = "#A41623",
            relief = tk.GROOVE
        )
        self.title_label.pack(side = tk.TOP,fill = tk.X)

        #main info frame
        self.info_frame = tk.Frame(
            bg = '#FFFFFA',
            height = 500,
            width = 1540
        )
        self.info_frame.pack(side=tk.BOTTOM)

        #frame for display buttons: staff, customer, product
        self.detail_frame = tk.Frame(
            self.window,
            bg='#FFFFFA'
        )
        self.detail_frame.place(y = 60, width = 800, height = 80)

        #Button Frame For Display Staff
        self.btn_frame_for_list = tk.Frame(
            self.detail_frame,
            bg ='#FFFFFA',
            relief = tk.GROOVE
        )
        self.btn_frame_for_list.place(x = 25, y = 20, width = 150, height = 85)
        #Display Staff Button
        self.stflist_btn=tk.Button(
            self.btn_frame_for_list,
            bg = '#A41623',
            foreground = 'white',
            text = 'Staff List',
            bd = 2,
            font = ("Franklin Gothic Medium",13),
            width = 15,
            relief = tk.GROOVE
        )
        self.stflist_btn.grid(row = 0, column = 0, padx = 1, pady = 2)

        #Button Frame for Display Customer
        self.btn_frame_for_list = tk.Frame(
            self.detail_frame,
            bg = '#FFFFFA',
            relief = tk.GROOVE
        )
        self.btn_frame_for_list.place(x = 325, y = 20, width = 150, height = 85)
        #Display Customer Buttom
        self.ctmlist_btn = tk.Button(
            self.btn_frame_for_list,
            bg = '#A41623',
            foreground = 'white',
            text = 'Customer List',
            bd = 2,
            font = ("Franklin Gothic Medium",13),
            width = 15,
            relief = tk.RIDGE
        )
        self.ctmlist_btn.grid(row = 0, column = 0, padx = 2, pady = 2)

        #Button Frame for Dispaly Product
        self.btn_frame_for_input = tk.Frame(
            self.detail_frame,
            bg='#FFFFFA',
            relief=tk.RIDGE
        )
        self.btn_frame_for_input.place(x = 625, y = 20, width = 150, height = 85)
        #Display Product Button
        self.prdlist_btn=tk.Button(
            self.btn_frame_for_input,
            bg='#A41623',
            foreground='white',
            text='Product list',
            font=("Franklin Gothic Medium",13),
            width=15,
            relief=tk.RIDGE
        )
        self.prdlist_btn.grid(row = 0, column = 0, padx = 2, pady = 2)

        # Create a label in the info_frame to display the text
        self.display_label = tk.Label(
            self.info_frame,
            font = ("Franklin Gothic Medium", 15),
            bg = '#FFFFFA',
            justify = tk.CENTER,
            anchor = tk.CENTER,
        )
        # self.display_label.pack(fill=tk.BOTH, expand=1)
        self.display_label.place(x = 25, y = 300)

        # configure stflist_btn to display the staff list
        self.stflist_btn.config(command = self.display_staff_list)

        # add staff 
        self.add_stf_btn = tk.Button(
            self.info_frame,
            text = "Add Staff",
            font = ("Franklin Gothic Medium", 13),
            width = 15,
            relief = tk.RAISED,
            command = self.show_staff_input_frame  # add this line to set the command
        )
        self.add_stf_btn.place()
        # delete staff
        self.dlt_stf_btn = tk.Button(
            self.info_frame,
            text = "Delete Staff",
            font = ("Franklin Gothic Medium", 13),
            width = 15,
            relief = tk.SUNKEN
        ) 
        # search staff
        self.src_stf_btn = tk.Button(
            self.info_frame,
            text = "Search Staff",
            font = ("Franklin Gothic Medium", 13),
            width = 15,
            relief = tk.GROOVE
        )

        # hide the staff buttons initially
        self.add_stf_btn.place_forget()
        self.dlt_stf_btn.place_forget()
        self.src_stf_btn.place_forget()

        # configure add_btn to display the stf buttons
        self.stflist_btn.config(command = self.display_staff_buttons)

        # add customer
        self.add_ctm_btn = tk.Button(
            self.info_frame,
            text = "Add Customer",
            font = ("Franklin Gothic Medium", 13),
            width = 15,
            relief = tk.RAISED  # add this line to set the command
        )
        #delete customer
        self.dlt_ctm_btn = tk.Button(
            self.info_frame,
            text = "Delete Customer",
            font = ("Franklin Gothic Medium", 13),
            width = 15,
            relief = tk.SUNKEN
        )
        #search customer
        self.src_ctm_btn = tk.Button(
            self.info_frame,
            text = "Search Customer",
            font = ("Franklin Gothic Medium", 13),
            width = 15,
            relief = tk.GROOVE
        )

        # hide the product buttons initially
        self.add_ctm_btn.place_forget()
        self.dlt_ctm_btn.place_forget()
        self.src_ctm_btn.place_forget()

        # configure add_btn to display the customer buttons
        self.ctmlist_btn.config(command = self.display_customer_buttons)

        # add product
        self.add_prd_btn = tk.Button(
            self.info_frame,
            text = "Add Product",
            font = ("Franklin Gothic Medium", 13),
            width = 15,
            relief = tk.RAISED  # add this line to set the command
        )
        # delete product
        self.dlt_prd_btn = tk.Button(
            self.info_frame,
            text = "Delete Product",
            font = ("Franklin Gothic Medium", 13),
            width = 15,
            relief = tk.SUNKEN
        )
        # search product 
        self.src_prd_btn = tk.Button(
            self.info_frame,
            text = "Search Product",
            font = ("Franklin Gothic Medium", 13),
            width = 15,
            relief = tk.GROOVE
        )

        # hide the product buttons initially
        self.add_prd_btn.place_forget()
        self.dlt_prd_btn.place_forget()
        self.src_prd_btn.place_forget()

        # configure add_btn to display the product buttons
        self.prdlist_btn.config(command = self.display_product_buttons)

    def display_staff_list(self):
        # hide the staff/course list labels if they are visible
        self.display_label.place_forget()
        # display the staff list label
        self.display_label.config(text = "This is the staff list")
        self.display_label.place(x = 25, y = 50)

    def display_customer_list(self):
        # hide the product buttons if they are visible
        self.add_prd_btn.place_forget()
        self.dlt_prd_btn.place_forget()
        self.src_prd_btn.place_forget()

        # hide the staff buttons if they are visible
        self.add_stf_btn.place_forget()
        self.dlt_stf_btn.place_forget()
        self.src_stf_btn.place_forget()

        # display the customer list label
        self.display_label.config(text = "This is the customer list")
        self.display_label.place(x = 500, y = 100)

    def display_staff_buttons(self):
        # hide the staff/customer list labels if they are visible
        self.display_label.place_forget()

        # hide the customer buttons if they are visible
        self.add_ctm_btn.place_forget()
        self.dlt_ctm_btn.place_forget()
        self.src_ctm_btn.place_forget()
        
        # hide the product buttons if they are visible
        self.add_prd_btn.place_forget()
        self.dlt_prd_btn.place_forget()
        self.src_prd_btn.place_forget()

        # display the staff buttons
        self.add_stf_btn.place(x = 100, y = 400)
        self.dlt_stf_btn.place(x = 300, y = 400)
        self.src_stf_btn.place(x = 500, y = 400)

    def display_customer_buttons(self):
        # hide the staff/customer list labels if they are visible
        self.display_label.place_forget()

        # hide the staff buttons if they are visible
        self.add_stf_btn.place_forget()
        self.dlt_stf_btn.place_forget()
        self.src_stf_btn.place_forget()

        # hide the product buttons if they are visible
        self.add_prd_btn.place_forget()
        self.dlt_prd_btn.place_forget()
        self.src_prd_btn.place_forget()

        # display the customer buttons
        self.add_ctm_btn.place(x = 100, y = 400)
        self.dlt_ctm_btn.place(x = 300, y = 400)
        self.src_ctm_btn.place(x = 500, y = 400)

    def display_product_buttons(self):
        # hide the staff/customer list labels if they are visible
        self.display_label.place_forget()

        # hide the staff buttons if they are visible
        self.add_stf_btn.place_forget()
        self.dlt_stf_btn.place_forget()
        self.src_stf_btn.place_forget()

        # hide the customer buttons if they are visible
        self.add_ctm_btn.place_forget()
        self.dlt_ctm_btn.place_forget()
        self.src_ctm_btn.place_forget()

        # display the product buttons
        self.add_prd_btn.place(x = 100, y = 400)
        self.dlt_prd_btn.place(x = 300, y = 400)
        self.src_prd_btn.place(x = 500, y = 400)

    def show_staff_input_frame(self):
        # hide the staff buttons if they are visible
        self.add_stf_btn.place_forget()
        self.dlt_stf_btn.place_forget()
        self.src_stf_btn.place_forget()

        # hide the customer buttons if they are visible
        self.add_ctm_btn.place_forget()
        self.dlt_ctm_btn.place_forget()
        self.src_ctm_btn.place_forget()

        # hide the product buttons if they are visible
        self.add_prd_btn.place_forget()
        self.dlt_prd_btn.place_forget()
        self.src_prd_btn.place_forget()

        # create a new frame for staff input
        self.staff_input_frame = tk.Frame(
            self.info_frame,
            height = 900,
            width = 1300,
            bg = '#FFFFFA'
        )
        # display the staff input frame
        self.staff_input_frame.place(x = 0, y = 40)

        # create the widgets for the staff input frame
        # title
        self.stf_lab = tk.Label(
            self.staff_input_frame, 
            text="Enter Staff Info", 
            font=("Franklin Gothic Medium", 16))
        self.stf_lab.place(x = 20, y = 15)
        # name label
        self.staff_name_lab = tk.Label(
            self.staff_input_frame, 
            text="Name: ",
            font=("Franklin Gothic Medium", 16))
        self.staff_name_lab.place(x = 20, y = 55)
        #name entry
        self.staff_name_entry = tk.Entry(
            self.staff_input_frame, 
            font=("Franklin Gothic Medium", 13))
        self.staff_name_entry.place(x = 90, y = 55, width = 250, height = 30)
        #id label
        self.staff_id_lab = tk.Label(
            self.staff_input_frame,
            text="ID: ",
           font=("Franklin Gothic Medium", 16))
        self.staff_id_lab.place(x = 20, y = 95)
        #id entry
        self.staff_id_entry = tk.Entry(
            self.staff_input_frame, 
            font=("Franklin Gothic Medium", 13))
        self.staff_id_entry.place(x = 90, y = 95, width = 250, height = 30)

        # create a Back button
        self.back_button = tk.Button(
            self.staff_input_frame,
            text = "Back",
            font = ("Franklin Gothic Medium", 13),
            width = 15,
            relief = tk.FLAT,
            command = self.show_info_frame  # this command will show the previous frame
        )
        self.back_button.place(x = 500, y = 400)

        # create a Submit button
        self.submit_button = tk.Button(
            self.staff_input_frame, 
            text = "Submit", 
            font = ("Franklin Gothic Medium", 13),
            width = 15, 
            relief = tk.FLAT, 
            command = self.show_staff_list_frame #this command will show the staff list
        )
        self.submit_button.place(x = 300, y = 400)

        #create message box for invalid input
        name = self.staff_name_entry.get()
        id = self.staff_id_entry.get()

        if name == "" or id == "":
            messagebox.showerror('Error', 'Please enter a valide name or id.')
            return

    # info_frame    
    def show_info_frame(self):
        self.staff_input_frame.place_forget()   # hide the current frame
        self.info_frame.place()     # show the previous frame

    # staff_list_frame
    def show_staff_list_frame(self): 
        self.staff_input_frame.place_forget()   #hide the current frame 
        self.display_staff_list()   #show the staff list

# main function
if __name__ == "__main__":
    root = tk.Tk()
    obj = Management(root)
    root.mainloop()