# Author: Nahum Maciel
# Email: nahumamaciel@gmail.com
# Date: 2021-04-27
# File: main.py

import datetime
from datetime import datetime
import tkinter as tk

BG = '#0d2b51'

WINDOW = tk.Tk()
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
            bg='#244670',
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
                "%m/%d/%Y %H:%M"
            )
            end_parsed = datetime.strptime(
                self.ent_end.ent.get(),
                "%m/%d/%Y %H:%M"
            )

            interval_delta = end_parsed - start_parsed
            total_hours = (interval_delta.seconds)/3600

            self.lbl_display.lbl["text"] = f"{total_hours} hrs"

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