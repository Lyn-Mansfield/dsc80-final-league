import pandas as pd
import numpy as np


# clean DataFrame constructed like LoL data
def clean_lol_data(dataframe):
	df_copy = dataframe.copy()


	# turn int columns into ints
	for column in df_copy.columns:
		column_series = df_copy[column]
		example_entry = column_series[column_series != ''].iloc[0]
		# print(column, example_entry, type(example_entry))
		try:
			# try to turn first entry into int
			int(example_entry)
			# if it can be turned into an int, then transform the whole column, imputing -1 instead of nan
			# print(f"{example_entry} can be turned into an int!")
			df_copy[column] = df_copy[column].apply(lambda x: x if x != '' else '-1')
			df_copy[column] = df_copy[column].astype(int)
		except ValueError:
			# print(f"{example_entry} cannot be turned into an int...")
			continue

	# turn empty strings into np.NaN, now that we won't poison the int columns
	df_copy = df_copy.replace(to_replace='', value=np.nan)

	# turn float columns into floats
	for column in df_copy.columns:
		# if already turned into float, then skip
		if df_copy[column].dtype == int:
			continue

		column_series = df_copy[column]
		example_entry = column_series.iloc[column_series.first_valid_index()]
		# print(column, example_entry, type(example_entry))
		try:
			# try to turn first non-NaN entry into float
			float(example_entry)
			# if it can be turned into an float, then transform the whole column
			df_copy[column] = df_copy[column].astype(float)
		except ValueError:
			continue

	# turn date column into pd.Datetime
	df_copy['date'] = pd.to_datetime(df_copy['date'])

	# for boolean columns, give special treatment
	boolean_columns = ['firstblood', 'firstbloodkill', 'firstbloodassist', 'firstbloodvictim', 'monsterkillsownjungle', 'monsterkillsenemyjungle']
	def transform_int_to_bool(x):
		if x == 1:
			return True
		if x == 0:
			return False
		if x == -1:
			return np.nan
	for column in boolean_columns:
		df_copy[column] = df_copy[column].apply(transform_int_to_bool)

	# clearly label if players won or lost
	df_copy['result'] = df_copy['result'].apply(lambda x: 'Won' if x == 1 else 'Lost')

	print(df_copy.columns)
	# drop unneeded rows
	random_game_columns = [df_copy.columns[i] for i in range(45, 76)]
	df_copy = df_copy.drop(random_game_columns, axis=1)

	# split into avg vs time info
	overall_game_df = df_copy.iloc[:, :70].set_index('gameid')
	time_data_df = df_copy.iloc[:, 70:]
	time_data_df['gameid'] = df_copy['gameid']
	time_data_df = time_data_df.set_index('gameid')

	return (overall_game_df, time_data_df)