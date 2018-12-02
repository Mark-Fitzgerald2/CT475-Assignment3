import numpy as np
from scipy.integrate import simps
from numpy import trapz

class rocCurveGen(object):
	
	def main(self, probsArr, ArrOutTest, posLabel):
		
		TPRateArr = []
		FPRateArr = []

		for Threshold in np.linspace(0,1,1000):

			predictedClass = []
			for prob in probsArr:
				if prob >= Threshold:
					#Positive
					predictedClass.append(posLabel)
					#print('Positive')
				else:
					#Negative
					predictedClass.append('negative')
					#print('Negative')
			print(predictedClass)
			TN = TP = FP = FN = 0
			for count in range(0, len(ArrOutTest)):
				if predictedClass[count] == ArrOutTest[count]:
					if predictedClass[count] == posLabel:
						TP += 1
					else:
						TN += 1
				else: 
					if predictedClass[count] == posLabel:
						FP += 1
					else:
						FN += 1
			print('True Positive: ', TP)
			print('False Positive: ', FP)
			print('True Negative: ', TN)
			print('False Negative: ', FN)
			TPRate = TP/(TP+FN)
			FPRate = FP/(FP+TN)
			TPRateArr.append(TPRate)
			FPRateArr.append(FPRate)

		AUC = 0
		TPRateArr.reverse()
		FPRateArr.reverse()
		for i in range(1, len(TPRateArr)):
			if TPRateArr[i] - TPRateArr[i - 1] == 0:
				AUC += (FPRateArr[i] - FPRateArr[i - 1]) * TPRateArr[i]
			else:
				AUC += (FPRateArr[i] - FPRateArr[i - 1]) * TPRateArr[i - 1]
				AUC += 0.5 * (FPRateArr[i] - FPRateArr[i - 1]) * (TPRateArr[i] - TPRateArr[i - 1])

		return TPRateArr, FPRateArr, TP, FP, TN, FN, AUC


	def meanAUC(self, TPRateAvg, FPRateAvg):
		meanAUC = 0.0
		for i in range(1, len(TPRateAvg)):
			if TPRateAvg[i] - TPRateAvg[i - 1] == 0:
				meanAUC += (FPRateAvg[i] - FPRateAvg[i - 1]) * TPRateAvg[i]
			else:
				meanAUC += (FPRateAvg[i] - FPRateAvg[i - 1]) * TPRateAvg[i - 1]
				meanAUC += 0.5 * (FPRateAvg[i] - FPRateAvg[i - 1]) * (TPRateAvg[i] - TPRateAvg[i - 1])

		return meanAUC