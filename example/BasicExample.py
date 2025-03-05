from PictureTextCreator import GetPictureWithText

exampleText = "this is text added by 'PTC' to Y pixel 125."
outputPath = "./output.png"
exampleFontPath = "./Arial-BD.ttf" 
wrapValue = 35
GetPictureWithText("./exampleTemplate.png", 125, exampleText, exampleFontPath, outputPath, textWrapValue=wrapValue)

outputPath2 = "output with all values.png"
exampleText2 = "this text was added with 'PTC' to Y pixel 125, with leftSideMargin as 10, so this text is 10 pixels away from left side"

GetPictureWithText("./exampleTemplate.png", 125, exampleText2, exampleFontPath, outputPath2, textWrapValue=wrapValue, leftSideMargin=10)