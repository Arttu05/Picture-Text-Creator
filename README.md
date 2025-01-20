# Picture-Text-Creator
Simple python library, used to create pictures with given text from template picture.
This project uses pillow and textwrap.

# how to install 

```
pip install PictureTextCreator==0.1
```

# Example

Create **output.png** with following code and **exampleTemplate.png** 

**BasicExample.py**
```
from PictureTextCreator import GetPictureWithText

exampleText = "this is text added by 'PTC' to Y pixel 125."
outputPath = "./output.png"
exampleFontPath = "./Arial-BD.ttf" 
GetPictureWithText("./exampleTemplate.png",125,exampleText,exampleFontPath,outputPath)
```

**exampleTemplate.png**

![Template picture](https://raw.githubusercontent.com/Arttu05/Picture-Text-Creator/refs/heads/main/example/exampleTemplate.png)

**output.png**

![output picture](https://raw.githubusercontent.com/Arttu05/Picture-Text-Creator/refs/heads/main/example/output.png)

# Note
Tested with python 2.9.0 and pillow 9.3.0
