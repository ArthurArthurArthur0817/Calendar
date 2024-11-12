from flask import Flask, render_template, request, redirect, url_for
import calendar
from datetime import datetime
import openpyxl

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calendar_view():
    year = datetime.now().year
    month = datetime.now().month

    if request.method == 'POST':
        year = int(request.form.get('year', year))
        month = int(request.form.get('month', month))

    cal = calendar.HTMLCalendar().formatmonth(year, month)
    return render_template('calendar.html', calendar=cal, year=year, month=month)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        date = request.form['date']
        task = request.form['task']
        location = request.form['location']
        priorty = request.form['priorty']
        detail_1 = request.form.get('detail_1', '')
        detail_2 = request.form.get('detail_2', '')
        detail_3 = request.form.get('detail_3', '')

        # 儲存資料到 tasks.xlsx
        save_to_excel(date, task, location, priorty, detail_1, detail_2, detail_3)

        return redirect(url_for('calendar_view'))

    return render_template('date.html')

def save_to_excel(date, task, location, priorty, detail_1, detail_2, detail_3):
    try:
        workbook = openpyxl.load_workbook('task.xlsx')
    except FileNotFoundError:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(["Date", "Task", "Location","priorty", "detail_1", "detail_2", "detail_3"])  # 標題行
    else:
        sheet = workbook.active

    # 新增一行資料
    sheet.append([date, task, location,priorty, detail_1, detail_2, detail_3])
    workbook.save('task.xlsx')

if __name__ == '__main__':
    app.run(debug=True)
