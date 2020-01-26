import requests
import json
import cv2 as cv
import re

def ocr_space_file(filename, overlay=False, api_key='1940116e7488957', language='eng', ocrEngine = '1'):
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
               'OCREngine' : ocrEngine,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

def getCost(filename, ocrEngine):
    print("getting cost...")
    data = ocr_space_file(filename=filename, language='eng', ocrEngine = ocrEngine)
    detectedText = json.loads(data)
    #print(detectedText)
    finalCostTerms = ["total", "purchase", "acct"]

    try:
        parsedText = detectedText["ParsedResults"]
    except KeyError:
        print(" Could not detect values")
        return 0

    parsedText = parsedText[0]["ParsedText"]
    hstIndex = parsedText.rfind('HST')
    if hstIndex != -1:
        print("\t HST Detected")
        parsedText = parsedText[hstIndex:len(parsedText)]
    else:
        print("\t Couldn't find hst")
    
    for term in finalCostTerms:
        totalIndex = parsedText.lower().rfind(term)
        #totalIndex = parsedText.rfind("TOTAL")

        if totalIndex != -1:
            print("\t Found total index position")
            newString2 = parsedText[totalIndex:len(parsedText)]
            totalValueIndexEnd = newString2.find("\n")
            totalValueIndexStart = newString2.find("\t")
            break
        elif term == "acct":
            print("\t Couldn't find total")
            print(" No total could be detected")
            return -1

    print("\tDone OCR Interfacing")
    finalString = newString2[totalValueIndexStart+1:totalValueIndexEnd]
    finalString = re.sub("[^0-9,.]", "", finalString)
    
    if len(finalString) != 0 and len(finalString) < 6:
        if finalString.find(".") == -1:
            finalString = finalString[0:len(finalString)-2] + "." + finalString[len(finalString)-2:len(finalString)]
        cost = float(finalString)
        return cost
    else:
        print(" Failed to detect cost")
        return -1
    return cost

def changeImageSize(filepath, filename, filenumber):
    img = cv.imread(filepath + "/" + filename, 3)
    height, width = img.shape[:2]
    newFileName = "receipt" + str(filenumber)

    if width >= 1000: 
        resizeFactor = width/1000
        img = cv.resize(img, (int(width/resizeFactor), int(height/resizeFactor)))
        print("\tResized by a factor of " + str(resizeFactor))
        cv.imwrite(filepath + "/" + newFileName + ".jpg", img)
        return [True, newFileName]
    return [False, newFileName]

def runOCRAlgo(filepath, filename, filenumber):
    cost = 0
    info = []
    fileName = ""
    for i in range(0, 1, 1):
        print("Processing image #" + str(i))
        info = changeImageSize(filepath, filename, filenumber)
        if info[0] == True:
            print("\tresized")
            print(filepath + info[1])
            cost = getCost(filepath + info[1] + ".jpg", ocrEngine = 1)
            if cost == -1:
                cost = getCost(filepath + info[1] + ".jpg", ocrEngine = 2)
        else:
            print("\tno resizing, continue as normal")
            cost = getCost(filepath + info[1] + ".jpg", ocrEngine = 1)   
            if cost == -1:
                cost = getCost(filepath + info[1] + ".jpg", ocrEngine = 2)   
    print("OCR Algo complete")   
    return float(cost), info[1]

