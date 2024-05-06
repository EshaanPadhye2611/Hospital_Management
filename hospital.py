from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
       self.root=root
       self.root.title("Hospital Management System")
       self.root.geometry("1540x800+0+0")


       self.Nameoftablets=StringVar()
       self.ref=StringVar()
       self.Dose=StringVar()
       self.NumberofTablets=StringVar()
       self.Lot=StringVar()
       self.Issuedate=StringVar()
       self.ExpDate=StringVar()
       self.DailyDose=StringVar()
       self.sideEffect=StringVar()
       self.FurtherInformation=StringVar()
       self.StorageAdvice=StringVar()
       self.DrivingUsingMachine=StringVar()
       self.HowToUseMedication=StringVar()
       self.PatientID=StringVar()
       self.nhsNumber=StringVar()
       self.PatientName=StringVar()
       self.DateOfBirth=StringVar()
       self.PatientAddress=StringVar()
       self.SearchPatient=StringVar()
    
       lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("times new roman",40,"bold" ))
       lbltitle.pack(side=TOP,fill=X)
       

       #=================================Data Frame================================================

       SearchFrame=Frame(self.root,bd=10,relief=RIDGE)
       SearchFrame.place(x=0,y=80,width=560,height=70)

       DataFrame=Frame(self.root,bd=20,relief=RIDGE)
       DataFrame.place(x=0,y=130,width=1530,height=400)

       DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                         font=("times new roman",12,"bold" ),text="Patient Information")
       DataFrameLeft.place(x=0,y=5,width=980,height=350)
           
       DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                         font=("times new roman",12,"bold" ),text="Prescription")
       DataFrameRight.place(x=990,y=5,width=460,height=350)

       #===============================button frame=================================================

       ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
       ButtonFrame.place(x=0,y=530,width=1530,height=70)
       

       #===============================Details frame=================================================

       DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)
       DetailsFrame.place(x=0,y=600,width=1530,height=190)

       #=======================Data frame left=======================================================
       
       lblNameTablet=Label(DataFrameLeft,text="Names of Tablet",font=("arial",12,"bold" ),padx=2,pady=6)
       lblNameTablet.grid(row=0,column=0)
       txtNameTablet=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Nameoftablets,width=35)
       txtNameTablet.grid(row=0,column=1)



       lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No", padx=2)
       lblref.grid(row=1,column=0,sticky=W)
       txtref=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
       txtref.grid(row=1,column=1)

       lblDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dose Given", padx=2,pady=4)
       lblDose.grid(row=2,column=0,sticky=W)
       txtDose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
       txtDose.grid(row=2,column=1)

       lblNoOftablets=Label(DataFrameLeft,font=("arial",12,"bold"),text="No Of Tablets", padx=2,pady=6)
       lblNoOftablets.grid(row=3,column=0,sticky=W)
       txtNoOftablets=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.NumberofTablets,width=35)
       txtNoOftablets.grid(row=3,column=1)

       lblLot=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot", padx=2,pady=6)
       lblLot.grid(row=4,column=0,sticky=W)
       txtLot=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
       txtLot.grid(row=4,column=1)

       lblissueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date", padx=2,pady=6)
       lblissueDate.grid(row=5,column=0,sticky=W)
       txtissueDate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=35)
       txtissueDate.grid(row=5,column=1)

       lblExpDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Expiry Date", padx=2,pady=6)
       lblExpDate.grid(row=6,column=0,sticky=W)
       txtExpDate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=35)
       txtExpDate.grid(row=6,column=1)

       lblDailyDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose", padx=2,pady=4)
       lblDailyDose.grid(row=7,column=0,sticky=W)
       txtDailyDose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
       txtDailyDose.grid(row=7,column=1)

       
       lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect", padx=2,pady=6)
       lblSideEffect.grid(row=8,column=0,sticky=W)
       txtSideEffect=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.sideEffect,width=35)
       txtSideEffect.grid(row=8,column=1)

       lblFurtherInfo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Further Information", padx=2)
       lblFurtherInfo.grid(row=0,column=2,sticky=W)
       txtFurtherInfo=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.FurtherInformation,width=35)
       txtFurtherInfo.grid(row=0,column=3)

       
       lblBloodPressure=Label(DataFrameLeft,font=("arial",12,"bold"),text="BloodPressure", padx=2,pady=6)
       lblBloodPressure.grid(row=1,column=2,sticky=W)
       txtBloodPressure=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DrivingUsingMachine,width=35)
       txtBloodPressure.grid(row=1,column=3)


       lblStorage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage Advice", padx=2,pady=6)
       lblStorage.grid(row=2,column=2,sticky=W)
       txtStorage=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.StorageAdvice,width=35)
       txtStorage.grid(row=2,column=3)

       lblMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medication", padx=2,pady=6)
       lblMedicine.grid(row=3,column=2,sticky=W)
       txtMedicine=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.HowToUseMedication,width=35)
       txtMedicine.grid(row=3,column=3,sticky=W)

       lblPatientID=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient ID", padx=2,pady=6)
       lblPatientID.grid(row=4,column=2,sticky=W)
       txtPatientID=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.PatientID,width=35)
       txtPatientID.grid(row=4,column=3,sticky=W)

       
       lblNhsNumber=Label(DataFrameLeft,font=("arial",12,"bold"),text="NHS Number", padx=2,pady=6)
       lblNhsNumber.grid(row=5,column=2,sticky=W)
       txtNhsNumber=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.nhsNumber,width=35)
       txtNhsNumber.grid(row=5,column=3,sticky=W)

        
       lblPatientname=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Name", padx=2,pady=6)
       lblPatientname.grid(row=6,column=2,sticky=W)
       txtPatientname=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.PatientName,width=35)
       txtPatientname.grid(row=6,column=3,sticky=W)

         
       lblDateOfBirth=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Of Birth", padx=2,pady=6)
       lblDateOfBirth.grid(row=7,column=2,sticky=W)
       txtDateOfBirth=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DateOfBirth,width=35)
       txtDateOfBirth.grid(row=7,column=3,sticky=W)

       lblPatientAddress=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Address", padx=2,pady=6)
       lblPatientAddress.grid(row=8,column=2,sticky=W)
       txtPatientAddress=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.PatientAddress,width=35)
       txtPatientAddress.grid(row=8,column=3,sticky=W)
    
       
       lblPatientName=Label(SearchFrame,font=("arial",12,"bold"),text="Patient Name", padx=2,pady=6)
       lblPatientName.grid(row=0,column=0,sticky=W)
       txtPatientName=Entry(SearchFrame,font=("arial",13,"bold"),textvariable=self.SearchPatient,width=35)
       txtPatientName.grid(row=0,column=1,sticky=W)


       #==========================Data frame left====================================================
       
       self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=4)
       self.txtPrescription.grid(row=0,column=0)
    
       #==========================Buttons============================================================
       
       btnPrescription = Button(ButtonFrame,command=self.iPrescription, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
       btnPrescription.grid(row=0, column=0)

       btnPrescriptionData = Button(ButtonFrame, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6, command=self.iPrescriptionData)
       btnPrescriptionData.grid(row=0, column=1)


       btnUpdate = Button(ButtonFrame,command=self.update_data, text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
       btnUpdate.grid(row=0, column=2)

       btnDelete = Button(ButtonFrame,command=self.idelete, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
       btnDelete.grid(row=0, column=3)

       btnClear = Button(ButtonFrame,command=self.clear, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
       btnClear.grid(row=0, column=4)

       btnExit = Button(ButtonFrame, command=self.exit, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=23, padx=2, pady=6)
       btnExit.grid(row=0, column=5)

       btnSearch =Button(SearchFrame,command=self.search, text="Search", bg="green", fg="white", font=("arial", 12, "bold"), width=10, padx=2, pady=4)
       btnSearch.grid(row=0, column=7)


       #============================Table================================================================
       #============================Scroll Bar===========================================================

       scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
       self.hospital_table=ttk.Treeview(DetailsFrame,columns=("nameoftable","ref","dose","nooftablets","lot","issuedate"
                                                              ,"expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)

       scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
       scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)


       self.hospital_table.heading("nameoftable",text="Name of table")
       self.hospital_table.heading("ref",text="Reference No")
       self.hospital_table.heading("dose",text="Dose")
       self.hospital_table.heading("nooftablets",text="No of Tablets")
       self.hospital_table.heading("lot",text="Lot")
       self.hospital_table.heading("issuedate",text="Issue Date")
       self.hospital_table.heading("expdate",text="Exp Date")
       self.hospital_table.heading("dailydose",text="Daily Dose")
       self.hospital_table.heading("storage",text="Storage")
       self.hospital_table.heading("nhsnumber",text="NHS Number")
       self.hospital_table.heading("pname",text="Patient Name")
       self.hospital_table.heading("dob",text="DOB")
       self.hospital_table.heading("address",text="Address")

       self.hospital_table["show"]="headings"
       self.hospital_table.pack(fill=BOTH,expand=1)
       self.hospital_table.column("nameoftable",width=100)
       self.hospital_table.column("ref",width=100)
       self.hospital_table.column("dose",width=100)
       self.hospital_table.column("nooftablets",width=100)
       self.hospital_table.column("lot",width=100)
       self.hospital_table.column("issuedate",width=100)
       self.hospital_table.column("expdate",width=100)
       self.hospital_table.column("dailydose",width=100)
       self.hospital_table.column("storage",width=100)
       self.hospital_table.column("nhsnumber",width=100)
       self.hospital_table.column("pname",width=100)
       self.hospital_table.column("dob",width=100)
       self.hospital_table.column("address",width=100)

       self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

       self.fetch_data()
       
       #============================Functionality Declaration===========================

    def iPrescriptionData(self):
       print("Inserting prescription data...")
       if self.Nameoftablets.get()=="" or self.ref.get()=="":
           messagebox.showerror("Error","All fields are required")
       else :
            conn=mysql.connector.connect(host="localhost",username="root",password="astro",database="hospital")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
               
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been Inserted Successfully")
    
    def update_data(self):
     try:
        Reference_no = (self.ref.get()) 
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
           messagebox.showerror("Error","All fields are required")
        else:
          conn=mysql.connector.connect(host="localhost",username="root",password="astro",database="hospital")
          my_cursor=conn.cursor()
          my_cursor.execute("UPDATE hospital SET NameOftablets=%s,dose=%s,Numberoftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,DOB=%s,patientaddress=%s where Reference_No = %s",(
            self.Nameoftablets.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.Issuedate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.nhsNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get(),
            self.ref.get()
        ))
        conn.commit()
        conn.close()

        messagebox.showinfo("Update","Record has been Update Successfully")
     except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

        

    def fetch_data(self):
        
        conn=mysql.connector.connect(host="localhost",username="root",password="astro",database="hospital")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()    
       
     
    def get_cursor(self,event=""):

         cursor_row=self.hospital_table.focus()
         content=self.hospital_table.item(cursor_row)
         row=content["values"]
         self.Nameoftablets.set(row[0])
         self.ref.set(row[1])
         self.Dose.set(row[2])
         self.NumberofTablets.set(row[3])
         self.Lot.set(row[4])
         self.Issuedate.set(row[5])
         self.ExpDate.set(row[6])
         self.DailyDose.set(row[7])
         self.StorageAdvice.set(row[8])
         self.nhsNumber.set(row[9])
         self.PatientName.set(row[10])
         self.DateOfBirth.set(row[11])
         self.PatientAddress.set(row[12])
    
    def iPrescription(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t" +self.Nameoftablets.get() + "\n")
        self.txtPrescription.insert(END,"Reference_No:\t\t\t" +self.ref.get() + "\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t" +self.Dose.get() + "\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t" +self.Lot.get() + "\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t" +self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t" +self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t" +self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END,"Side Effects:\t\t\t" +self.sideEffect.get() + "\n")
        self.txtPrescription.insert(END,"Futher Information:\t\t\t" +self.FurtherInformation.get() + "\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t" +self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t" +self.DrivingUsingMachine.get() + "\n")
        self.txtPrescription.insert(END,"Patient ID:\t\t\t" +self.PatientID.get() + "\n")
        self.txtPrescription.insert(END,"NHSNumber:\t\t\t" +self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t" +self.PatientName.get() + "\n")
        self.txtPrescription.insert(END,"Date Of Birth:\t\t\t" +self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END,"PatientAddress:\t\t\t" +self.PatientAddress.get() + "\n")

    def idelete(self):

        if self.Nameoftablets.get()=="" or self.ref.get()=="":
           messagebox.showerror("Error","All fields are required")
        else:
          conn=mysql.connector.connect(host="localhost",username="root",password="astro",database="hospital")
          my_cursor=conn.cursor()
          query ="delete from hospital where Reference_No=%s" 
          value=(self.ref.get(),)
          my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")

    
    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientID.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)
        
    def exit(self):
        
        exit=messagebox.askyesno("Hospital Management System","Confirm you want to exit ?")
        if exit>0:
           root.destroy()
           return

    def search(self):
      conn = mysql.connector.connect(host="localhost", username="root", password="astro", database="hospital")
      my_cursor = conn.cursor()
      my_cursor.execute("SELECT * FROM hospital WHERE patientname = %s", (self.SearchPatient.get(),))
      row = my_cursor.fetchone()
      if row:
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])
        self.txtPrescription.delete(1.0, END)
        self.txtPrescription.insert(END, f"Name of Tablets:\t\t\t{row[0]}\n")
        self.txtPrescription.insert(END, f"Reference No:\t\t\t{row[1]}\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t" +self.Dose.get() + "\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t" +self.Lot.get() + "\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t" +self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t" +self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t" +self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END,"Side Effects:\t\t\t" +self.sideEffect.get() + "\n")
        self.txtPrescription.insert(END,"Futher Information:\t\t\t" +self.FurtherInformation.get() + "\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t" +self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t" +self.DrivingUsingMachine.get() + "\n")
        self.txtPrescription.insert(END,"Patient ID:\t\t\t" +self.PatientID.get() + "\n")
        self.txtPrescription.insert(END,"NHSNumber:\t\t\t" +self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t" +self.PatientName.get() + "\n")
        self.txtPrescription.insert(END,"Date Of Birth:\t\t\t" +self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END,"PatientAddress:\t\t\t" +self.PatientAddress.get() + "\n")

       
      else:
        messagebox.showinfo("Search", "No matching record found")
      conn.close()

       
        
       


root=Tk()
ob=Hospital(root)
root.mainloop()
