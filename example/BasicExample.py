from PictureTextCreator import GetPictureWithText

exampleText = "this is text added by 'PTC' to Y pixel 125."
outputPath = "./output.png"
exampleFontPath = "./Arial-BD.ttf" 
GetPictureWithText("./exampleTemplate.png",125,exampleText,exampleFontPath,outputPath)