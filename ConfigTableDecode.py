import os
import json
import sys
import importlib

from pathlib import Path
from google.protobuf import json_format
from binary import BinaryStream

def BytesFileEdit(inputDir, outputDir):
    ZERO_TABLE_LIST_FILE = './ZeroConfigTableList.txt'
    
    inputFilePath = ''.join([inputDir, 'Config.bytes'])

    inputFile = open(inputFilePath, "rb")
    stream = BinaryStream(inputFile)

    outputDir.mkdir(parents=True, exist_ok=True)

    tableNumber = stream.readUInt32()
    zeroTableList = []
    for i in range(tableNumber):
        tableBytesLength = stream.readUInt32()
        tableCount = stream.readUInt32()
        tableNameLength = stream.readUInt32()
        tableNameStringBytes = stream.readBytes(tableNameLength)

        restBytesLength = tableBytesLength - 8 - tableNameLength
        tableData = stream.readBytes(restBytesLength)        

        tableNameString = str(tableNameStringBytes, 'utf-8')

        if tableCount == 0:
            zeroTableList.append(tableNameString) 
        else:
            outputFileFullName = ''.join([outputDir, tableNameString, '.bytes'])

            outputFile = open(outputFileFullName, "wb")    
            tableBytes = BinaryStream(outputFile)

            tableBytes.writeUInt32(tableBytesLength)
            tableBytes.writeUInt32(tableCount)
            tableBytes.writeUInt32(tableNameLength)
            tableBytes.writeBytes(tableNameStringBytes)
            tableBytes.writeBytes(tableData)

            outputFile.close()

    inputFile.close()

    zeroTableListString = '\n'.join(zeroTableList)
    zeroTableListFile = open(ZERO_TABLE_LIST_FILE,'w+')
    zeroTableListFile.write(zeroTableListString)
    zeroTableListFile.close()


def BytesFileDecode(inputDir, outputDir):
    PB2_MODULE_DIR = 'ConfigTablePb2.'
    
    inputDir = Path(inputDir)
    outputDir = Path(outputDir)

    for inputRoot, _, files in os.walk(inputDir):
        inputRoot = Path(inputRoot)
        relativeDir = inputRoot.relative_to(inputDir)
        outputRoot = outputDir / relativeDir 
        outputRoot.mkdir(parents=True, exist_ok=True)

        for inputFileFullName in files:
            inputPath = inputRoot / inputFileFullName

            inputFile = open(inputPath, "rb")
            stream = BinaryStream(inputFile)
            tableBytesLength = stream.readUInt32()
            tableCount = stream.readUInt32()
            tableNameLength = stream.readUInt32()
            tableNameStringBytes = stream.readBytes(tableNameLength)

            pb2Dir = ''.join([PB2_MODULE_DIR, Path(inputFileFullName).stem, '_pb2'])
            table_pb2 = importlib.import_module(pb2Dir)
            protobufMessage = table_pb2.Cfg()
            jsonList = []

            for i in range(tableCount):
                protoBytesLength = stream.readUInt32()
                protoBytes = stream.readBytes(protoBytesLength)

                protobufMessage.ParseFromString(protoBytes)
                jsonList.append(json_format.MessageToDict(message=protobufMessage))

            inputFile.close()

            outputFileFullName = ''.join([Path(inputFileFullName).stem,".json"])
            outputPath = outputRoot / outputFileFullName

            outputFile = open(outputPath, "w+", encoding="utf-8") 
            jsonDict = {'Data':jsonList}   

            jsonString = json.dumps(jsonDict, indent=2, ensure_ascii=False)
            outputFile.write(jsonString)

            outputFile.close()


if __name__=="__main__":
    BytesFileEdit('./ConfigTable01Raw/assets/abresources/', './ConfigTable02Edit/')
    BytesFileDecode('./ConfigTable02Edit/', './ConfigTable03Decode/')