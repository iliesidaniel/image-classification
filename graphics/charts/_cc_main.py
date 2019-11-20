import tkinter as tk

from graphics.charts.column_chart import ColumnChart
from utils.charts.chart_entries import ChartEntries, ChartEntry

root = tk.Tk()
root.title('Column chart dev')

f_cc = ColumnChart(parent=root)
f_cc.pack(side='top',
          fill='both',
          expand=True)

ces = ChartEntries()

classes = [
    'Airplane',
    'Automobile',
    'Bird',
    'Cat',
    'Deer',
    'Dog',
    'Frog',
    'Horse',
    'Ship',
    'Truck',
    'Airplane',
    'Automobile',
    'Bird',
    'Cat',
    'Deer',
    'Dog',
    'Frog',
    'Horse',
    'Ship',
    'Truck'
]

for i in range(2):
    tmp = ChartEntry()

    tmp.identifier = classes[i]
    tmp.x = 0
    tmp.y = i * 20 + 20

    ces.add(new_entry=tmp)
f_cc.update_values(ces)

# print(str(ces))

ces.clear()
for i in range(10):
    tmp = ChartEntry()

    tmp.identifier = classes[i]
    tmp.x = 0
    tmp.y = (i * 20) % 110

    ces.add(new_entry=tmp)
f_cc.update_values(ces)

# print(str(ces))

RWidth = root.winfo_screenwidth()
RHeight = root.winfo_screenheight()
root.geometry('%dx%d' % (RWidth, RHeight))

root.update()

root.minsize(1700, 900)
# root.attributes('-fullscreen', True)
# root.state('zoomed')

# root.minsize(root.winfo_width(), root.winfo_height())
# root.maxsize(root.winfo_width(), root.winfo_height())
# root.resizable(0, 0)

root.mainloop()
