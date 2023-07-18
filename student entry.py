import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
root.geometry('500x600')
root.title('WX')

student_data = [1 , 'John' , 'jonestudent@gmail.com' , 'python'],
[2, 'qwwi' , 'dsncdn', ' ufdsudue, (re)'],
[3, 'rezfds','erf','tre'],
[4,'frds','rfe','gbfd'],
[5,'vfecx','fevx','frds']
[5,'vfcdxsqw','vfcd','fvcvf']


def load_student_data():
    for item in record_table.get_children():
        record_table.delete(item)
        for r in range(student_data):
            record_table.insert(parent = '', index ='end',text = '' ,
                                iid=r, values=student_data[r])

def put_student_in_entry(index):
    student_id.delete(0, tk.END)
    student_name.delete(0, tk.END)
    student_email.delete(0, tk.END)
    student_COURCES.delete(0, tk.END)

    stud_Id = student_data[index][0]
    stud_name = student_data[index][1]
    stud_email = student_data[index][2]
    stud_COURCES = student_data[index][3]

    student_id.insert(0, stud_Id )
    student_name.insert(0, stud_name)
    student_email.insert(0, stud_email)
    student_COURCES.insert(0, stud_COURCES)

def clear_student_data():
    student_id.delete(0, tk.END)
    student_name.delete(0, tk.END)
    student_email.delete(0, tk.END)
    student_COURCES.delete(0, tk.END)
    load_student_data()

def add_student_data(stud_ID, stud_name ,stud_email, stud_cources):
    student_data([stud_ID , stud_name , stud_email ,stud_cources])
    load_student_data()
    clear_student_data()

def update_student_data(stud_ID, stud_name ,stud_email, stud_cources,index):
    student_data[index] = [stud_ID, stud_name ,stud_email, stud_cources]
    load_student_data()
    clear_student_data()

def delete_student_data(index):
    del student_data[index]
    load_student_data()
    clear_student_data()

def find_student_by_id(stud_id):

    if stud_id != '':
        student_data_index = []

        for data in student_data:
            if str(stud_id) in str (data[0]):
                student_data_index.append(student_data.index(data))
        for item in record_table.get_children():
            record_table.delete(item)

        for r in student_data_index:
            record_table.insert(parenta = '', index ='end',text = '' , iid=r, values=student_data[r])
    else:
        load_student_data()


head_frame = tk.Frame(root)

heading_lb = tk.Label(head_frame,text='Student Registre System' , bg ='Red')
heading_lb.pack(fill =tk.X , pady=5)

student_id_lb = tk.Label(head_frame , text = 'student Id')
student_id_lb.place(x=0, y=50)

student_id= tk.Entry(head_frame)
student_id.place(x=110 , y=50 ,width=180)

student_name_lb = tk.Label(head_frame, text = 'student name')
student_name_lb.place(x=0, y=100)


student_name = tk.Entry(head_frame)
student_name.place(x= 110 , y =100, width=180 )

student_email_lb = tk.Label(head_frame, text = 'student EMAIL')
student_email_lb.place(x=0, y=150)

student_email = tk.Entry(head_frame)
student_email.place(x=110 , y =150, width=180)

student_cources_lb = tk.Label(head_frame, text = 'student cources')
student_cources_lb.place(x=0, y=200)

student_COURCES = tk.Entry(head_frame)
student_COURCES.place(x=110 , y =200, width=180)

register_btn = tk.Button(head_frame, text='register', command=lambda: add_student_data(student_id.get(),
student_name.get(),
student_email.get(),
student_COURCES.get()))
register_btn.place(x= 0 , y=250)

update_btn = tk.Button(head_frame, text='Update',
command= lambda : update_student_data(student_id.get(),
student_name.get(),

student_email.get(),
student_COURCES.get(),
index=int(record_table.selection()[0])))


update_btn.place(x= 85 , y=250)

delete_btn = tk.Button(head_frame, text='delete' ,
command= lambda :delete_student_data(record_table.selection()[0]))
delete_btn.place(x=163,y=250)

clear_btn = tk.Button(head_frame , text ='clear',
command= lambda : clear_student_data())
clear_btn.place(x=235,y=250)




head_frame.pack(pady= 10)
head_frame.pack_propagate(False)
head_frame.configure(width= 400, height = 300)

search_bar_frame = tk.Frame(root)

search_lb = tk.Label(search_bar_frame, text='search Student ',)
search_lb.pack(anchor=tk.W)

search_entry = tk.Entry(search_bar_frame)
search_entry.pack(anchor=tk.W)
search_entry.bind('<KeyRelease>', lambda e: find_student_by_id(search_entry.get()) )

search_bar_frame.pack(pady = 0)
search_bar_frame.pack_propagate(False)
search_bar_frame.configure(width=400 , height=50)

record_frame = tk.Frame(root)

record_lb = tk.Label(record_frame, text='select REcord for delete or Update',bg = 'Red')

record_lb.pack(fill=tk.X)

record_table = ttk.Treeview(record_frame)
record_table.pack(fill=tk.X , pady =5 )

record_table.bind('<<TreeviewSelect>>' , lambda e: put_student_in_entry(
int(record_table.selection()[0])))

record_table['column'] = ['Id','Named','email','cources' ]

record_table.column('#0', anchor=tk.W, width=0, stretch= tk.NO)

record_table.column('Id', anchor=tk.W, width= 50)
record_table.column('Named', anchor=tk.W, width= 100)
record_table.column('email', anchor=tk.W, width= 120)
record_table.column('cources', anchor=tk.W, width= 160)

record_table.heading('Id',text = 'Id', anchor=tk.W )
record_table.heading('Named',text = 'name', anchor=tk.W )
record_table.heading('email',text = 'email', anchor=tk.W )
record_table.heading('cources',text = 'cources', anchor=tk.W )

record_frame.pack(pady= 10)
record_frame.pack_propagate(False)
record_frame.configure(width=400 , height=200)
load_student_data()


root.mainloop()