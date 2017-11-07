'''Clean Data'''
import pandas as pd
def main():
	'''Main function'''
	clean_year()

def clean_year():
	'''Format year to y/d/m'''
	df = pd.read_csv('dataset psit.csv')
	df.Date = pd.to_datetime(df.Date)
	df.to_csv('clean_data_year.csv')

main()