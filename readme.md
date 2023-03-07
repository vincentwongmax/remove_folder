# 指定的文件夾中的所有文件夾的子內容移到指定目錄然後移除空文件夾(V2.1)

## 使用方法 
1. 打開folder.exe 文件
2. 輸入source_folder
3. 輸入target_folder
4. 是否要勾選多層清空
5. 是否要勾選備份原文件夾

## 說明
1.  程式文件中，若果提取過程中有同樣名字的文件，則會在文件名稱中加上  _  。
2.  文件的路徑使用中文有可能導致程式發生錯誤。
3.  文件的路徑中可以直接使用WINDOWS 中的文件路徑。
4.  建議 source_folder 和target_folder 中的路徑一致。
5.  這個程式會檢查多次是否還有資料夾的存在，並詢問使用者，是否再次運行程式。
6.  新增一鍵移除多層子資料夾
7.  提供EXE 文件版本，可直接使用。 
8.  新增使用者介面
   

PS : 使用本程式是需要注意，操作後，WINDOWS系統是無法復原的。


## python 程式碼TO EXE (先打開powershell, 輸入以下程式碼)
```
pyinstaller --name=MoveFiles --onefile --windowed --specpath=. folder.py
```