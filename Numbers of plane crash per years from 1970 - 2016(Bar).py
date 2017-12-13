'''Plot graph year'''
import years
import pygal
def main():
	'''Numbers of plane crash per years from 1970 - 2016'''
	year()
def year():
	dict_ = years.allyear()
	line_chart = pygal.HorizontalBar()
	line_chart.title = 'Numbers of plane crash per years from 1970 - 2016'
	# add key to list
	keys = [key for key in dict_.keys()]
	keys.sort(reverse=True)
	#add key to chart
	line_chart.add('Per years', [dict_[key] for key in keys])
	line_chart.x_labels = keys #add keys to x labels
	line_chart.render_to_file('line_chart.svg')

main()
