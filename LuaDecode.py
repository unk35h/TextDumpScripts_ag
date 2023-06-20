import os
from ljd.tools import set_luajit_version, process_file, process_folder
from pathlib import Path


def BytesFileEdit(inputDir, outputDir):
    inputDir = Path(inputDir)
    outputDir = Path(outputDir)
    HEADER = b'\x1B\x4C\x4A'

    for inputRoot, _, files in os.walk(inputDir):
        inputRoot = Path(inputRoot)
        relativeDir = inputRoot.relative_to(inputDir)
        outputRoot = outputDir / relativeDir 
        outputRoot.mkdir(parents=True, exist_ok=True)

        for inputFileFullName in files:
            inputPath = inputRoot / inputFileFullName

            with open(inputPath, 'rb') as f:
                fileRawByte = f.read()
                position = fileRawByte.find(HEADER)
                fileByte = fileRawByte[position:]
                fileByte = fileByte.rstrip(b'\x00')

            outputFileFullName = Path(inputFileFullName).stem
            outputPath = outputRoot / outputFileFullName

            with open(outputPath, 'wb') as f:
                f.write(fileByte)


if __name__=="__main__":
    BytesFileEdit('./Lua01Raw/', './Lua02Edit/')
    set_luajit_version(21)
    process_folder('./Lua02Edit/', './Lua03Decode/')