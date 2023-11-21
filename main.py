from tkinter import *
import wikipedia

def wikipedia_request():
    # Функция для поиска запроса на сайте Wikipedia.
    wikipedia.set_lang("ru")
    try:
        result = wikipedia.summary(txt.get())
        lbl2.config(text=result)
        text.insert(END, lbl2.cget("text") + '\n')
    except wikipedia.exceptions.PageError:
        #Исключение, если запрос не может найти информацию на сайте.
        lbl2.config(text="Страница не найдена.")
        text.insert(END, lbl2.cget("text") + '\n')
    except wikipedia.exceptions.DisambiguationError as e:
        #Исключение, если по запросу находиться несколько страниц и надо уточнить, что именно ищет пользователь.
        options = "\n".join(e.options)
        lbl2.config(text=f"Уточните запрос. Найдено несколько возможных страниц:\n{options}")
        text.insert(END, lbl2.cget("text") + '\n')


def del_info():
    #Перед новым запросом очищаем страницу и поле запроса.
    text.delete("1.0", END)
    txt.delete(0, END)

#Используем библиотеку tkinter для создания интерфейса программы
window = Tk()
window.title("Википедия")
window.geometry('900x700')
window.image = PhotoImage(file='logo.png')
bg_logo = Label(window, image=window.image) #
bg_logo.place(relx=0, rely=0)

lbl_0 = Label(window)
lbl_0.grid(row=0, column=0)

#Создание Label с текстом 'Введите ваш запрос: '.
lbl = Label(window,
            text='Введите ваш запрос (RU): ',
            font=("Times New Roman", 14), bg='grey72',
            padx=10,
            pady=10)
lbl.grid(row=1, column=1)

lbl_2 = Label(window)
lbl_2.grid(row=2, column=0)

#Label, куда будет вставляться ответ на запрос.
lbl2 = Label(window, text='',
             font=("Times New Roman", 14),
             wraplength=500,
             justify='center',
             pady=10
             )
# lbl2.grid(row=3, column=1, columnspan=25, stick='we')

#Tекстовоe окнo, куда будет копироваться информация из Label(т.к. на Label нельзя установить Scroll)
text = Text(window, wrap="word",
            font=("Times New Roman", 14),
            padx=15, pady=10)
text.grid(row=3, column=1, columnspan=10, stick='we')

#Skrolling полученного ответа
scroll_lbl2 = Scrollbar(orient='vertical', command=text.yview)
scroll_lbl2.grid(row=3, column=11, stick='ns')

#Поле куда будет вводиться запрос
txt = Entry(window, font=("Times New Roman", 14), bg='grey72')
txt.grid(row=1, column=2, pady=5)
txt.focus()

#Кнопка поиска по запросу.
Button(window, text='Поиск',
       font=("Times New Roman", 14), bg='grey72',
       command=wikipedia_request).grid(row=1, column=3, stick='we')

#Кнопка удаления информации предыдущего запроса.
Button(window, text="Очистить окно",
       font=("Times New Roman", 14), bg='grey72',
       command=del_info).grid(row=1, column=4, stick='we')

#Задаем размер колонок для расположения Labe,Text,Button.
window.grid_columnconfigure(0, minsize=50)
window.grid_columnconfigure(1, minsize=50)
window.grid_columnconfigure(2, minsize=50)
window.grid_columnconfigure(3, minsize=70)
window.grid_columnconfigure(4, minsize=50)
window.grid_columnconfigure(5, minsize=50)
window.grid_rowconfigure(0, minsize=30)
window.grid_rowconfigure(1, minsize=50)
window.grid_rowconfigure(2, minsize=30)
window.grid_rowconfigure(3, minsize=50)
window.grid_rowconfigure(4, minsize=50)

window.mainloop()