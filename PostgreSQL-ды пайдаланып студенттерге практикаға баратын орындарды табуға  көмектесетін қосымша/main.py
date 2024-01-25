import tkinter as tk
from tkinter import PhotoImage
import random
def first_page():
    def final_page():
        lang = []
               
        def lock2():
            pyt.config(background='white', command=lock1)
            lang.remove('Python')
            print(lang)

        def lock1():
            pyt.config(background='green', command=lock2)
            lang.append('Python')
            print(lang)

        def lock4():
            java.config(background='white', command=lock3)
            lang.remove('Java')
            print(lang)

        def lock3():
            java.config(background='green', command=lock4)
            lang.append('Java')
            print(lang)

        def lock5():
            web.config(background='green', command=lock6)
            lang.append('Web')
            print(lang)

        def lock6():
            web.config(background='white', command=lock5)
            lang.remove('Web')
            print(lang)

        def lock7():
            db.config(background='green', command=lock8)
            lang.append('Database')
            print(lang)

        def lock8():
            db.config(background='white', command=lock7)
            lang.remove('Database')
            print(lang)

        def lock9():
            game.config(background='green', command=lock10)
            lang.append('Gamedev')
            print(lang)

        def lock10():
            game.config(background='white', command=lock9)
            lang.remove('Gamedev')
            print(lang)

        def lock11():
            app.config(background='green', command=lock12)
            lang.append('App')
            print(lang)

        def lock12():
            app.config(background='white', command=lock11)
            lang.remove('App')
            print(lang)

        def pro():
            pyt.destroy()
            web.destroy()
            java.destroy()
            game.destroy()
            db.destroy()
            but.destroy()
            app.destroy()
            cont.destroy()
            if lang == ['Web', 'Java'] or lang == ['Java', 'Web']:
                arr = tk.Label(root, text='Aituc group ★★★★★', background='white', font=('monserat', 16))
                arr.place(x=10, y=120)
                zp=tk.Button(root,text='')
            elif lang == ['Java', 'Database'] or lang == ['Database', 'Java']:
                arr = tk.Label(root, text='Aitu group ★★★★★', background='white', font=('monserat', 16))
                arr.place(x=10, y=120)
            elif lang == ['Python', 'GameDev']:
                arr = tk.Label(root, text='Aituc Game ★★★★★', background='white', font=('monserat', 16))
                arr.place(x=10, y=120)

        def show():
            but.config(text='Фильтр↑', command=hide, activebackground='yellow')
            global pyt
            pyt = tk.Button(root, text='Python', command=lock1)
            pyt.place(x=40, y=120)
            global java
            java = tk.Button(root, text='Java', command=lock3)
            java.place(x=90, y=120)
            global web
            web = tk.Button(root, text='Web+', command=lock5)
            web.place(x=124, y=120)
            global db
            db = tk.Button(root, text='Database', command=lock7)
            db.place(x=166, y=120)
            global game
            game = tk.Button(root, text='Gamedev', command=lock9)
            game.place(x=226, y=120)
            global app
            app = tk.Button(root, text='App dev', command=lock11)
            app.place(x=286, y=120)
            global cont
            cont = tk.Button(root, text='Жалғастыру', command=pro)
            cont.place(x=156, y=160)

        def hide():
            but.config(text='Фильтр↓', command=show, activebackground='yellow')
            pyt.destroy()
            web.destroy()
            java.destroy()
            game.destroy()
            db.destroy()
            app.destroy()
            cont.destroy()

        root.config(background='white')
        root.geometry('400x600')
        main = tk.Label(root, text='Серіктестік табу', background='white', foreground='Black', font=('monserat', 26))
        main.place(x=72, y=30)
        but = tk.Button(root, text='Фильтр↓', bd=0, background='white', font=('monserat', 14), command=show)
        but.place(x=160, y=80)
        def hide():
            but.config(text='Фильтр↓', command=show, activebackground='yellow')
            pyt.destroy()
            web.destroy()
            java.destroy()
            game.destroy()
            db.destroy()

        root.config(background='white')
        root.geometry('400x600')
        main = tk.Label(root, text='Серіктестік табу', background='white', foreground='Black', font=('monserat', 26))
        main.place(x=72, y=30)
        but = tk.Button(root, text='Фильтр↓', bd=0, background='white', font=('monserat', 14), command=show)
        but.place(x=160, y=80)
    def sort_page():
        lar.destroy()
        lost = []
        for i in range(6):
            i = random.randint(0, 9)
            a = str(i)
            lost.append(a)
            print(lost)

        def check_num():
            long = []
            b = one.get()
            c = two.get()
            d = three.get()
            e = four.get()
            f = five.get()
            g = six.get()
            long.append(b)
            long.append(c)
            long.append(d)
            long.append(e)
            long.append(f)
            long.append(g)
            print(long)
            if long == lost:
                left.destroy()
                left1.destroy()
                left2.destroy()
                left3.destroy()
                left4.destroy()
                left5.destroy()
                left6.destroy()
                left7.destroy()
                one.destroy()
                two.destroy()
                three.destroy()
                four.destroy()
                five.destroy()
                six.destroy()
                seven.destroy()
                final_page()
            else:
                pass
        left6 = tk.Label(root, width=1, height=10, background='white')
        left6.grid(row=1, column=1)
        left = tk.Label(root, width=8, height=10, background='white')
        left.grid(row=1, column=2)
        left1 = tk.Label(root, width=8, height=10, background='white')
        left1.grid(row=1, column=3)
        left2 = tk.Label(root, width=8, height=10, background='white')
        left2.grid(row=1, column=4)
        left3 = tk.Label(root, width=8, height=10, background='white')
        left3.grid(row=1, column=5)
        left4 = tk.Label(root, width=8, height=10, background='white')
        left4.grid(row=1, column=6)
        left5 = tk.Label(root, width=8, height=10, background='white')
        left5.grid(row=1, column=7)
        left7 = tk.Label(root, width=1, height=10, background='white')
        left7.grid(row=2, column=1)
        one = tk.Entry(root, width=2, bd=1, font=('arial', 26), background='#f5f7f9')
        one.grid(row=2, column=2)
        two = tk.Entry(root, width=2, bd=1, font=('arial', 26), background='#f5f7f9')
        two.grid(row=2, column=3)
        three = tk.Entry(root, width=2, bd=1, font=('arial', 26), background='#f5f7f9')
        three.grid(row=2, column=4)
        four = tk.Entry(root, width=2, bd=1, font=('arial', 26), background='#f5f7f9')
        four.grid(row=2, column=5)
        five = tk.Entry(root, width=2, bd=1, font=('arial', 26), background='#f5f7f9')
        five.grid(row=2, column=6)
        six = tk.Entry(root, width=2, bd=1, font=('arial', 26), background='#f5f7f9')
        six.grid(row=2, column=7)
        seven = tk.Button(root, text='Жалғастыру', font=('arial', 12), background='#75a8fc', command=check_num)
        seven.place(x=146, y=340)
    def sing_page():
        def on_entry_click(event, entry, default_text=''):
            if lan.get() == 'Аты-жөні':
                lan.delete(0, "end")
                lan.insert(0, '')
                lan.config(fg='black')

        def on_focus_out(event, entry, default_text=''):
            if lan.get() == '':
                lan.insert(0, 'Аты-жөні')
                lan.config(fg='grey')

        def on_entry_click1(event, entry, default_text=''):
            if lan1.get() == 'Email':
                lan1.delete(0, "end")
                lan1.insert(0, '')
                lan1.config(fg='black')

        def on_focus_out1(event, entry, default_text=''):
            if lan1.get() == '':
                lan1.insert(0, 'Email')
                lan1.config(fg='grey')

        def on_entry_click2(event, entry, default_text=''):
            if password_entry.get() == 'Құпиясөз':
                password_entry.delete(0, "end")
                password_entry.insert(0, '')
                password_entry.config(show='*')
                password_entry.config(fg='black')

        def on_focus_out2(event, entry, default_text=''):
            if password_entry.get() == '':
                password_entry.insert(0, 'Құпиясөз')
                password_entry.config(show='')
                password_entry.config(fg='grey')

        def on_entry_click3(event, entry, default_text=''):
            if password_entry1.get() == 'Құпиясөзді қайталаңыз':
                password_entry1.delete(0, "end")
                password_entry1.insert(0, '')
                password_entry1.config(show='*')
                password_entry1.config(fg='black')

        def on_focus_out3(event, entry, default_text=''):
            if password_entry1.get() == '':
                password_entry1.insert(0, 'Құпиясөзді қайталаңыз')
                password_entry1.config(show='')
                password_entry1.config(fg='grey')

        def check():
            def send(a, b, c):
                import psycopg2
                db_params = {
                    'host': 'localhost',
                    'database': 'Tulpar',
                    'user': 'postgres',
                    'password': 'Tulpar14',
                    'port': '5432',
                    'client_encoding': 'UTF8'
                }

                try:
                    connection = psycopg2.connect(**db_params)
                    connection.autocommit = True
                    cursor = connection.cursor()
                    create_table_query = '''
                    CREATE TABLE IF NOT EXISTS users_table (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100),
                        email VARCHAR(100),
                        password VARCHAR(100)
                    );
                    '''
                    cursor.execute(create_table_query)
                    name = a
                    email = b
                    password = c
                    insert_query = "INSERT INTO users_table (name, email, password) VALUES (%s, %s, %s);"
                    cursor.execute(insert_query, (name, email, password))
                    connection.commit()

                except (Exception, psycopg2.Error) as error:
                    print("PostgreSQL-ге қосылу кезінде қателік кетті:", error)

                finally:
                    if 'connection' in locals():
                        connection.close()
                        print("PostgreSQL-ге қосылу жабық.")
            a = lan.get()
            b = lan1.get()
            c = password_entry.get()
            d = password_entry1.get()
            if c == d and a != 'Аты-жөні' and b != 'Email':
                send(a,b,c)
                lab.destroy()
                lan.destroy()
                lan1.destroy()
                password_entry.destroy()
                password_entry1.destroy()
                btn.destroy()
                move.destroy()
                move2.destroy()
                sort_page()
            elif a == 'Аты-жөні' and b == 'Email':
                lar.config(text='Толық толтырыңыз',foreground='red')
            elif a == 'Аты-жөні':
                lar.config(text='Аты-жөніңізді толтырыңыз',foreground='red')
            elif b == 'Email':
                lar.config(text='email жазыңыз',foreground='red')
            else:
                lar.config(text='Құпиясөздер сәйкес келмейді',foreground='red')

        first.destroy()
        second.destroy()
        tir.destroy()
        lab = tk.Label(root, text="Тіркелу", foreground='black', font=('montserrat', 40),background='white')
        lab.place(x=50, y=30)

        lan = tk.Entry(root, width=60, background="white")
        lan.place(x=20, y=120, height=30)
        lan.insert(0, 'Аты-жөні')
        lan.bind('<FocusIn>', lambda event: on_entry_click(event, lan, 'Аты-жөні'))
        lan.bind('<FocusOut>', lambda event: on_focus_out(event, lan, 'Аты-жөні'))

        lan1 = tk.Entry(root, width=60, background="white")
        lan1.place(x=20, y=160, height=30)
        lan1.insert(0, 'Email')
        lan1.bind('<FocusIn>', lambda event: on_entry_click1(event, lan1, 'Email'))
        lan1.bind('<FocusOut>', lambda event: on_focus_out1(event, lan1, 'Email'))

        password_entry = tk.Entry(root, width=60, background="white", show='')
        password_entry.place(x=20, y=200, height=30)
        password_entry.insert(0, 'Құпиясөз')
        password_entry.bind('<FocusIn>', lambda event: on_entry_click2(event, password_entry, 'Пароль'))
        password_entry.bind('<FocusOut>', lambda event: on_focus_out2(event, password_entry, 'Пароль'))

        password_entry1 = tk.Entry(root, width=60, background="white", show='')
        password_entry1.place(x=20, y=240, height=30)
        password_entry1.insert(0, 'Құпиясөзді қайталаңыз')
        password_entry1.bind('<FocusIn>', lambda event: on_entry_click3(event, password_entry1, 'Повторите пароль'))
        password_entry1.bind('<FocusOut>', lambda event: on_focus_out3(event, password_entry1, 'Повторите пароль'))

        btn = tk.Button(root, text='Жалғастыру', cursor='hand2', background='#75a8fc', width=40, height=2, command=check)
        btn.place(x=56, y=280)
        move = tk.Label(root, text=f'Жалғастыра отырып сіз ', background='Blue')
        move.place(x=40, y=340)
        move2=tk.Label(root,text='жеке ақпараттарды өңднуге келісім бересіз',background='Blue')
        move2.place(x=110,y=360)

        global lar
        lar=tk.Label(root, text='', foreground='white',background='white')
        lar.place(x=120, y=410)

    def login_page():
        tir.destroy()
        second.destroy()
        first.destroy()
        def on_entry_click(event):
            if lan1.get() == 'Email':
                lan1.delete(0, "end")
                lan1.insert(0, '')
                lan1.config(fg='black')

        def on_focus_out(event):
            if lan1.get() == '':
                lan1.insert(0, 'Email')
                lan1.config(fg='grey')

        def on_entry_click2(event):
            if password_entry.get() == 'Құпиясөз':
                password_entry.delete(0, "end")
                password_entry.insert(0, '')
                password_entry.config(show='*')
                password_entry.config(fg='black')

        def on_focus_out2(event):
            if password_entry.get() == '':
                password_entry.insert(0, 'Құпиясөз')
                password_entry.config(show='')
                password_entry.config(fg='grey')

        def chec():
            import psycopg2

            def check_credentials(username, password):
                connection = psycopg2.connect(
                    dbname='Tulpar',
                    user='postgres',
                    password='Tulpar14',
                    host='localhost',
                    port='5432'
                )
                cursor = connection.cursor()
                query = f"SELECT * FROM users_table WHERE email = '{username}' AND password = '{password}';"
                cursor.execute(query)
                result = cursor.fetchone()
                cursor.close()
                connection.close()
                return result is not None

            username_input = lan1.get()
            password_input = password_entry.get()

            if check_credentials(username_input, password_input):
                br.destroy()
                lan1.destroy()
                password_entry.destroy()
                btn.destroy()
                final_page()
            else:
                print('Error дұрыс ақпарат еңгізіңіз')

        br = tk.Label(root, text='Кіру', font=('monserat', 52),background='white')
        br.place(x=110, y=30)

        lan1 = tk.Entry(root, width=60, background="white")
        lan1.place(x=20, y=160, height=30)
        lan1.insert(0, 'Email')
        lan1.bind('<FocusIn>', on_entry_click)
        lan1.bind('<FocusOut>', on_focus_out)

        password_entry = tk.Entry(root, width=60, background="white", show='')
        password_entry.place(x=20, y=200, height=30)
        password_entry.insert(0, 'Құпиясөз')
        password_entry.bind('<FocusIn>', on_entry_click2)
        password_entry.bind('<FocusOut>', on_focus_out2)

        btn = tk.Button(root, text='Жалғастыру', cursor='hand2', background='#75a8fc', width=40, height=2,
                        command=chec)
        btn.place(x=56, y=280)
    def second_page():
        second.config(background='white', bd=0, foreground='blue', text='Кіру', command=login_page)
        tir.config(foreground='blue', command=sing_page)

    root = tk.Tk()
    icon_path = "SKILL.ico"
    root.iconbitmap(icon_path)
    root.config(background='white')
    root.title('Skill Sync')
    root.geometry('400x600')

    icon = PhotoImage(file="Find work.png")
    first = tk.Label(root, image=icon, bd=0)
    first.place(x=-40, y=30)

    second = tk.Button(root, text="Кіру", bd=0, background='black', foreground='#F6F7F9', width=40, height=2, command=second_page)
    second.place(x=70, y=480)

    tir = tk.Button(root, text="Тіркелу", bd=0, background='white', foreground='white', width=40, height=2)
    tir.place(x=70, y=520)

    root.mainloop()
first_page()