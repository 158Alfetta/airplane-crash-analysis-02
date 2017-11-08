'''Plot graph year'''
import years
import pygal
def main():
	'''Main function'''
	year()

def year():
	dict_ = years.allyear()
	line_chart = pygal.HorizontalBar()
	line_chart.title = 'Amount of fatalities in plane crash (years)'
	keys = [key for key in dict_.keys()]
	keys.sort(reverse=True)
	line_chart.add('Fatalities', [dict_[key] for key in keys])
	line_chart.x_labels = keys
	line_chart.render_to_file('line_chart.svg')

main()
