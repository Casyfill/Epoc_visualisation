#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import os


def simplify (sourcePath):
	

	def simplifyData(rows, m):
		tempList = []
		res  = []
		Max = 1

		for row in data:
			tempList.append(row)

			if len(tempList)==m:
				cols = len(tempList[0])
				newRow = []
				for i in xrange(cols):
					tempValue = sum([float(row[i]) for row in tempList])/len([row[i] for row in tempList])
					newRow.append(tempValue)

				res.append(newRow)
				tempList = []
						# print average

		return res

	# sourcePath = "/Users/casy/Dropbox (RN&IA'N)/Projects/Kats/Afisha/2014_05_27_Epoch/data/patient1/12.csv"
	resPath = sourcePath.replace('patient','simplified/patient').replace('.csv','s.csv')

	rPath = ''
	with open(sourcePath, 'r') as f:
		reader = csv.reader(f, delimiter=',', quotechar='"')
		next(reader, None)  # skip the headers

		headers = [['bored','excitement','meditation','frustration','position','soundPeak']]
		data = list(reader)
		totalrows = len(data)
		Max = int(totalrows/550)
		

		res = simplifyData(data, Max)
		# print resPath.split('/')[-1], ' written! rows:', totalrows, ':', Max, ':', len(res)
		res = headers + res

		with open(resPath, 'w') as result:
			writer = csv.writer(result, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		   	writer.writerows(res)
		   	print resPath.split('/')[-1], ' written! rows:', len(res), ':', totalrows, ':', Max
		   	# print resPath

basepath = "/Users/casy/Dropbox (RN&IA'N)/Projects/Kats/Afisha/2014_05_27_Epoch/data/"
patients = ['patient1','patient2','patient3']

for  p in patients:
	path = basepath + p
	for file in os.listdir(path):
	    if file.endswith(".csv"):
	        sumPath = path + '/' + file
	        simplify(sumPath)
	        # print sumPath

