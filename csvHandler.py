import pandas as pd 

def loadDictFromCSV(filePath):
    df_csv = pd.read_csv(filePath + '//userData.csv', usecols=range(1,4))
    print("Hello there")
    return df_csv.to_dict(orient = 'list')

def saveDictToCSV(my_dict, filePath):
    df = pd.DataFrame(my_dict)
    df.to_csv(filePath + '//userData.csv')  
    return True

def updateDict(my_dict, data):
    keys = ["date", "cost", "image path"]
    for i in range(0, len(keys), 1):
        my_dict[keys[i]].append(data[i])
    return True

def getNumberOfEntries(my_dict, key):
	return len(my_dict[key])

def getCost(my_dict): 
	data = my_dict['cost']
	totalCost = 0
	for value in data:
		totalCost = totalCost + value

	return totalCost

# my_dict = loadDictFromCSV('userData.csv')
# updateDict(my_dict, ["oct 27", "42", "anotherImg.jpg"])
# updateDict(my_dict, ["nov 14", "15", "specialImg.jpg"])
# saveDictToCSV(my_dict, 'userData.csv')




  
