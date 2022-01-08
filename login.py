from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from signup import SIGNUP_System
from dashboad import Report_System



class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Admin Login System")


        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


      #  bg image
        img1=Image.open(r"Photo\back.png")
        img1=img1.resize((1530,790),Image.ANTIALIAS)
        self.photo_img1=ImageTk.PhotoImage(img1)

        bg_img=Label(self.root,image=self.photo_img1)
        bg_img.place(x=0,y=0,width=1530,height=790)

   


        frame=Frame(self.root,bg="#fff000")
        frame.place(x=610,y=120,width=340,height=450)



        login_label=Label(frame,text="Login Here",font=("Yatra One",15,"bold"),bg="white",fg="black")
        login_label.place(x=115,y=50)

        #label
        username=Label(frame,text="Username",font=("Yatra One",12,"bold"),bg="#fff000",fg="black")
        username.place(x=40,y=155)

        self.txtuser=ttk.Entry(frame,font=("Yatra One",12,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=Label(frame,text="Password",font=("Yatra One",12,"bold"),bg="#fff000",fg="black")
        password.place(x=40,y=210)

        self.txtpass=ttk.Entry(frame,font=("Yatra One",12,"bold"))
        self.txtpass.place(x=40,y=235,width=270)



        #loginbutton
        login_button=Button(frame,command=self.login,text="LOGIN",font=("Yatra One",12,"bold"),cursor="hand2",bd=3,relief=RIDGE,fg="black",bg="red",activebackground="#ED9D2C")
        login_button.place(x=110,y=300,width=120,height=35)

        #Registerbutton
        register_button=Button(frame,command=self.register_window,text="SIGN UP",font=("Yatra One",11,"bold"),cursor="hand2",borderwidth=0,relief=RIDGE,fg="black",bg="#fff000",activebackground="#87CEFB")
        register_button.place(x=10,y=350,width=160)

      



    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=SIGNUP_System(self.new_window)



    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="poku" and self.txtpass.get()=="poku":
            messagebox.showinfo("Successful","Valid User")
        else:
             conn=mysql.connector.connect(host="localhost",username="root",password="pratik",database="dreamz")
             my_cursor=conn.cursor()
             my_cursor.execute("select * from profile where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()

                                                                                             ))
             row=my_cursor.fetchone()
             if row==None:
                 messagebox.showerror("Error","Invalid Username and Password")
             else:
                 open_main=messagebox.askyesno("YesNo","Access only admin")
                 if open_main>0:
                     self.new_window=Toplevel(self.root)
                     self.app=Report_System(self.new_window)
                 else:
                     if not open_main:
                         return


             conn.commit()
             conn.close()

    

    # def forgot_password_window(self):
    #     if self.txtuser.get()=="":
    #         messagebox.showerror("Error","Please Enter the Email address to reset password")
    #     else:
    #         conn=mysql.connector.connect(host="localhost",username="root",password="pratik",database="project")
    #         my_cursor=conn.cursor()
    #         query=("select * from voter_officer_register where email=%s")
    #         value=(self.txtuser.get(),)
    #         my_cursor.execute(query,value)
    #         row=my_cursor.fetchone()

    #         if row==None:
    #             messagebox.showerror("Error","Please Enter The Valid Username")
    #         else:
    #             conn.close()
    #             self.new_window=Toplevel(self.root)
    #             self.app=Forget_Password(self.new_window)



if __name__== "__main__":
    root=Tk()
    obj=Login_System(root)
    root.mainloop()
