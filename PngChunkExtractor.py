IMG_PATH = 'Images\media_wallpaper_1.png'

def loadPNG(imagePath):
    loadedImage = open(imagePath,mode='rb')
    return loadedImage

def extractHeader(image):
    header = image.read(8)
    return header

def extractNextChunk(image):
    #This function assumes you are at the start of a PNG chunk,
    #extracts its length, type, data, and crc,
    #and moves the cursor to the end of the chunk
    chunkLength = int.from_bytes(image.read(4),"big")
    chunkType = image.read(4)
    chunkData = image.read(chunkLength)
    chunkCRC = image.read(4)
    print("data size: "+str(chunkLength))
    print("chunk type: "+str(chunkType))
    print("chunk data: "+str(chunkData))
    print("CRC: "+str(chunkCRC))
    return (chunkLength,chunkType,chunkData,chunkCRC)
    
myPNG = loadPNG(IMG_PATH)
print(extractHeader(myPNG))
cursorPos = 8
while(myPNG.read(1)):
    myPNG.seek(cursorPos)
    myChunk = extractNextChunk(myPNG)
    outFile = open(str(myChunk[1]) + "_data.txt",'w')
    print(myChunk[2],file=outFile)
    outFile.close()
    cursorPos += 12 + myChunk[0]
    print(cursorPos)
    
