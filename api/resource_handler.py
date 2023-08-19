import os
from typing import Optional

import pandas as pd

module_dir = os.path.dirname(__file__)  # get current directory


def load_data(file_name) -> Optional[pd.DataFrame]:
		"""
		The 'api method' for reading csv files.
		Returns a panda's data frame if the file path is correct.
		"""
		# get the file path of the file, don't forget the extension
		file_path = os.path.join(module_dir, file_name)
		# print("Data Set path: \n", file_path)

		try:
				# read data into a data frame
				data_frame = pd.read_csv(file_path, header=None).reset_index(drop=True)
		except:
				# return nothing, if file path is incorrect
				return None

		return data_frame


# from api.resource_handler import get_resources

def get_resources(fro, to):
		print(fro)
		print(to)
		frame = load_data('data.csv')
		frame = frame.loc[fro:to]

		print(frame.values)
		result = []
		for data in frame.values:
				result.append({'datetime': data[0], 'street_time': data[1], 'count': data[2], 'velocity': data[3]})

		return result
