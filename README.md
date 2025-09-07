# 📅 智慧行事曆應用 (Calendar + To-do + Weather Notification)

🎥 **Demo 影片**  
[![Demo Video](https://img.youtube.com/vi/P6KZMJltXSI/0.jpg)](https://youtu.be/P6KZMJltXSI?si=IUyt8VO2YJZiFF__)

這是一個以 **Python + Flask** 打造的應用，整合了 **月曆、待辦事項提醒與紀錄、天氣通知** 等功能。

## ✨ 特色功能
1. **事件排序與進度顯示**  
   - 可依據不同事件的重要程度進行排序  
   - 若事件包含多個階段，會根據完成度顯示整體進度  

2. **天氣資訊提醒**  
   - 當事件設定了特定地區，可顯示該地區的 **天氣、濕度、溫度**  

3. **每日鼓勵小語**  
   - 系統會每日自動生成一句勵志小語  
   - 讓使用者在規劃行程時更有動力 💪

 ```
Calendar/
│
├── app.py           # 主 Flask 應用程式文件
├── task.xlsx           
├── templates/
│   ├── task.html    #新增或編輯事件，提供表單介面輸入
│   ├── task_details.html    #當使用者在task_on_date.html點選指定任務，會顯示該任務的所有子任務
│   ├── task_on_date.html    #當使用者在index.html點選指定日期，會顯示當天的所有任務
│   └── index.html   #主頁面，顯示日曆       
└── static/
    ├── styles.css         # CSS 文件
    ├── sea.jpg         # 背景圖
    └── calendar.js        
```
