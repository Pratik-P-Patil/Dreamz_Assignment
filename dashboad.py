from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import geocoder
from tkcalendar import *
import re



class Report_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x990+0+0")
        self.root.title("Report System")


                # ======= Variable====

        self.var_fname=StringVar()
        self.var_lname=StringVar()
  
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_address=StringVar()
        self.selected_date=StringVar()


        #bg image
        img1=Image.open(r"Photo\pass_icon.png")
        img1=img1.resize((1530,990),Image.ANTIALIAS)
        self.photo_img1=ImageTk.PhotoImage(img1)
        

        bg_img=Label(self.root,image=self.photo_img1)
        bg_img.place(x=0,y=0,width=1530,height=990)



       
        

    
        # =====main frame===
        frame=Frame(self.root,bg="#FAD5A5")
        frame.place(x=250,y=10,width=800,height=650)

        register_label=Label(frame,text="UPDATE HERE",font=("Yatra One",20,"bold"),bg="white",fg="black")
        register_label.place(x=20,y=20)


        # ======= Label and Entry field ====

        fname=Label(frame,text="First Name",font=("Yatra One",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Yatra One",15,"bold"))
        fname_entry.place(x=50,y=135,width=250)



        lname=Label(frame,text="Last Name",font=("Yatra One",15,"bold"),bg="white")
        lname.place(x=50,y=170)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("Yatra One",15,"bold"))
        lname_entry.place(x=50,y=205,width=250)

        


        dob=Label(frame,text="Date Of Birth",font=("Yatra One",15,"bold"),bg="white")
        dob.place(x=450,y=135)

        dob= DateEntry(root, selectmode="day",year= 2022, month=1, day=1,textvariable=self.selected_date)
        dob.pack(pady=230)
     


         

        email=Label(frame,text="Username",font=("Yatra One",15,"bold"),bg="white")
        email.place(x=50,y=240)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("Yatra One",15,"bold"))
        email_entry.place(x=50,y=275,width=250)



        pswd=Label(frame,text="Password",font=("Yatra One",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        pass_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("Yatra One",15,"bold"))
        pass_entry.place(x=50,y=345,width=250)



        # confirm_pswd=Label(frame,text="Confirm Password",font=("Yatra One",15,"bold"),bg="white")
        # confirm_pswd.place(x=50,y=380)

        # confirm_pswd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("Yatra One",15,"bold"))
        # confirm_pswd_entry.place(x=50,y=415,width=250)

  


        security_Q=Label(frame,text="Select Security Quetions",font=("Yatra One",15,"bold"),bg="white")
        security_Q.place(x=50,y=450)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Yatra One",12),state="readonly")
        self.combo_security_Q["values"]=("Select-Question","Your Birth Place","Your Animal Name","Your School Name")
        self.combo_security_Q.place(x=50,y=485,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("Yatra One",15,"bold"),bg="white")
        security_A.place(x=50,y=520)

        security_A_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("Yatra One",15,"bold"))
        security_A_entry.place(x=50,y=520,width=250)

      


        address=Label(frame,text="Address",font=("Yatra One",15,"bold"),bg="white")
        address.place(x=50,y=555)

        address_entry=ttk.Entry(frame,textvariable=self.var_address,font=("Yatra One",15,"bold"))
        address_entry.place(x=50,y=590,width=250)


  

      

        register_btn=Button(frame,command=self.update_data,text="Update",width=17,font=("Yatra one",12,"bold"),bg="#E63530",fg="black")
        register_btn.place(x=370,y=425,width=300)




        #Down frame
        Down_frame=LabelFrame(root,bd=2,bg="white",relief=RIDGE,text="No Details",font=("Yantra One",12,"bold"))
        Down_frame.place(x=850,y=550,width=600,height=200)

        table_frame=Frame(Down_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=50,y=50,width=510,height=100)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.Report_table=ttk.Treeview(table_frame,columns=("fname","lname","email","securityQ","securityA","password","Address","date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Report_table.xview)
        scroll_y.config(command=self.Report_table.yview)


        self.Report_table.heading("fname",text="fname")
        self.Report_table.heading("lname",text="lname")
        self.Report_table.heading("email",text="email")
        self.Report_table.heading("securityQ",text="securityQ")
        self.Report_table.heading("securityA",text="securityA")
        self.Report_table.heading("password",text="password")
        self.Report_table.heading("Address",text="Address")
        self.Report_table.heading("date",text="date")
        self.Report_table["show"]="headings"



        self.Report_table.column("fname",width=100)
        self.Report_table.column("lname",width=100)
        self.Report_table.column("email",width=150)
        self.Report_table.column("securityQ",width=150)
        self.Report_table.column("securityA",width=100)
        self.Report_table.column("password",width=100)
        self.Report_table.column("Address",width=100)
        self.Report_table.column("date",width=100)

        self.Report_table.pack(fill=BOTH,expand=1)
        self.Report_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="pratik",database="dreamz")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from profile")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.Report_table.delete(*self.Report_table.get_children())
            for i in data:
                self.Report_table.insert("",END,values=i)
            conn.commit()
        conn.close()
  
    def get_cursor(self,event=""):
        cursor_focus=self.Report_table.focus()
        content=self.Report_table.item(cursor_focus)
        data1=content["values"]


        self.var_fname.set(data1[0]),
        self.var_lname.set(data1[1]),
        self.var_email.set(data1[2]),
        self.var_securityQ.set(data1[3]),
        self.var_securityA.set(data1[4]),
        self.var_pass.set(data1[5]),
        self.var_address.set(data1[6]),
        self.selected_date.set(data1[7])

    def update_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select-Question" or self.var_securityA.get()=="" or self.var_pass.get()=="" or  self.var_address.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do You Want To Update Voter Details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="pratik",database="dreamz")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update profile set fname=%s,lname=%s,securityQ=%s,securityA=%s,password=%s,Address=%s where email=%s",(

                                                                                                                                                                                                         self.var_fname.get(),
                                                                                                                                                                                                         self.var_lname.get(),
                                                                                                                                                                                                         self.var_securityQ.get(),
                                                                                                                                                                                                         self.var_securityA.get(),
                                                                                                                                                                                                         self.var_pass.get(),
                                                                                                                                                                                                         self.var_address.get(),
                                                                                                                                                                                                         
                                                                                                                                                                                                         
                                                                                                                                                                                                         self.var_email.get()
                                                                                                                                                                                                         
                                                                                                                                                                                                         
                                                                                                                                                                                                         ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Voter Details Update Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



if __name__== "__main__":
    root=Tk()
    obj=Report_System(root)
    root.mainloop()


