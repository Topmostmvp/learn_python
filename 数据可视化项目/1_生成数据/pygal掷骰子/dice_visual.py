from die import Die
import pygal

#创建两个D6骰子
die_1 = Die()
die_2 = Die()

#掷多次骰子，并将结果储存在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() +die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sides +die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化分析
hist = pygal.Bar()  #bar为条形图

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [str(x_label) for x_label in range(2, max_result+1)]

#hist.x_labels = list(range(2, 13))亦可
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6+D6', frequencies)  #将分析结果添加到图表中
hist.render_to_file('dice_visual.svg')