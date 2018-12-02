
class confusionMatrix(object):
	
	def main(self, classNames, pred, output):

		matrix = []
		unclassified = 0
		for i in range(len(classNames)):
			matrix.append([])

		for j in range(len(classNames)):
			for k in range(len(classNames)):
				matrix[j].append([0])

		for x in range(len(output)):
			
			if pred[x] != 'N/A':
				outIndex = classNames.index(output[x])
				predIndex = classNames.index(pred[x])

				val = list(matrix[outIndex][predIndex])
				val[0] += 1
				matrix[outIndex][predIndex] = val
			else: 
				unclassified += 1

		return matrix, unclassified


