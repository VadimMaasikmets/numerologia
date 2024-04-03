﻿
import tkinter as tk
from tkinter import Toplevel, messagebox
from datetime import datetime
import amamam
import email
import smtplib, ssl
from email.message import EmailMessage

def calculate_pythagorean_numbers(day, month, year):
    sum_day_month = sum(map(int, str(day))) + sum(map(int, str(month)))
    sum_year = sum(map(int, str(year)))
    first_working_number = sum_day_month + sum_year
    second_working_number = sum(map(int, str(first_working_number)))
    if day >= 10:
        day_first_digit = int(str(day)[0])
    else:
        day_first_digit = day
    third_working_number = first_working_number - (2 * day_first_digit)
    fourth_working_number = sum(map(int, str(third_working_number)))
    return first_working_number, second_working_number, third_working_number, fourth_working_number

def open_email_window():
    global results
    if not results:
        messagebox.showerror("Ошибка", "Сначала рассчитайте результаты.")
        return
    
    def send_email():
        email = email_entry.get()
        saada_k(email, results)
        email_window.destroy()
    
    email_window = tk.Toplevel(root)
    email_window.title("Отправить результаты на почту")
    email_window.geometry("300x200")
    email_window.configure(bg='pink')
    
    tk.Label(email_window, text="Введите адрес электронной почты:", bg='pink', fg='black').pack(pady=10)
    email_entry = tk.Entry(email_window)
    email_entry.pack(pady=10)
    
    send_button = tk.Button(email_window, text="Отправить", command=send_email, bg='red', fg='black')
    send_button.pack(pady=20)

def saada_k(receiver_email, message_content):
    smtp_server = "smtp.gmail.com"
    port = 587 
    sender_email = "maasikmetssatoru@gmail.com"
    password = "lfvv xozu njuf bmjw" 

    msg = EmailMessage()
    msg["Subject"] = "Результаты расчёта"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(message_content)
    
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.send_message(msg)
            messagebox.showinfo("Успех", "Результаты успешно отправлены.")
    except Exception as e:
        messagebox.showerror("Ошибка отправки", str(e))

def calculate_and_show():
    global results
    date_str = entry_date.get()
    try:
        birth_date = datetime.strptime(date_str, "%d.%m.%Y")
        calculate_and_show_save()
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректный формат даты. Используйте ДД.ММ.ГГГГ")

def calculate_and_show_save():
    global results
    date_str = entry_date.get()
    print("Дата введена:", date_str)
    try:
        birth_date = datetime.strptime(date_str, "%d.%m.%Y")
        print("Дата успешно разобрана:", birth_date)
        day, month, year = birth_date.day, birth_date.month, birth_date.year
        numbers = calculate_pythagorean_numbers(day, month, year)  
        analysis = amamam.analyze_numbers(numbers)
        results = f"1-е рабочее число: {numbers[0]}\n2-е рабочее число: {numbers[1]}\n"\
                  f"3-е рабочее число: {numbers[2]}\n4-е рабочее число: {numbers[3]}\n\nАнализ:\n{analysis}"   
        print("Результаты расчета получены:", results)
        messagebox.showinfo("Результаты", results)
        filename = "results.txt"
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(results + '\n')
        print("Результаты записаны в файл:", filename)
    except ValueError as e:
        print("Ошибка:", e)


root = tk.Tk()
root.title("Расчет по методу Пифагора")
root.geometry("300x600")
root.configure(bg='pink')

tk.Label(root, text="Введите дату рождения (ДД.ММ.ГГГГ):", bg='pink', fg='black').pack(pady=(20, 0))
entry_date = tk.Entry(root)
entry_date.pack(pady=(0, 20))

calculate_button = tk.Button(root, text="Рассчитать", command=calculate_and_show, bg='red', fg='white')
calculate_button.pack(pady=(20, 20))

email_button = tk.Button(root, text="Отправить результат", command=open_email_window, bg='red', fg='white')
email_button.pack(pady=(0, 20))

root.mainloop()