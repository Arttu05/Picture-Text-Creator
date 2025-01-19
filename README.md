# Picture-Text-Creator
Simple python library, used to create pictures with given text from template picture.
This project uses pillow and textwrap.

# Example

Create **output.png** with following code and **exampleTemplate.png** 
```
from src import PTC

exampleText = "this is text added by 'PTC' to Y pixel 125."
outputPath = "./output.png"
exampleFontPath = "./Arial-BD.ttf" 
PTC.GetPictureWithText("./exampleTemplate.png",125,exampleText,exampleFontPath,outputPath, textWrapValue=35)
```

**exampleTemplate.png**

![Template picture](https://raw.githubusercontent.com/Arttu05/Picture-Text-Creator/refs/heads/main/exampleTemplate.png)

**output.png**

![output picture](https://raw.githubusercontent.com/Arttu05/Picture-Text-Creator/refs/heads/main/output.png)

# Note
Tested with python 2.9.0 and pillow 9.3.0
