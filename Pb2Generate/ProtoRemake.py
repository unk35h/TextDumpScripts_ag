import os
from pathlib import Path

def ProtoRemake(inputDir, outputDir):
    inputDir = Path(inputDir)
    outputDir = Path(outputDir)
    HEADER = 'proto3'

    for inputRoot, _, files in os.walk(inputDir):
        inputRoot = Path(inputRoot)
        relativeDir = inputRoot.relative_to(inputDir)
        outputRoot = outputDir / relativeDir 
        outputRoot.mkdir(parents=True, exist_ok=True)

        for inputFileFullName in files:
            if inputFileFullName == 'table.proto':
                inputPath = inputRoot / inputFileFullName
                packageName = str(relativeDir)
                outputFileFullName = ''.join([packageName, '.proto'])
                outputPath = ''.join([outputDir, outputFileFullName])

                
                with open(inputPath, 'r') as f:
                    fileRawString = f.read()              
                    position = fileRawString.find(HEADER)
                    fileString = ''.join([fileRawString[:position+8], '\n\n', 'package ', packageName, ';', fileRawString[position+8:]])

                #with open(outputPath,'wb') as f:
                with open(outputPath,'w+') as f:
                    f.write(fileString)


if __name__=="__main__":
    ProtoRemake('./proto/', './proto/')