import tkinter as tk
from tkinter import messagebox
import os

phone_file = 'Phone.txt'
recnew_file = 'recnew.txt'

def main_menu():
    root = tk.Tk()
    root.title("Телефонный справочник")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Label(frame, text="Телефонный справочник", font=("Arial", 16)).pack(pady=10)

    buttons_frame = tk.Frame(frame)
    buttons_frame.pack(pady=10)

    tk.Button(buttons_frame, text="Найти в базе номер", command=search_entry, width=25, relief='raised', bd=3).pack(pady=5)
    tk.Button(buttons_frame, text="Добавить в базу номер", command=add_entry, width=25, relief='raised', bd=3).pack(pady=5)
    tk.Button(buttons_frame, text="Удалить номер", command=delete_entry, width=25, relief='raised', bd=3).pack(pady=5)
    tk.Button(buttons_frame, text="Копировать данные", command=copy_entry, width=25, relief='raised', bd=3).pack(pady=5)
    tk.Button(buttons_frame, text="Выйти из программы", command=root.quit, width=25, relief='raised', bd=3).pack(pady=5)

    root.mainloop()

def search_entry():
    search_window = tk.Toplevel()
    search_window.title("Поиск записи")

    tk.Label(search_window, text="Введите фамилию или имя для поиска:").pack(pady=5)
    search_query = tk.Entry(search_window, width=30, bg='white')
    search_query.pack(pady=5)

    result_frame = tk.LabelFrame(search_window, text="Результат поиска", padx=10, pady=10)
    result_frame.pack(padx=10, pady=10)
    result_text = tk.Text(result_frame, width=50, height=10, bg='white')
    result_text.pack(pady=5)

    def search():
        query = search_query.get().lower()
        result_text.delete('1.0', tk.END)
        global search_results
        search_results = []
        with open(phone_file, 'r', encoding='utf-8') as file:
            found = False
            for line in file:
                if query in line.lower():
                    result_text.insert(tk.END, f"Найдена запись: {line.strip()}\n")
                    search_results.append(line.strip())
                    found = True
            if not found:
                result_text.insert(tk.END, "Запись не найдена.\n")

    tk.Button(search_window, text="Поиск", command=search, relief='raised', bd=3).pack(pady=5)

def add_entry():
    add_window = tk.Toplevel()
    add_window.title("Добавить запись")

    tk.Label(add_window, text="Фамилия:").pack(pady=5)
    surname = tk.Entry(add_window, width=30, bg='white')
    surname.pack(pady=5)

    tk.Label(add_window, text="Имя:").pack(pady=5)
    name = tk.Entry(add_window, width=30, bg='white')
    name.pack(pady=5)

    tk.Label(add_window, text="Отчество:").pack(pady=5)
    patronymic = tk.Entry(add_window, width=30, bg='white')
    patronymic.pack(pady=5)

    tk.Label(add_window, text="Номер телефона:").pack(pady=5)
    phone_number = tk.Entry(add_window, width=30, bg='white')
    phone_number.pack(pady=5)

    def add():
        with open(phone_file, 'a', encoding='utf-8') as file:
            file.write(f"{surname.get()}, {name.get()}, {patronymic.get()}, {phone_number.get()}\n")
        messagebox.showinfo("Добавление записи", "Запись добавлена.")
        add_window.destroy()

    tk.Button(add_window, text="Добавить", command=add, relief='raised', bd=3).pack(pady=5)

def delete_entry():
    delete_window = tk.Toplevel()
    delete_window.title("Удалить запись")

    tk.Label(delete_window, text="Введите фамилию или имя для удаления:").pack(pady=5)
    delete_query = tk.Entry(delete_window, width=30, bg='white')
    delete_query.pack(pady=5)

    def delete():
        query = delete_query.get().lower()
        lines = []
        with open(phone_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open(phone_file, 'w', encoding='utf-8') as file:
            found = False
            for line in lines:
                if query not in line.lower():
                    file.write(line)
                else:
                    found = True
            if found:
                messagebox.showinfo("Удаление записи", "Запись удалена.")
            else:
                messagebox.showwarning("Удаление записи", "Запись не найдена.")
        delete_window.destroy()

    tk.Button(delete_window, text="Удалить", command=delete, relief='raised', bd=3).pack(pady=5)

def copy_entry():
    copy_window = tk.Toplevel()
    copy_window.title("Копировать запись")

    tk.Label(copy_window, text="Записи для копирования:").pack(pady=5)
    copy_listbox = tk.Listbox(copy_window, selectmode=tk.EXTENDED, width=50, height=10)
    copy_listbox.pack(pady=5)

    for result in search_results:
        copy_listbox.insert(tk.END, result)

    def copy():
        selected_indices = copy_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Копирование записи", "Записи не выбраны.")
            return

        with open(recnew_file, 'a', encoding='utf-8') as dest_file:
            for i in selected_indices:
                dest_file.write(search_results[i] + '\n')

        messagebox.showinfo("Копирование записи", "Записи скопированы.")
        copy_window.destroy()

    tk.Button(copy_window, text="Копировать", command=copy, relief='raised', bd=3).pack(pady=5)

if __name__ == "__main__":
    if not os.path.exists(phone_file):
        with open(phone_file, 'w', encoding='utf-8'):
            pass
    if not os.path.exists(recnew_file):
        with open(recnew_file, 'w', encoding='utf-8'):
            pass
    search_results = []
    main_menu()