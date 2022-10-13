from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
import os
import datetime




gg='#134e86'#secondary color
g="blue"#color
gw="white"

def report():
                R1.destroy()
                
                def sr():
                        try:
                        
                                listbox1.delete(0,END)
                                listbox2.delete(0,END)
                                listbox3.delete(0,END)
                                
                                cm.execute("use "+str(ccd.get()))
                                cm.execute("select rollno from "+(mmd.get())+" where status_tot='Satisfactory'")
                                oo=cm.fetchall()
                                for item in oo:
                                    listbox1.insert(END,item)

                                
                                cm.execute("select rollno from "+(mmd.get())+" where status_tot='Unsatisfactory'")
                                oo=cm.fetchall()
                                for item in oo:
                                    listbox2.insert(END,item)

                                cm.execute("select rollno from "+(mmd.get())+" where status_tot='Miserable'")
                                oo=cm.fetchall()
                                for item in oo:
                                    listbox3.insert(END,item)
                        except:
                            ly.config(text="something went wrong",fg="red")
                        
                        
                         
                gg='#0a2845'#secondary color
                g="blue"#color
                gw="white"
                global R15
                R15= Tk()
                R15.resizable(width=FALSE, height=FALSE)
                R15.geometry('1280x720')
                R15.title('Login')
                R15.configure(background=g)

                Image_open=Image.open("bgre.jpg")
                image=ImageTk.PhotoImage(Image_open)
                logo=Label(R15,image=image,bg=gg)
                logo.place(x=0,y=0,bordermode="outside")

                fo=open("user.txt","r")
                myuser=fo.readline()
                mypass=fo.readline()
                fo.close()
                                                

                cl=mysql.connector.connect(host='localhost',user=myuser,password=mypass,database="dgclass")
                cm=cl.cursor()




                        
                def s(sub):
                    try:

                            my=[]
                            im=0
                            cm.execute("use "+str(sub))
                            cm.execute("show tables ")
                            wu=cm.fetchall()
                            for e in wu:
                             ep=e[im]
                             my.append(ep)
                            del my[-1]
                             

                            global mmd
                            mmd=StringVar()
                            droplist2=OptionMenu(R15,mmd,*my)
                            droplist2.config(width=5)
                            droplist2.place(x=280,y=30)
                    except:
                        ly.config(text="something went wrong",fg="red")



                def OnVsb(*args):
                        listbox1.yview(*args)
                        listbox2.yview(*args)
                        listbox3.yview(*args)
                       
                        


                def OnMouseWheel(event):
                    
                        listbox1.yview("scroll", (event.delta-100),"units")
                        listbox2.yview("scroll",(event.delta-100),"units")
                        listbox3.yview("scroll",(event.delta-100),"units")
                       
                        return "break"
                    

                def jui(x):
                   sr()


                listbox1 = Listbox(R15, width=7,borderwidth=0,fg="#3cff00", highlightthickness=0,selectbackground=gg,height=26,bg=gg,font="10")
                listbox1.bind("<MouseWheel>",OnMouseWheel)
                listbox1.place(x=90,y=200)


                listbox2 = Listbox(R15, width=7, height=26,fg="orange",highlightthickness=0,bg=gg,borderwidth=0,selectbackground=gg,font="10")
                listbox2.bind("<MouseWheel>",OnMouseWheel)
                listbox2.place(x=600,y=200)

                listbox3=Listbox(R15, width=7,borderwidth=0,fg="red",height=26,bg=gg,selectbackground=gg,font="10",highlightthickness=0)
                listbox3.bind("<MouseWheel>",OnMouseWheel)
                listbox3.place(x=1050,y=200)


                yscroll=Scrollbar(R15,command=OnVsb,orient=VERTICAL,width=10)
                yscroll.place(relx=1,x=-15,y=138,height=570)


                cy=[]
                im=0
                cm.execute("show tables")
                wu=cm.fetchall()
                for e in wu:
                    ep=e[im]
                    cy.append(ep)
                sk=str(cy)
                global ccd
                ccd=StringVar()
                droplist=OptionMenu(R15,ccd, *cy,command=s)
                droplist.config(width=5)
                droplist.place(x=25,y=30)



                b2=Button(R15,text="SEARCH",width=20,bg=gg,fg="white",font="5",relief=RAISED,overrelief=RIDGE,command=sr)
                b2.place(x=900,y=30)
                def hj():
                        R15.destroy()
                        afterlogin()

                back=Button(R15,text="HOME",bg="#1d8cf7",fg=gw,command=hj)
                back.place(x=1200,y=30)

                ly=Label(R15,bg=gg,font=('bold','20'))
                ly.place(x=400,y=250)

                R15.bind('<Return>',jui)
                R15.mainloop()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def afterlogin():
        global R2
        R2=Tk()
        R2.title("SELECT")
        R2.geometry("1280x720")
        R2.config(bg=gg)
        
        def delc ():

                
                        def newclass():
                                try:
                                        fo=open("user.txt","r")
               
                                        myuser=fo.readline()
                                        mypass=fo.readline()
                                        
               
                                        cl=mysql.connector.connect(host='localhost',user=myuser,password=mypass,database="dgclass")
                                        cm=cl.cursor()
                                        cll=mysql.connector.connect(host='localhost',user=myuser,password=mypass)
                                        cml=cll.cursor()
                                        cm.execute("""drop table """+str(cdelete.get()))
                                        cl.commit()
                                        cml.execute("drop database """+str(cdelete.get()))
                                        cll.commit()
                                        l.config(text="deleted",fg="green")
                                except:
                                        l.config(text="something went wrong",fg="red")
                                           
                        te=Toplevel(R2,bg=gg)
                        te.geometry("500x120")
                        te.title("EDIT")
                        te.resizable(height=FALSE,width=FALSE)
                        lp=Label(te,text="class name",bg=gg,fg=gw)
                        lp.place(x=15,y=5)
                        
                        
                        fo=open("user.txt","r")
                        myuser=fo.readline()
                        mypass=fo.readline()
                        fo.close()
                        cl=mysql.connector.connect(host='localhost',user=myuser,password=mypass)
                        cm=cl.cursor()

                        cy=[]
                        im=0
                        cm.execute("use dgclass")
                        cm.execute("show tables")
                        wu=cm.fetchall()
                        for e in wu:
                            ep=e[im]
                            cy.append(ep)
                        sk=str(cy)
                        
                        cy=[]
                        im=0
                        cm.execute("show tables")
                        wu=cm.fetchall()
                        for e in wu:
                            ep=e[im]
                            cy.append(ep)
                        sk=str(cy)
                        global cdelete
                        cdelete=StringVar()
                        droplist=OptionMenu(te,cdelete, *cy)
                        droplist.config(width=5)
                        droplist.place(x=200,y=5)


                        b=Button(te,text="delete",width=10,command=newclass)
                        b.place(x=200,y=55)
                        l=Label(te,bg=gg)
                        l.place(x=180,y=90)
                        R2.mainloop()
                
                
        
        def viewclass():
                
                        R2.destroy()                       
                        def s(sub):
                                        listbox1.delete(0,END)
                                        listbox2.delete(0,END)
                                        listbox3.delete(0,END)
                                        listbox4.delete(0,END)

                                        droplist.config(bg=g,fg="white")
                                       
                                        cm.execute("use dgclass")
                                        cm.execute("select rollno from "+str(cd.get()))
                                        oo=cm.fetchall()
                                        for item in oo:
                                         
                                         listbox2.insert(END,item)
                            
                                        cm.execute("use dgclass")
                                        cm.execute("select grno from "+str(cd.get()))
                                        oo=cm.fetchall()
                                        for item in oo:
                                         listbox1.insert(END,item)

                                        cm.execute("use dgclass")
                                        cm.execute("select fname from "+str(cd.get()))
                                        oo=cm.fetchall()
                                        for item in oo:
                                         listbox3.insert(END,item)

                                        cm.execute("use dgclass")
                                        cm.execute("select lname from "+str(cd.get()))
                                        oo=cm.fetchall()
                                        for item in oo:
                                         listbox4.insert(END,item)
                                    

                        def srch(x):
                                sr()
                                
                        gg='#0a2845'#secondary color
                        g="blue"#color
                        gw="white"
                        global R11
                        R11=Tk()
                        R11.title("")
                        R11.geometry("1280x720")
                        R11.config(bg=gg)
                        R11.resizable(width=FALSE, height=FALSE)

                        Image_open=Image.open("bgscl.jpg")
                        image=ImageTk.PhotoImage(Image_open)
                        logo=Label(R11,image=image,bg=gg)
                        logo.place(x=0,y=0,bordermode="outside")



                        def OnVsb(*args):
                                listbox1.yview(*args)
                                listbox2.yview(*args)
                                listbox3.yview(*args)
                                listbox4.yview(*args)
                            
                                


                        def OnMouseWheel(event):
                            
                                listbox1.yview("scroll", (event.delta-100),"units")
                                listbox2.yview("scroll",(event.delta-100),"units")
                                listbox3.yview("scroll",(event.delta-100),"units")
                                listbox4.yview("scroll",(event.delta-100),"units")
                                
                                return "break"
                            





                        listbox1 = Listbox(R11, width=10,borderwidth=0, highlightthickness=0,selectbackground=gg,height=30,bg=gg,fg=gw,font=("bold", 20))
                        listbox1.bind("<MouseWheel>",OnMouseWheel)
                        listbox1.place(x=35,y=150)


                        listbox2 = Listbox(R11, width=10, height=30,highlightthickness=0,bg=gg,borderwidth=0,selectbackground=gg,fg=gw,font=("bold", 20))
                        listbox2.bind("<MouseWheel>",OnMouseWheel)
                        listbox2.place(x=270,y=150)

                        listbox3=Listbox(R11, width=20,borderwidth=0,height=30,bg=gg,selectbackground=gg,fg=gw,font=("bold", 20),highlightthickness=0)
                        listbox3.bind("<MouseWheel>",OnMouseWheel)
                        listbox3.place(x=590,y=150)



                        listbox4=Listbox(R11, width=20,borderwidth=0,height=30,bg=gg,selectbackground=gg,fg=gw,font=("bold", 20),highlightthickness=0)
                        listbox4.bind("<MouseWheel>",OnMouseWheel)
                        listbox4.place(x=950,y=150)




                        yscroll=Scrollbar(R11,command=OnVsb,orient=VERTICAL,width=10)
                        yscroll.place(relx=1,x=-10,y=80,height=635)


                        a=mysql.connector.connect(user='root',password='1230')
                        mm=a.cursor()

                            






                        fo=open("user.txt","r")
                        myuser=fo.readline()
                        mypass=fo.readline()
                        fo.close()
                        cl=mysql.connector.connect(host='localhost',user=myuser,password=mypass)
                        cm=cl.cursor()

                        cy=[]
                        im=0
                        cm.execute("use dgclass")
                        cm.execute("show tables")
                        wu=cm.fetchall()
                        for e in wu:
                            ep=e[im]
                            cy.append(ep)
                        sk=str(cy)




                        cy=[]
                        im=0
                        cm.execute("show tables")
                        wu=cm.fetchall()
                        for e in wu:
                            ep=e[im]
                            cy.append(ep)
                        sk=str(cy)
                        global cd
                        cd=StringVar()
                        droplist=OptionMenu(R11,cd, *cy,command=s)
                        droplist.config(width=100)
                        droplist.place(x=490,y=30)
                        def back_afterlogin():
                                R11.destroy()
                                afterlogin()
                        back=Button(R11,text="HOME",width=5,bg=gg,fg=gw,command=back_afterlogin)
                        back.place(x=1200,y=30)




                        R11.bind('<Return>',srch)
                        R11.mainloop()

                                                            
                                                

                    
                


        menubar = Menu(R2)
        

        be= Menu(menubar)
        be.add_command(label="View",command=viewclass)
        be.add_command(label="delete",command=delc)
        menubar.add_cascade(label="Class", menu=be)
        R2.config(menu=menubar)


        Image_open=Image.open("bg2.jpg")
        image=ImageTk.PhotoImage(Image_open)
        logo=Label(R2,image=image,bg=gg)
        logo.place(x=0,y=0,bordermode="outside")

        b1=Button(R2,text="STUDENT AND REPORT",width=48,height=15,bg=g,fg="white",font="5",relief=FLAT,overrelief=RIDGE,borderwidth='5',activebackground=gw,command=std_re)
        b1.place(x=100,y=74)
        b1=Button(R2,text="NEW STUDENT",width=48,height=15,bg=g,fg="white",font="5",relief=FLAT,overrelief=RIDGE,borderwidth='5',activebackground=gw,command=new_student)
        b1.place(x=100,y=374)
        b1=Button(R2,text="NEW ATTENDANCE",width=48,height=15,bg=g,fg="white",font="5",relief=FLAT,overrelief=RIDGE,borderwidth='5',activebackground=gw,command=new_atten)
        b1.place(x=730,y=74)
        b1=Button(R2,text="CREATE NEW CLASS",width=48,height=15,bg=g,fg="white",font="5",relief=FLAT,overrelief=RIDGE,borderwidth='5',activebackground=gw,command=create_class)
        b1.place(x=730,y=374)

        b1=Button(R2,text="logout",width=5,bg=gg,fg=gw,command=R2.destroy)
        b1.place(x=1210,y=20)
        R2.mainloop()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def create_class():
                R2.destroy()
                def add():
                        try:
                                try:    
                                        ka=e1.get()
                                        kb=e2.get()
                                        kc=e3.get()
                                except:
                                   lc.congfig(text="something went wrong",fg="red")
                                finally:
                                        x=e2.get()
                                        y = [int(e) if e.isdigit() else e for e in x.split(',')]
                                        fo=open("user.txt","r")
                                        myuser=fo.readline()
                                        mypass=fo.readline()
                                        fo.close()
                                        ncl1=mysql.connector.connect(host='localhost',user=myuser,password=mypass,database="dgclass")
                                        ncl2=mysql.connector.connect(host='localhost',user=myuser,password=mypass)
                                        ncm1=ncl1.cursor()
                                        ncm2=ncl2.cursor()
                                    
                                        ncm1.execute("""create table """+str(e1.get())+"""
                                                           (
                                                            rollno    int auto_increment,
                                                            grno     int not null ,
                                                            fname    char(20) not null,
                                                            lname    char(20) not null,
                                                            primary key(rollno,grno)
                                                            );""")
                                        ncm1.execute("""ALTER TABLE """+str(e1.get())+""" AUTO_INCREMENT = """+str(e3.get()))
                                        ncl1.commit()
                                        ncm2.execute("""create database """+str(e1.get()))
                                        ncl2.commit()
                                        ncm2.execute("""use """+str(e1.get()))
                                        ncm2.execute("""create table subject (subjects varchar(10));""")
                                        for row in y:
                                           
                                           ncm2.execute("INSERT INTO subject(subjects) VALUES  ('%s')"%(row))
                                        ncl2.commit()
                        except:
                                lc.config(text="something went wrong",fg="red")
                        else:
                                lc.config(text="added",fg="spring green2")
                    

                                
                def ghu():
                    add()

                def clear(x):
                        e1.delete(0,END)
                        e2.delete(0,END)
                        e3.delete(0,END)
                        lc.config(text="")
                        
                R7= Tk()
                R7.resizable(width=FALSE, height=FALSE)
                R7.geometry('1280x720')
                R7.title('MAKE NEW CLASS')
                R7.configure(background=g)


                Image_open=Image.open("centry.jpg")
                image=ImageTk.PhotoImage(Image_open)
                logo=Label(R7,image=image,bg=gg)
                logo.place(x=0,y=0,bordermode="outside")

                e1=Entry(R7,width=10,font=("bold",15),highlightthickness=2)
                e1.bind('<Button-1>',clear)
                e1.place(x=425,y=275)
                e2=Entry(R7,width=40,font=("bold",15),highlightthickness=2)
                e2.place(x=425,y=360)
                e3=Entry(R7,width=10,font=("bold",15),highlightthickness=2)
                e3.place(x=425,y=460)

                b1=Button(R7,text="ADD",width=20,height=2,bg=gg,fg="white",font="5",relief=RAISED,overrelief=RIDGE,command=add)
                b1.place(x=400,y=520)
                def hu():
                        R7.destroy()
                        afterlogin()

                back=Button(R7,text="HOME",bg=gg,fg=gw,command=hu)
                back.place(x=1200,y=30)

                lc=Label(R7,font="10",bg=g)
                lc.place(x=400,y=580)
                R7.bind('<Return>',ghu)
                R7.mainloop()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def new_atten():
                R2.destroy()
                def add_att():
                          if(1+int(e1.get())>int(e2.get())):
                              
                              
                                              try:
                                                     p=mo.get()
                                                     mm.execute("USE "+classs)
                                                     mm.execute("""create table """+p+"""
                                                                                 (
                                                                                  rollno int,
                                                                                  primary key(rollno)
                                                                                  
                                                                                  );""")
                                                     for y in i:
                                                            mm.execute("alter table "+p+" add "+y+" int;")
                                                            mm.execute("alter table "+p+
                                                                       " add atten_"+y+" int;")
                                                            mm.execute("alter table "+p+
                                                                       " add per_"+y+" int;")
                                                            mm.execute("alter table "+p+
                                                                       " add status_"+y+" char(30);")
                                                     
                                                            
                                                     mm.execute("alter table "+p+" add total int;")
                                                     mm.execute("alter table "+p+" add tot_atten int;")
                                                     mm.execute("alter table "+p+" add per_tot int;")
                                                     mm.execute("alter table "+p+" add status_tot char(30);")
                                                     am.commit()
                                              except:
                                                  pass
                                              try:
                                              
                                                  rollno=r.get()
                                                     
                                                  mm.execute("insert into "+p+"(rollno)  values("+rollno+");")
                                                  am.commit()
                                              except:
                                                   pass
                                                 
                                              try:
                                                  a=int(e1.get())
                                                  b=int(e2.get())
                                              except:
                                                  l.config(text="some thing Went wrong\n at entry ",fg="red")
                                                  pass
                                                  
                                          
                                              try:
                                                  mm.execute("""update """+p+""" set """+str(sub.get())+"""="""+str(e1.get())+""" where rollno ="""+str(r.get()))
                                                  mm.execute("""update """+p+""" set atten_"""+str(sub.get())+"""="""+str(e2.get())+""" where rollno ="""+str(r.get()))
                                                  
                                                  a=int(e1.get())
                                                  b=int(e2.get())
                                                  per=b/a*100
                                                  mm.execute("""update """+p+""" set per_"""+str(sub.get())+"""="""+str(per)+""" where rollno ="""+str(r.get()))
                                                 
                                                  if(per>75):
                                                             status='Satisfactory'
                                                  elif(59<per<75):
                                                           status='Unsatisfactory'
                                                  elif(per<60):
                                                           status='Defaulter'
                                                  else:
                                                           pass
                                                  mm.execute("""update """+p+""" set status_"""+str(sub.get())+"""='"""+str(status)+"""' where rollno ="""+str(r.get()))
                                                  am.commit()

                                                  ki=[]
                                                  for u in i:
                                                      mm.execute("select "+str(u)+" from "+str(mo.get())+" where rollno ="+str(r.get()))
                                                      rr=mm.fetchall()
                                                      for e in rr:
                                                          try:
                                                           ki.append(int(e[0]))
                                                          except:
                                                              pass


                                                  kii=[]
                                                  for u in i:
                                                      mm.execute("select atten_"+str(u)+" from "+str(mo.get())+" where rollno ="+str(r.get()))
                                                      rr=mm.fetchall()
                                                      for e in rr:
                                                          try:
                                                           kii.append(int(e[0]))
                                                          except:
                                                              pass
                     
                                                  tot.set(sum(ki))
                                                  atot.set(sum(kii))
                                                  aq=int(tot.get())
                                                  bq=int(atot.get())
                                                  pertot=bq/aq*100
                                                  
                                                  

                                                  
                                                  if(pertot>75):
                                                             totstatus='Satisfactory'
                                                  elif(59<pertot<75):
                                                           totstatus='Unsatisfactory'
                                                  elif(pertot<60):
                                                           totstatus='Defaulter'
                                                  else:
                                                           pass
                                                  mm.execute("""update """+p+""" set total"""+"""="""+str(aq)+""" where rollno ="""+str(r.get()))
                                                  mm.execute("""update """+p+""" set tot_atten"""+"""="""+str(bq)+""" where rollno ="""+str(r.get()))
                                                  mm.execute("""update """+p+""" set per_tot"""+"""="""+str(pertot)+""" where rollno ="""+str(r.get()))
                                                  mm.execute("""update """+p+""" set status_tot"""+"""='"""+str(totstatus)+"""' where rollno ="""+str(r.get()))
                                                  v="Added "+str(sub.get())
                                                  l.config(text=v,fg="spring green2")
                                              except:
                                               l.config(text="some thing Went wrong",fg="red")
                          else:
                                  l.config(text="Attended lecture is more than total",fg="cyan")
                                  
                                
                def c(cl):
                       global classs
                       classs=cl
                       mm.execute("USE "+cl)
                       mm.execute("select * from subject")
                       cls=mm.fetchall()
                       global i
                       i=[]
                       m=0
                       for row in cls:
                              i.append(row[m])
                       global sub
                       sub=StringVar()
                       sub.set("SELECT")
                       droplist=OptionMenu(R8,sub, *i)
                       droplist.bind('<Button-1>',clear2)
                       droplist.config(width=20)
                       droplist.place(x=270,y=330)
                           

                       rsty=[]
                       im=0
                       mm.execute("use dgclass;")
                       mm.execute("select rollno from "+cl+"")
                       wr=mm.fetchall()
                       for e in wr:
                           ep=e[im]
                           rsty.append(ep)
                       global r
                       r=StringVar()
                       r.set("SELECT")
                       droplistr=OptionMenu(R8,r,*rsty)
                       droplistr.bind('<Button-1>',clear3)
                       droplistr.config(width=20)
                       droplistr.place(x=750,y=210)
                              
                       
                def clear1(x):
                    clas.set("SELECT")
                    tot.set(0)
                    atot.set(0)
                    mo.set("select")
                    try:
                     sub.set("select")
                    except:
                        pass
                    e1.delete(0,END)
                    e2.delete(0,END)
                    l.config(text="")

                       
                def clear2(x):
                    try:
                     sub.set("select")
                    except:
                        pass
                    e1.delete(0,END)
                    e2.delete(0,END)
                    l.config(text="")

                       
                def clear3(x):       
                    try:
                     sub.set("select")
                    except:
                        pass
                    e1.delete(0,END)
                    e2.delete(0,END)
                    l.config(text="")
                    tot.set(0)
                    atot.set(0)
                              
                           
                fo=open("user.txt","r")
                myuser=fo.readline()
                mypass=fo.readline()
                fo.close()
                               
                        
                am=mysql.connector.connect(user=myuser,password=mypass,host='localhost')
                mm=am.cursor()

                global clsty
                clsty=[]
                im=0
                mm.execute("use dgclass;")
                mm.execute("Show tables;")
                wu=mm.fetchall()
                for e in wu:
                    ep=e[im]
                    clsty.append(ep)
                sk=str(clsty)

                month=['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']

                R8= Tk()
                R8.resizable(width=FALSE, height=FALSE)
                R8.geometry('1280x720')
                R8.title('MAKE ATTENDENCE ENTRY')
                R8.configure(background=g)

                Image_open=Image.open("attentry.jpg")
                image=ImageTk.PhotoImage(Image_open)
                logo=Label(R8,image=image,bg=gg)
                logo.place(x=0,y=0,bordermode="outside")

                e1=Entry(R8,width=5,font=("bold",20),highlightthickness=2)
                e1.place(x=700,y=320)

                e2=Entry(R8,width=5,font=("bold",20),highlightthickness=2)
                e2.place(x=1120,y=320)

                clas=StringVar()
                clas.set("SELECT")
                droplist=OptionMenu(R8,clas, *clsty,command=c)
                droplist.config(width=20)
                droplist.bind('<Button-1>',clear1)
                droplist.place(x=370,y=210)

                global mo
                mo=StringVar()
                mo.set("SELECT")
                droplist=OptionMenu(R8,mo, *month)
                droplist.config(width=10)
                droplist.place(x=1110,y=210)

                tot=IntVar()
                te=Label(R8,textvariable=tot,width=4)
                te.place(x=90,y=674)

                atot=IntVar()
                ae=Label(R8,textvariable=atot,width=4)
                ae.place(x=210,y=674)

                button1=Button(R8,text="ADD",width=30,height=4,bg=gg,fg="white",font="5",relief=RAISED,overrelief=RIDGE,command=add_att)
                button1.place(x=900,y=400)
                def hou():
                        R8.destroy()
                        afterlogin()
                back=Button(R8,text="HOME",bg=gg,fg=gw,command=hou)
                back.place(x=1200,y=30)

                l=Label(R8,font="10",bg=g)
                l.place(x=300,y=400)
                R8.mainloop()


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\        

def new_student():
                R2.destroy()
                def add():
                    try:
                        gr=e1.get()
                        fname=e2.get()
                        lname=e3.get()
                        cm.execute("""insert into """+(clas.get())+"""(grno,fname,lname) values(%s,%s,%s)""",(gr,fname,lname))
                        cl.commit()
                    except:
                        l.config(text="something went wrong",fg="red")
                    else:
                        
                        l.config(text="Added",fg="spring green2")
                    
                    

                def roll(rn):

                    cm.execute("""SELECT `auto_increment` FROM INFORMATION_SCHEMA.TABLES
                                   WHERE table_name = '"""+rn+"""';""")
                    wu=cm.fetchall()
                    for row in wu:
                        w=int(row[0])
                        ro=w
                        r.set(ro)
                    
                def clear1(x):
                    e1.delete(0, END)
                    e2.delete(0,END)
                    e3.delete(0,END)
                    r.set(0)
                    clas.set("select")
                    l.config(text="",width=20,bg=g)

                def clear2(x):
                    clas.set("select")
                    r.set(0)
                    l.config(text="",width=20,bg=g)
                def fgu(x):
                    add()
                    
                def grup():
                                def up():
                                    try:
                                        cl=mysql.connector.connect(host='localhost',user=myuser,password=mypass,database="dgclass")
                                        cm=cl.cursor()
                                        cm.execute("update "+str(cclas.get())+" set grno="+str(eg.get())+" where rollno="+str(er.get()))
                                        cl.commit()
                                    except:
                                        lq.config(text="something went wrong",fg="red")
                                    else:
                                        lq.config(text="updated Gr.no",fg="green")
                                        
                                
                                gn="#0a2745"
                                te=Toplevel(R6,bg=gn)
                                te.geometry("500x200")
                                te.title("UPDATE")
                                te.resizable(height=FALSE,width=FALSE)
                                cclaassy=[]
                                im=0
                                cm.execute("show tables")
                                wu=cm.fetchall()
                                for e in wu:
                                    ep=e[im]
                                    cclaassy.append(ep)
                                sk=str(cclaassy)
                                cclas=StringVar()
                                droplist=OptionMenu(te,cclas, *cclaassy)
                                droplist.config(width=5)
                                droplist.place(x=200,y=5)
                                lp=Label(te,text="Class",bg=gn,fg=gw)
                                lp.place(x=15,y=5)
                                lr=Label(te,text="Rollno",bg=gn,fg=gw)
                                lr.place(x=15,y=70)
                                lu=Label(te,text="New Gr.no",bg=gn,fg=gw)
                                lu.place(x=15,y=120)
                                er=Entry(te)
                                er.place(x=200,y=70)
                                eg=Entry(te)
                                eg.place(x=200,y=120)
                                b=Button(te,text="Update",width=10,command=up)
                                b.place(x=200,y=150)
                                lq=Label(te,bg=gn)
                                lq.place(x=200,y=180)
                                R6.mainloop()                    

                def nameup():
                                def up():
                                    try:
                                    
                                        cl=mysql.connector.connect(host='localhost',user=myuser,password=mypass,database="dgclass")
                                        cm=cl.cursor()
                                        cm.execute("update "+str(cclas.get())+" set fname='"+str(eg.get())+"' where rollno="+str(er.get()))
                                        cm.execute("update "+str(cclas.get())+" set lname='"+str(eeg.get())+"' where rollno="+str(er.get()))
                                        cl.commit()
                                    except:
                                        lq.config(text="something went wrong",fg="red")
                                    else:
                                    
                                        lq.config(text="updated Gr.no",fg="green")
                                        
                                
                                gn="#0a2745"
                                te=Toplevel(R6,bg=gn)
                                te.geometry("500x250")
                                te.title("UPDATE")
                                te.resizable(height=FALSE,width=FALSE)
                                cclaassy=[]
                                im=0
                                cm.execute("show tables")
                                wu=cm.fetchall()
                                for e in wu:
                                    ep=e[im]
                                    cclaassy.append(ep)
                                sk=str(cclaassy)
                                cclas=StringVar()
                                droplist=OptionMenu(te,cclas, *cclaassy)
                                droplist.config(width=5)
                                droplist.place(x=200,y=5)
                                lp=Label(te,text="Class",bg=gn,fg=gw)
                                lp.place(x=15,y=5)
                                lr=Label(te,text="Rollno",bg=gn,fg=gw)
                                lr.place(x=15,y=70)
                                lu=Label(te,text="New firstname",bg=gn,fg=gw)
                                lu.place(x=15,y=120)
                                leu=Label(te,text="New lastname",bg=gn,fg=gw)
                                leu.place(x=15,y=170)
                                er=Entry(te)
                                er.place(x=200,y=70)
                                eg=Entry(te)
                                eg.place(x=200,y=120)
                                eeg=Entry(te)
                                eeg.place(x=200,y=170)
                                b=Button(te,text="Update",width=10,command=up)
                                b.place(x=200,y=200)
                                lq=Label(te,bg=gn)
                                lq.place(x=200,y=230)
                                R6.mainloop()                        


                    
                R6= Tk()
                R6.resizable(width=FALSE, height=FALSE)
                R6.geometry('1280x720')
                R6.title('Login')
                R6.configure(background=g)

                menubar = Menu(R6)
                ae= Menu(menubar)
                ae.add_command(label="Gr.no",command=grup)
                ae.add_command(label="Name",command=nameup)
                menubar.add_cascade(label="Update", menu=ae)
                R6.config(menu=menubar)

                Image_open=Image.open("entry.jpg")
                image=ImageTk.PhotoImage(Image_open)
                logo=Label(R6,image=image,bg=gg)
                logo.place(x=0,y=0,bordermode="outside")

                fo=open("user.txt","r")
                myuser=fo.readline()
                mypass=fo.readline()
                fo.close()
                                                

                cl=mysql.connector.connect(host='localhost',user=myuser,password=mypass,database="dgclass")
                cm=cl.cursor()

                global claassy,im
                claassy=[]
                im=0
                cm.execute("show tables")
                wu=cm.fetchall()
                for e in wu:
                    ep=e[im]
                    claassy.append(ep)
                sk=str(claassy)


                e1=Entry(R6,width=20,font=("bold",15),highlightthickness=2)
                e1.bind('<Button-1>',clear1)
                e1.place(x=940,y=206)
                e2=Entry(R6,width=15,font=("bold",15),highlightthickness=2)
                e2.place(x=988,y=280)
                e3=Entry(R6,width=15,font=("bold",15),highlightthickness=2)
                e3.place(x=988,y=350)

                clas=StringVar()
                droplist=OptionMenu(R6,clas, *claassy,command=roll)
                droplist.config(width=20)
                droplist.bind('<Button-1>',clear2)
                droplist.place(x=940,y=415)

                r=IntVar()
                e4=Label(R6,width=20,font=("bold",15),textvariable=r,highlightthickness=2)
                e4.place(x=940,y=490)

                b1=Button(R6,text="ADD",width=25,height=2,bg=gg,fg="white",font="5",relief=RAISED,overrelief=RIDGE,command=add)
                b1.place(x=890,y=600)
                def hoii():
                        R6.destroy()
                        afterlogin()

                back=Button(R6,text="HOME",bg=gg,fg=gw,command=hoii)
                back.place(x=1200,y=30)
                l=Label(R6,font="10",bg=g)
                l.place(x=940,y=660)
                ls=Label(R6,font="10",bg=g)
                ls.place(x=100,y=400)
                R6.bind('<Return>',fgu)
                R6.mainloop()



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def std_re():
        global R3
        R2.destroy()
        
        def sr():
                
                listbox1.delete(0,END)
                listbox2.delete(0,END)
                listbox3.delete(0,END)
                listbox4.delete(0,END)
                listbox5.delete(0,END)
                listbox6.delete(0,END)
                listbox7.delete(0,END)
                listbox9.delete(0,END)
                
                cm.execute("use "+str(cd.get()))
                
                

                cm.execute("use dgclass")
                cm.execute("select rollno from "+str(cd.get()))
                oo=cm.fetchall()
                for item in oo:
                   listbox2.insert(END,item)

                cm.execute("use "+str(cd.get()))
                
                cm.execute("use dgclass")
                cm.execute("select grno from "+str(cd.get()))
                oo=cm.fetchall()
                for item in oo:
                  listbox1.insert(END,item)

                cm.execute("use dgclass")
                cm.execute("select fname from "+str(cd.get()))
                oo=cm.fetchall()
                for item in oo:
                 listbox3.insert(END,item)

                cm.execute("use dgclass")
                cm.execute("select lname from "+str(cd.get()))
                oo=cm.fetchall()
                for item in oo:
                 listbox9.insert(END,item)
                 
                qr=sd.get()
                rr='All'
                if(qr==rr):
                        cm.execute("use "+str(cd.get()))
                        cm.execute("select total from "+md.get())
                        oo=cm.fetchall()
                        for item in oo:
                         listbox4.insert(END,item)


                        cm.execute("use "+str(cd.get()))
                        cm.execute("select tot_atten from "+md.get()) 
                        oo=cm.fetchall()
                        for item in oo:
                         listbox5.insert(END,item)

                        cm.execute("use "+str(cd.get()))
                        cm.execute("select per_tot from "+md.get())
                        oo=cm.fetchall()
                        for item in oo:
                         listbox6.insert(END,item)

                        cm.execute("use "+str(cd.get()))
                        cm.execute("select status_tot from "+md.get())
                        oo=cm.fetchall()
                        for item in oo:
                         listbox7.insert(END,item)
                        
                else:
                        
                        cm.execute("use "+str(cd.get()))
                        cm.execute("select "+sd.get()+" from "+md.get() )
                        oo=cm.fetchall()
                        for item in oo:
                         listbox4.insert(END,item)


                        cm.execute("use "+str(cd.get()))
                        cm.execute("select atten_"+sd.get()+" from "+md.get() )
                        oo=cm.fetchall()
                        for item in oo:
                         listbox5.insert(END,item)

                        cm.execute("use "+str(cd.get()))
                        cm.execute("select per_"+sd.get()+" from "+md.get() )
                        oo=cm.fetchall()
                        for item in oo:
                         listbox6.insert(END,item)

                        cm.execute("use "+str(cd.get()))
                        cm.execute("select status_"+sd.get()+" from "+md.get() )
                        oo=cm.fetchall()
                        for item in oo:
                         listbox7.insert(END,item)

                
        def s(sub):
            sy=[]
            im=0
            cm.execute("use "+str(sub))
            cm.execute("select subjects from subject")
            wu=cm.fetchall()
            for e in wu:
             ep=e[im]
             sy.append(ep)
            sy.append("All")
             
            global sd 
            sd=StringVar()
            droplist1=OptionMenu(R3,sd, *sy)
            droplist1.config(width=5)
            droplist1.place(x=700,y=30)
            my=[]
            im=0
            cm.execute("use "+str(sub))
            cm.execute("show tables ")
            wu=cm.fetchall()
            for e in wu:
             ep=e[im]
             my.append(ep)
            del my[-1]
             

            global md
            md=StringVar()
            droplist2=OptionMenu(R3,md,*my)
            droplist2.config(width=5)
            droplist2.place(x=900,y=30)


                
        gg='#0a2845'#secondary color
        g="blue"#color
        gw="white"
        R3=Tk()
        R3.title("")
        R3.geometry("1280x720")
        R3.config(bg=gg)
        R3.resizable(width=FALSE, height=FALSE)

        Image_open=Image.open("bgst.jpg")
        image=ImageTk.PhotoImage(Image_open)
        logo=Label(R3,image=image,bg=gg)
        logo.place(x=0,y=0,bordermode="outside")



        def OnVsb(*args):
                listbox1.yview(*args)
                listbox2.yview(*args)
                listbox3.yview(*args)
                listbox4.yview(*args)
                listbox5.yview(*args)
                listbox6.yview(*args)
                listbox7.yview(*args)
                listbox8.yview(*args)
                


        def OnMouseWheel(event):
            
                listbox1.yview("scroll", (event.delta-100),"units")
                listbox2.yview("scroll",(event.delta-100),"units")
                listbox3.yview("scroll",(event.delta-100),"units")
                listbox4.yview("scroll",(event.delta-100),"units")
                listbox5.yview("scroll",(event.delta-100),"units")
                listbox6.yview("scroll",(event.delta-100),"units")
                listbox7.yview("scroll",(event.delta-100),"units")
                listbox8.yview("scroll",(event.delta-100),"units")
                return "break"
            



        listbox8 = Listbox(R3, width=200,borderwidth=0, highlightthickness=0,selectbackground=gg,height=38,bg=gg,fg=gw,font="10")
        listbox8.bind("<MouseWheel>",OnMouseWheel)
        listbox8.place(x=25,y=125)

        listbox1 = Listbox(R3, width=7,borderwidth=0, highlightthickness=0,selectbackground=gg,height=30,bg=gg,fg=gw,font="10")
        listbox1.bind("<MouseWheel>",OnMouseWheel)
        listbox1.place(x=17,y=125)




        listbox2 = Listbox(R3, width=7, height=30,highlightthickness=0,bg=gg,borderwidth=0,selectbackground=gg,fg=gw,font="10")
        listbox2.bind("<MouseWheel>",OnMouseWheel)
        listbox2.place(x=145,y=125)

        listbox3=Listbox(R3, width=20,borderwidth=0,height=30,bg=gg,selectbackground=gg,fg=gw,font="10",highlightthickness=0)
        listbox3.bind("<MouseWheel>",OnMouseWheel)
        listbox3.place(x=270,y=125)

        listbox9 = Listbox(R3, width=20,borderwidth=0, highlightthickness=0,selectbackground=gg,height=30,bg=gg,fg=gw,font="10")
        listbox9.bind("<MouseWheel>",OnMouseWheel)
        listbox9.place(x=350,y=125)

        listbox4=Listbox(R3, width=20,borderwidth=0,height=30,bg=gg,selectbackground=gg,fg=gw,font="10",highlightthickness=0)
        listbox4.bind("<MouseWheel>",OnMouseWheel)
        listbox4.place(x=520,y=125)

        listbox5=Listbox(R3, width=5,borderwidth=0,height=30,bg=gg,selectbackground=gg,fg=gw,font="10",highlightthickness=0)
        listbox5.bind("<MouseWheel>",OnMouseWheel)
        listbox5.place(x=750,y=125)

        listbox6=Listbox(R3, width=5,borderwidth=0,height=30,bg=gg,selectbackground=gg,fg=gw,font="10",highlightthickness=0)
        listbox6.bind("<MouseWheel>",OnMouseWheel)
        listbox6.place(x=960,y=125)



        listbox7=Listbox(R3, width=15,borderwidth=0,height=30,bg=gg,selectbackground=gg,fg=gw,font="10",highlightthickness=0)
        listbox7.bind("<MouseWheel>",OnMouseWheel)
        listbox7.place(x=1150,y=125)


        yscroll=Scrollbar(R3,command=OnVsb,orient=VERTICAL,width=10)
        yscroll.place(relx=1,x=-10,y=80,height=635)


        a=mysql.connector.connect(user='root',password='1230')
        mm=a.cursor()

            
        fo=open("user.txt","r")
        myuser=fo.readline()
        mypass=fo.readline()
        fo.close()
        cl=mysql.connector.connect(host='localhost',user=myuser,password=mypass)
        cm=cl.cursor()

        cy=[]
        im=0
        cm.execute("use dgclass")
        cm.execute("show tables")
        wu=cm.fetchall()
        for e in wu:
            ep=e[im]
            cy.append(ep)
        sk=str(cy)




        cy=[]
        im=0
        cm.execute("show tables")
        wu=cm.fetchall()
        for e in wu:
            ep=e[im]
            cy.append(ep)
        sk=str(cy)
        global cd
        cd=StringVar()
        droplist=OptionMenu(R3,cd, *cy,command=s)
        droplist.config(width=5)
        droplist.place(x=490,y=30)



        b2=Button(R3,text="SEARCH",width=10,bg=g,fg="white",font="5",relief=RAISED,overrelief=RIDGE,command=sr)
        b2.place(x=1050,y=30)
        def ho():
                R3.destroy()
                afterlogin()

        back=Button(R3,text="HOME",bg=gg,fg=gw,command=ho)
        back.place(x=1200,y=30)

        R3.mainloop()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def login():
        #mysql user and password
        fo=open("user.txt","r")
       
        myuser=fo.readline()
        mypass=fo.readline()
        
        

        global a,m
        a=mysql.connector.connect(host='localhost',user=myuser,password=mypass)
        m=a.cursor()
        def final():
            
            if (e1.get(), e2.get()) in password:
                 R1.destroy()
                 afterlogin()
            else:
                L3.config(text="Invalid User or Password",fg="red")
        def login(x):
            final()

        
        def about():
                t=Toplevel(R1,cursor="hand2")
                t.geometry("661x571")
                t.title("about")
                t.resizable(height=FALSE,width=FALSE)
                t.group(R1)
                Imageo=Image.open("ab.jpg")
                image=ImageTk.PhotoImage(Imageo)
                logo=Label(t,image=image)
                logo.place(x=0,y=0,bordermode="outside")
                R1.mainloop()

                                                    
        def clear(x):
                e1.delete(0,END)
                e2.delete(0,END)
                L3.config(text="")
        def edit():
                        def refresh():
                                R1.destroy()
                                os.startfile("DG attendence management.py")
                        def ed():
                          
                                h=str(er.get())
                                j=str(e.get())
                                
                                if(h==passy):
                                   m.execute("""update log
                                                set user='"""+str(j)+"""'""")
                                   a.commit()
                                   l.config(text="Done!",fg="green")
                                   refresh()
                          
                                else:
                                  l.config(text="something went wrong",fg="red")       
                                            
               
                        te=Toplevel(R1,bg=gg)
                        te.geometry("500x120")
                        te.title("EDIT")
                        te.resizable(height=FALSE,width=FALSE)
                        lp=Label(te,text="New Name",bg=gg,fg=gw)
                        lp.place(x=15,y=5)
                        lr=Label(te,text="Current_Password",bg=gg,fg=gw)
                        lr.place(x=15,y=30)
                        e=Entry(te)
                        e.place(x=200,y=5)
                        er=Entry(te)
                        er.place(x=200,y=30)
                        b=Button(te,text="SET",width=10,command=ed)
                        b.place(x=200,y=55)
                        l=Label(te,bg=gg)
                        l.place(x=200,y=100)
                        R1.mainloop()
                        
            
        def reset():
                def r():
                        m.execute("""select password from log""")
                        f=m.fetchall()
                        for row in f:
                            ps=(row[0])
                        m.execute("""select backuppin from log""")
                        f=m.fetchall()
                        for row in f:
                            pb=(row[0])
                        reset=[]
                        re=[]
                        reset.append(ps)
                        re.append(pb)
                        h=str(e.get())
                        if(h==ps or pb):
                          m.execute("""update log
                                      set password='"""+str(er.get())+"""'""")
                          a.commit()
                          l.config(text="Done!",fg="green")
                          
                          refresh()
                          
                        else:
                                
                         l.config(text="wrong backupin or password",fg="red")
                        
                def refresh():
                        R1.destroy()
                        os.startfile("login ui.py")

                te=Toplevel(R1,bg=gg)
                te.geometry("500x120")
                te.title("RESET")
                te.resizable(height=FALSE,width=FALSE)
                lp=Label(te,text="backuppin or old password",bg=gg,fg=gw)
                lp.place(x=15,y=5)
                lr=Label(te,text="New Password",bg=gg,fg=gw)
                lr.place(x=15,y=30)
                e=Entry(te)
                e.place(x=200,y=5)
                er=Entry(te)
                er.place(x=200,y=30)
                b=Button(te,text="RESET",width=10,command=r)
                b.place(x=200,y=55)
                l=Label(te,bg=gg)
                l.place(x=200,y=100)
                R1.mainloop()                      





        m.execute("use login")
        m.execute("select * from log")
        p=m.fetchall()
        password=[]
        global ussy,passy
        for row in p:
             ussy=row[0]
             passy=row[1]
             password.append((ussy,passy))
             
        global R1
        R1= Tk()
        R1.resizable(width=FALSE, height=FALSE)
        R1.geometry('1280x720')
        R1.title('Login')
        R1.configure(background=g)
        
        
        menubar = Menu(R1)
        filemenu = Menu(menubar,tearoff=0)
        filemenu.add_command(label="view report",command=report)
        menubar.add_cascade(label="Student login", menu=filemenu)

        ae= Menu(menubar)
        ae.add_command(label="Edit username",command=edit)
        ae.add_command(label="Reset password",command=reset)
        ae.add_command(label="About",command=about)
        menubar.add_cascade(label="Help", menu=ae)
        
        
       
        
        R1.config(menu=menubar)
        
        Image_open=Image.open("yy.jpg")
        image=ImageTk.PhotoImage(Image_open)
        logo=Label(R1,image=image,bg=g)
        logo.place(x=0,y=0,bordermode="outside")

        now = datetime.datetime.now()
        y=str(now.day)+"/"+str(now.strftime('%B'))+"/"+str(now.year)
        Ltime=Label(R1,text=y,bg=g,fg=gw)
        Ltime.place(x=1180,y=0)

        L1=Label(R1,text="Username",width=10,bg=gg,fg=gw,font=("bold", 20))
        L1.place(x=680,y=380)
        L2=Label(R1,text="Password",width=10,bg=gg,fg=gw,font=("bold", 20))
        L2.place(x=680,y=450)
        L3=Label(R1,text="",width=20,fg="white",font="5",bg=gg)
        L3.place(x=880,y=580)
        default=StringVar()
        e1=Entry(R1,width=20,font=("bold",15),textvariable=default,highlightthickness=2,relief=SUNKEN)
        e1.bind('<Button-1>',clear)
        e1.place(x=850,y=385)
        e2=Entry(R1,width=20,font=("bold",15),highlightthickness=2,show="*",relief=SUNKEN)
        e2.place(x=850,y=455)
        b1=Button(R1,text="Login",width=25,height=2,bg=g,fg="white",font="5",relief=RAISED,overrelief=RIDGE,command=final)
        b1.place(x=850,y=510)
        R1.bind('<Return>',login)
        R1.mainloop()





#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def signup():
        
        def login_database():
                try:
                          user=e1.get()
                          password=e2.get()
                          backuppin=e3.get()
                          mysqluser=e4.get()
                          mysqlpassword=e5.get()
                          u=str(mysqluser)
                          p=str(mysqlpassword)
                          userf=open("user.txt","w")
                          userf.write(u+"\n"+p)
                          userf.close()
                          
                          aa=mysql.connector.connect(host='localhost',user=mysqluser,password=mysqlpassword)
                          mm=aa.cursor()
                          mm.execute("CREATE DATABASE login")
                          mm.execute("CREATE DATABASE dgclass")
                          aa.commit()
                          mm.execute("""use login""")
                          mm.execute("""CREATE TABLE log (
                                                   user varchar(20) not null,
                                                   password VARCHAR(70) not null,
                                                   backuppin varchar(20) not null
                                                   )""")
                
                          mm.execute("""INSERT  INTO log VALUES(%s,%s,%s)""",(user,password,backuppin))
                          aa.commit()
                          fr=open("start.txt","w")
                          fr.write('111')
                          fr.close()
                          R.destroy()
                except:
                        l.config("something went wrong",fg="red")
                else:
                        login()
                  
                            

                      
             
                 
             

        gg='#134e86'#secondary color
        g="blue"#color

        gw="white"

        

        R=Tk()
        R.resizable(width=FALSE, height=FALSE)
        R.geometry('1280x720')
        R.title('Sign up')
        R.configure(background=g)

        Image_open=Image.open("si.jpg")
        image=ImageTk.PhotoImage(Image_open)
        logo=Label(R,image=image,bg=gg)
        logo.place(x=0,y=0,bordermode="outside")

        e1=Entry(R,width=20,font=("bold",15),highlightthickness=2,bg=gw,relief=SUNKEN)
        e1.place(x=920,y=165)
        e2=Entry(R,width=20,font=("bold",15),show="*",highlightthickness=2,bg=gw,relief=SUNKEN)
        e2.place(x=920,y=238)
        e3=Entry(R,width=20,font=("bold",15),highlightthickness=2,bg=gw,relief=SUNKEN)
        e3.place(x=920,y=308)
        default=StringVar()
        e4=Entry(R,width=15,font=("bold",15),textvariable=default,highlightthickness=2,bg=gw,relief=SUNKEN,fg="brown")
        default.set("root")
        e4.place(x=980,y=482)
        e5=Entry(R,width=15,font=("bold",15),highlightthickness=2,bg=gw,relief=SUNKEN)
        e5.place(x=980,y=548)
        b1=Button(R,text="Sign Up",width=25,height=2,bg=g,fg="white",font="5",relief=RAISED,overrelief=RIDGE,command=login_database)
        b1.place(x=858,y=600)
        l=Label(R,font="10",bg=gg)
        l.place(x=928,y=660)
        R.bind('<Return>')
        R.mainloop()


try:

    fr=open("start.txt","r")
    sup=fr.read()
    
    if(int(sup)==111):
        login()
           
    else:
        signup()
except:
    signup()
    

#while(1):
#    fr=open("start.txt",'r')
#    sup=fr.read()

#    if(int(sup)==111):
 #       login()

  #  else:
   #      signup()
