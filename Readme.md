Some simple scripts to extract some text resources from Aether Gazer, which is used for the repository gamedata_ag.

This project uses https://gitlab.com/RazTools/Studio to get raw files from the game.

Notes:

1.Because the lua content and config table content are not in fixed asset files, you have to put all asset files to RawAsset document.

2.The running codes of whole progress is in WholeWork.txt. You have to edit it before using.

3.The structs of Protobuf Message for Table data are in Pb2Generate\proto. All struct are manually writen throught reading dump.cs from il2cppDumper.

4.This project use https://github.com/AzurLaneTools/ljd to decode lua codes.
