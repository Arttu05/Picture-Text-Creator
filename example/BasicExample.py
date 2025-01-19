from ..src import PTC

exampleText = "this is text added by 'PTC' to Y pixel 125."
outputPath = "./output.png"
exampleFontPath = "./Arial-BD.ttf" 
PTC.GetPictureWithText("./exampleTemplate.png",125,exampleText,exampleFontPath,outputPath)