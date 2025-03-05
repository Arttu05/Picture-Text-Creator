# Picture-Text-Creator
Simple python library, used to create pictures with given text from template picture.
This project uses pillow and textwrap.

# how to install 

```
pip install PictureTextCreator==0.3.0
```

## Arguments

### templatePath

path to the template picture

### textCordinate

at what pixel height (top to bottom) the text will be inserted

### textToAdd 

The text that gets inserted to the final image

### fontPath

Path to some ```.tff``` font file

### outputPath

Path where the final image will be saved. 

**note** outputPath must contain the image format extension, for example ```.png```

### textColor

Color of the text that will be inserted. Should be given as RGB tuple. 

By default this has a value of (0,0,0)

### backgroundColor

Color behind the  inseted text. Should be given the same way as ```textColor```.

By default this has a value of (255,255,255)

### fontSize

Size of the font.

By default this has a value of 45

### textWrapValue 

This value changes when text "wraps"/starts a new row based on the character count. For more info https://docs.python.org/3/library/textwrap.html.

By default this has a value of 39

### leftSideMargin

This value determines many pixels away the text will be inserted from the left side.

By default this has a value of 42

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

Tested with python 3.12.2 and pillow 10.4.0
