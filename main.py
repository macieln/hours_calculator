# Author: Nahum Maciel
# Email: nahumamaciel@gmail.com
# Date: 2021-04-27
# File: main.py

import datetime
from datetime import datetime
import tkinter as tk

BG = '#1b2537'

WINDOW = tk.Tk()
# WINDOW.withdraw()
WINDOW.configure(bg=BG)
WINDOW.title('Time Calculator')


class Lbl_Interval:

    def __init__(self, row, column, master, text):
        lbl = tk.Label(
            master=master,
            text=text,
            font='arial 16 bold',
            bg=BG,
            fg='#ca8538'
        )

        lbl.grid(
            row=row,
            column=column,
            padx=25,
            pady=2.5,
            sticky="w"
        )


class Ent_Interval:

    def __init__(self, row, column, master):
        self.ent = tk.Entry(
            master=master,
            font='arial 16',
            bg='#ffffff',
            fg='#D4806A',
            relief=tk.FLAT,
            width=16,
            justify='center'
        )
        self.ent.grid(
            row=row,
            column=column,
            padx=25,
            ipady=5
        )


class Lbl_Display:

    def __init__(self, row, column, master):
        self.lbl = tk.Label(
            master=WINDOW,
            text='0.0 hrs',
            font='arial 24 bold',
            bg='#8C929D',
            fg=BG
        )
        self.lbl.grid(
            row=row,
            column=column,
            padx=25,
            ipady=50,
            columnspan=2,
            sticky="nesw"
        )


class Hours_Calculator_Form:

    class Btn_Calculator:

        def hours_calcualtor(self):
            start_parsed = datetime.strptime(
                self.ent_start.ent.get(),
                "%m/%d/%Y   %H:%M"
            )
            print(start_parsed)
            end_parsed = datetime.strptime(
                self.ent_end.ent.get(),
                "%m/%d/%Y   %H:%M"
            )
            interval_delta = end_parsed - start_parsed
            total_hours = (interval_delta.days * 24) + interval_delta.seconds / 3600
            self.lbl_display.lbl["text"] = '{0:.2f} hrs'.format(total_hours)

        def calcualtor_caller(self, event):
            self.hours_calcualtor()

        def get_paste_interval(self, event):
            input_start_interval = WINDOW.clipboard_get().split("\t")[0]
            input_end_interval = WINDOW.clipboard_get().split("\t")[1]

            self.ent_start.ent.delete(0, tk.END)
            self.ent_end.ent.delete(0, tk.END)

            self.ent_start.ent.insert(0, input_start_interval)
            self.ent_end.ent.insert(0, input_end_interval)

            self.hours_calcualtor()

        def __init__(
            self,
            row,
            column,
            master,
            ent_start,
            ent_end,
            lbl_display,
            text='Calculate'
        ):
            btn = tk.Button(
                master=master,
                text=text,
                font='arial 16 bold',
                bg='#18ae94',
                fg='#ffffff',
                relief=tk.FLAT,
                command=self.hours_calcualtor
            )
            btn.grid(
                row=row,
                column=column,
                padx=25,
                pady=20,
                columnspan=2,
                sticky="nesw"
            )

            WINDOW.bind('<Return>', self.calcualtor_caller)
            WINDOW.bind('<<Paste>>', self.get_paste_interval)
            self.ent_start = ent_start
            self.ent_end = ent_end

            self.lbl_display = lbl_display

    def __init__(self):
        frm_header = tk.Frame(WINDOW, bg=BG)
        frm_header.grid(row=0, column=0, padx=25, pady=15)

        Lbl_Interval(1, 0, WINDOW, "Start")
        Lbl_Interval(1, 1, WINDOW, "End")

        self.ent_start_interval = Ent_Interval(2, 0, WINDOW)
        self.ent_end_interval = Ent_Interval(2, 1, WINDOW)

        self.lbl_display = Lbl_Display(4, 0, WINDOW)

        self.Btn_Calculator(
            3,
            0,
            WINDOW,
            self.ent_start_interval,
            self.ent_end_interval,
            self.lbl_display
        )

        frm_footer = tk.Frame(WINDOW, bg=BG)
        frm_footer.grid(row=6, column=0, padx=25, pady=15)


Hours_Calculator_Form()
WINDOW.mainloop()
