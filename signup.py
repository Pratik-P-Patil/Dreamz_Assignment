from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkcalendar import *
from tkinter import messagebox
import mysql.connector
import re


class SIGNUP_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Admin Register System")


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
        img1=img1.resize((1530,790),Image.ANTIALIAS)
        self.photo_img1=ImageTk.PhotoImage(img1)
        

        bg_img=Label(self.root,image=self.photo_img1)
        bg_img.place(x=0,y=0,width=1530,height=790)



       
        

    
        # =====main frame===
        frame=Frame(self.root,bg="#FAD5A5")
        frame.place(x=250,y=50,width=800,height=650)

        register_label=Label(frame,text="REGISTER HERE",font=("Yatra One",20,"bold"),bg="white",fg="black")
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



        confirm_pswd=Label(frame,text="Confirm Password",font=("Yatra One",15,"bold"),bg="white")
        confirm_pswd.place(x=50,y=380)

        confirm_pswd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("Yatra One",15,"bold"))
        confirm_pswd_entry.place(x=50,y=415,width=250)

  


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


  

      

        register_btn=Button(frame,text="Register",command=self.register_data,width=17,font=("Yatra one",12,"bold"),bg="#E63530",fg="black")
        register_btn.place(x=370,y=425,width=300)

        login_button=Button(frame,command=self.return_login,text="Login",font=("Yatra One",12,"bold"),cursor="hand2",bd=3,relief=RIDGE,fg="black",bg="#4CE64C",activebackground="#ED9D2C")
        login_button.place(x=370,y=490,width=300)


        
    def register_data(self):
      
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ=="Select-Question":
            messagebox.showerror("Error","All Fields Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password Or Confirm Password Must Be Same.")
        elif not re.search("[A-Z]",self.var_pass.get()):
             messagebox.showerror("Error","Aleast one Capitale Letter")
        elif (int(len(self.var_pass.get())<8)):
             messagebox.showerror("Error","Minimum 8 characters required")
        
        else:
             conn=mysql.connector.connect(host="localhost",username="root",password="pratik",database="dreamz")
             my_cursor=conn.cursor()
             query=("select * from profile where email=%s")
             value=(self.var_email.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             if row!=None:
                 messagebox.showerror("Error","User already exist try another email")
             else:
                 my_cursor.execute("insert into profile values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_fname.get(),
                                                                                                        self.var_lname.get(),
                                                                                                       
                                                                                                        self.var_email.get(),
                                                                                                        self.var_securityQ.get(),
                                                                                                        self.var_securityA.get(),
                                                                                                        self.var_pass.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.selected_date.get(),
                                                                                                        
                                                                                                    ))
             conn.commit()
             conn.close()
             messagebox.showinfo("success","Information fill Successfully",parent=self.root)


    def return_login(self):
        self.root.destroy()


if __name__== "__main__":
    root=Tk()
    obj=SIGNUP_System(root)
    root.mainloop()
