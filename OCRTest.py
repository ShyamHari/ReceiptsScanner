import requests
import json
import cv2 as cv
import re

def ocr_space_file(filename, overlay=False, api_key='1940116e7488957', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """
    print("interfacing with OCR API")
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'isTable' : True,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

def getCost(filename):
    print("getting cost...")
    data = ocr_space_file(filename=filename, language='pol')
    detectedText = json.loads(data)
    #print(detectedText)
    parsedText = detectedText["ParsedResults"]
    parsedText = parsedText[0]["ParsedText"]

    hstIndex = parsedText.rfind('HST')
    if hstIndex != -1:
        parsedText = parsedText[hstIndex:len(parsedText)]
    else:
        print("\t Couldn't find hst")
    
    totalIndex = parsedText.rfind("Total")
    if totalIndex != -1:
        newString2 = parsedText[totalIndex:len(parsedText)]
        totalValueIndexEnd = newString2.find("\n")
        totalValueIndexStart = newString2.find("\t")
    else:
        print("\t Couldn't find total")
        print(" No total could be detected")
        return -1

    finalString = newString2[totalValueIndexStart+1:totalValueIndexEnd]
    finalString = re.sub("[^0-9,.]", "", finalString)

    cost = float(finalString)

    return cost

def changeImageSize(filepath, filename):
    img = cv.imread(filepath + "/" + filename, 3)
    height, width = img.shape[:2]
    newFileName = "receipt0"

    if width >= 1000: 
        resizeFactor = width/1000
        img = cv.resize(img, (int(width/resizeFactor), int(height/resizeFactor)))
        print("\tResized by a factor of " + str(resizeFactor))
        cv.imwrite(filepath + "/" + newFileName + ".jpg", img)
        return [True, newFileName]
    return [False, newFileName]

def runOCRAlgo(filepath, filename):
    cost = 0
    info = []
    for i in range(0, 1, 1):
        print("Processing image #" + str(i))
        info = changeImageSize(filepath, filename)
        if info[0] == True:
            print("\tresized")
            print(filepath + info[1])
            cost = getCost(filepath + info[1] + ".jpg")
        else:
            print("\tno resizing, continue as normal")
            cost = getCost(filepath + info[1] + ".jpg")       
    return float(cost)

def ignore():
    #client = contentful.Client('nbjulodyld5b', '_zUBn2ge9faOWwjv6gNybB6d6KxKAfalGmCdMjP3N3E')
    filename = "receipt"
    for i in range(0, 1, 1):
        print("Processing image #" + str(i))
        getCost(str(filename) + str(i) + ".jpg")



