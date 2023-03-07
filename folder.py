import os
import shutil
import tkinter as tk
from tkinter import messagebox
from configparser import ConfigParser


class App:
    def __init__(self, master):
        self.master = master

        # 創建ConfigParser對象，並讀取ini文件
        self.config = ConfigParser()
        self.config.read('config.ini')

        # 創建用於輸入源文件夾和目標文件夾路徑的Entry控件
        tk.Label(master, text="Source folder:").grid(row=0, column=0)
        tk.Label(master, text="Target folder:").grid(row=1, column=0)
        self.source_folder_entry = tk.Entry(master, width=50)
        self.source_folder_entry.grid(row=0, column=1)
        self.target_folder_entry = tk.Entry(master, width=50)
        self.target_folder_entry.grid(row=1, column=1)

        self.confirm_var = tk.BooleanVar()
        self.confirm_checkbox = tk.Checkbutton(self.master, text="完全沒有資料夾", variable=self.confirm_var)
        self.confirm_checkbox.grid(row=2, column=0)

        
        # 從ini文件中讀取源文件夾和目標文件夾的路徑，並顯示在Entry控件中
        self.source_folder_entry.insert(tk.END, self.config.get('Folders', 'source_folder'))
        self.target_folder_entry.insert(tk.END, self.config.get('Folders', 'target_folder'))

        # 創建用於開始運行程式碼的按鈕
        tk.Button(master, text="Start", command=self.move_files).grid(row=2, column=0, columnspan=2)

    def move_files(self):
        print(self.confirm_var.get())
        # 從Entry控件中獲取輸入的源文件夾和目標文件夾路徑
        source_folder = self.source_folder_entry.get()
        target_folder = self.target_folder_entry.get()

        if(self.confirm_var.get()):
            if(source_folder != target_folder):
                messagebox.showerror('Error', '源文件夾和目標文件夾不的路徑不一致，請重新輸入！')
                return

        # 檢查輸入的路徑是否存在
        if not os.path.exists(source_folder):
            messagebox.showerror('Error', '源文件夾路徑不存在！')
            return
        if not os.path.exists(target_folder):
            messagebox.showerror('Error', '目標文件夾路徑不存在！')
            return

        # 儲存輸入的路徑到ini文件中
        self.config.set('Folders', 'source_folder', source_folder)
        self.config.set('Folders', 'target_folder', target_folder)
        with open('config.ini', 'w') as f:
            self.config.write(f)

        # 獲取源文件夾中所有文件夾的列表
        sub_folders = [f for f in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, f))]

        # 遍歷所有文件夾，將其內容移動到目標文件夾
        for folder in sub_folders:
            folder_path = os.path.join(source_folder, folder)
            for sub_file in os.listdir(folder_path):
                sub_file_path = os.path.join(folder_path, sub_file)
                # 如果文件已存在，則更改文件名稱
                while os.path.exists(os.path.join(target_folder, sub_file)):
                    sub_file = "_" + sub_file
                shutil.move(sub_file_path, os.path.join(target_folder, sub_file))
            os.rmdir(folder_path)

        # 檢查是否還有文件夾存在，如果有，彈出對話框詢問是否要重頭再運行程式碼
        sub_folders = [f for f in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, f))]
        
        if sub_folders:
            if(self.confirm_var.get()):
                self.move_files()
            else:
                if messagebox.askyesno('Confirm', '還有文件夾存在，是否要重頭再運行程式碼？'):
                    self.move_files()
                else:
                    self.master.destroy()
        else:
            messagebox.showinfo('Success', '所有文件已移動成功！')
            self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Move Files")
    app = App(root)
    root.mainloop()
