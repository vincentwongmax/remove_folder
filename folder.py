import os
import shutil
import tkinter as tk
from tkinter import messagebox
from configparser import ConfigParser

# 創建ConfigParser對象，並讀取ini文件
config = ConfigParser()
config.read('config.ini')

# 從ini文件中讀取源文件夾和目標文件夾的路徑
source_folder = string_with_forwardslash = config.get('Folders', 'source_folder').replace('\\ ', '/')
target_folder = string_with_forwardslash = config.get('Folders', 'target_folder').replace('\\ ', '/')


def move_files():
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
        
        # 移除空文件夾
        os.rmdir(folder_path)

    # 檢查目標文件夾中是否還有文件夾
    if any(os.path.isdir(os.path.join(target_folder, f)) for f in os.listdir(target_folder)):
        # 彈出對話框詢問是否重新運行程式碼
        root = tk.Tk()
        root.withdraw()
        msg_box = messagebox.askquestion('Question', '目標文件夾中還有文件夾，是否重新運行程式碼？')
        if msg_box == 'yes':
            move_files()
        else:
            messagebox.showinfo('Info', '程式結束')

# 開始運行程式
move_files()
