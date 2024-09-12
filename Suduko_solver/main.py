import tkinter as tk
from tkinter import messagebox

def check(mat,row,col,num):
    for i in range(9):

        if mat[i][col]==num or mat[row][i]==num:
            return False

    boxrow = 3* (row//3)
    boxcol = 3* (col//3)
    for i in range(3):
        for j in range(3):
            if mat[boxrow+i][boxcol+j]==num:
                return False
    return True

def solvemat(mat):
    for row in range(9):
        for col in range(9):
            if mat[row][col]==0:
                for num in range(1,10):
                    if check(mat,row,col,num):
                        mat[row][col]=num
                        if solvemat(mat):
                            return True
                        mat[row][col]=0
                return False
    return True

def getmat():
    mat=[]
    for row in range(9):
        mat.append([])
        for col in range(9):
            value=entries[row][col].get()
            if value=='':
                mat[row].append(0)
            else:
                mat[row].append(int(value))
    return mat

def setmat(mat):
    for row in range(9):
        for col in range(9):
            if mat[row][col]!=0:
                entries[row][col].delete(0,tk.END)
                entries[row][col].insert(0,str(mat[row][col]))
            else:
                entries[row][col].delete(0,tk.END)

def validate_input(mat):
    for row in range(9):
        row_vals=[val for val in mat[row] if val!=0]
        if len(row_vals) != len(set(row_vals)):
            return False
    for col in range(9):
        col_vals=[mat[row][col] for row in range(9) if mat[row][col] != 0]
        if len(col_vals)!=len(set(col_vals)):
            return False
    for boxrow in range(0,9,3):
        for boxcol in range(0,9,3):
            subgrid_vals=[]
            for i in range(3):
                for j in range(3):
                    if mat[boxrow+i][boxcol+j]!=0:
                        subgrid_vals.append(mat[boxrow+i][boxcol+j])
            if len(subgrid_vals) != len(set(subgrid_vals)):
                return False

    return True
def solve():
    mat=getmat()
    if not validate_input(mat):
        messagebox.showerror("Error","Invalid suduko input: Duplicate number found")
        return
    if solvemat(mat):
        setmat(mat)
    else:
        messagebox.showerror("Error", "No solution exist for this Suduko.")

def clearmat():
    for row in range(9):
        for col in range(9):
            entries[row][col].delete(0,tk.END)


root = tk.Tk()
root.title("Suduko Solver")

entries=[]
for row in range(9):
    row_entries=[]
    for col in range(9):
        entry=tk.Entry(root,width=3,font=('Arial',18), justify='center')
        entry.grid(row=row,column=col,padx=5,pady=5)
        row_entries.append(entry)
    entries.append(row_entries)

solve_button=tk.Button(root,text="Solve",command=solve, font=('Arial',15))
solve_button.grid(row=9,column=3,columnspan=5)

clear_button=tk.Button(root, text="Clear", command=clearmat,font=('Arial',15))
clear_button.grid(row=9,column=5,columnspan=5)

root.mainloop()
