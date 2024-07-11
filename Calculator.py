import tkinter as tk
from tkinter  import ttk
from typing import Callable

class Calculator:
    """
    Represents a single instance of a calculator application.
    """
    def __init__(self):
        """
        Initialises the app window, dimensions ui elements.
        """
        self.root = tk.Tk()
        self.root.geometry("312x200")
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.FONT = ("Helvetica", 35)

        self.screen = ttk.Label(self.root, text="", font=self.FONT, 
                                background="white", borderwidth=2,
                                relief="groove")
        self.screen.grid(row=0, column=0, columnspan=4, sticky="NWSE")


        self.seven = ttk.Button(text="7", command=self.symbol("7"))
        self.seven.grid(row=1, column=0, padx=1, pady=2, sticky="NSWE")

        self.eight = ttk.Button(text="8", command=self.symbol("8"))
        self.eight.grid(row=1, column=1, padx=1, pady=2, sticky="NSWE")

        self.nine = ttk.Button(text="9", command=self.symbol("9"))
        self.nine.grid(row=1, column=2, padx=1, pady=2, sticky="NSWE")

        self.division = ttk.Button(text="/", command=self.symbol("/"))
        self.division.grid(row=1, column=3, padx=1, pady=2, sticky="NSWE")

        self.four = ttk.Button(text="4", command=self.symbol("4"))
        self.four.grid(row=2, column=0, padx=1, pady=2, sticky="NSWE")

        self.five = ttk.Button(text="5", command=self.symbol("5"))
        self.five.grid(row=2, column=1, padx=1, pady=2, sticky="NSWE")

        self.six = ttk.Button(text="6", command=self.symbol("6"))
        self.six.grid(row=2, column=2, padx=1, pady=2, sticky="NSWE")

        self.multiplication = ttk.Button(text="*", command=self.symbol("*"))
        self.multiplication.grid(row=2, column=3, padx=1, pady=2, sticky="NSWE")

        self.one = ttk.Button(text="1", command=self.symbol("1"))
        self.one.grid(row=3, column=0, padx=1, pady=2, sticky="NSWE")

        self.two = ttk.Button(text="2", command=self.symbol("2"))
        self.two.grid(row=3, column=1, padx=1, pady=2, sticky="NSWE")

        self.three = ttk.Button(text="3", command=self.symbol("3"))
        self.three.grid(row=3, column=2, padx=1, pady=2, sticky="NSWE")

        self.subtraction = ttk.Button(text="-", command=self.symbol("-"))
        self.subtraction.grid(row=3, column=3, padx=1, pady=2, sticky="NSWE")

        self.zero = ttk.Button(text="0", command=self.symbol("0"))
        self.zero.grid(row=4, column=0, padx=1, pady=2, sticky="NSWE")

        self.clear = ttk.Button(text="C", command=self.clear_screen)
        self.clear.grid(row=4, column=1, padx=1, pady=2, sticky="NSWE")

        self.equals = ttk.Button(text="=", command=self.evaluate)
        self.equals.grid(row=4, column=2, padx=1, pady=2, sticky="NSWE")

        self.addition = ttk.Button(text="+", command=self.symbol("+"))
        self.addition.grid(row=4, column=3, padx=1, pady=2, sticky="NSWE")

        self.delete = ttk.Button(text="Del", command=self.delete_last)
        self.delete.grid(row=5, column=0, columnspan=4, padx=1, pady=2, sticky="NSWE")

        self.MAX_CHARS = 11
        self.current_equation: str = ""
        self.just_solved: bool = False

        self.root.mainloop()

    def delete_last(self) -> None:
        """
        Delete the last character on the screen. If a solution has just been
        calculated, delete the whole solution.
        """
        if self.current_equation:
            self.current_equation = self.current_equation[:-1]
        if self.just_solved:
            self.current_equation = ""
        self.screen.config(text=self.current_equation)

    def evaluate(self) -> None:
        """
        Evaluate the expression on the screen.
        """
        try:
            solution: float = float(eval(self.current_equation))
        except ZeroDivisionError:
            solution = 0.0
        except SyntaxError:
            pass
        
        try:
            if solution.is_integer():
                solution = int(solution)

            solution = round(solution, 5)
            self.screen.config(text=solution)
            self.current_equation = f"{solution}"
            self.just_solved = True
        except UnboundLocalError:
            pass

    def clear_screen(self) -> None:
        """
        Delete all charcters from the screen.
        """
        self.screen.config(text="")
        self.current_equation = ""


    def symbol(self, symbol: str) -> Callable:
        """
        Returns a function that adds a given character to the screen.
        :param symbol: the character to be added.
        :return: a function that adds the specified character to the screen.
        """
        def inner():
            if len(self.current_equation) >= self.MAX_CHARS:
                return

            if self.just_solved and symbol in '0123456789':
                self.current_equation = ""

            if self.current_equation and symbol == '0' and \
             self.current_equation[-1] in '+-/*':
                return

            if symbol in '+-/*':
                if self.current_equation and self.current_equation[-1] in '+-/*':
                    self.current_equation = self.current_equation[:-1]
            if symbol in '+-/*':
                if not self.current_equation or  \
                 self.current_equation[-1] not in '0123456789':
                    self.current_equation += '0'
            
            self.current_equation += symbol
            self.screen.config(text=self.current_equation)
            self.just_solved = False

        return inner

if __name__ == "__main__":
    Calculator()