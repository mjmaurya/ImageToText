try:
    from PIL import Image
except ImportError:
    import Image
from PIL import ImageEnhance
import pytesseract
from io import BytesIO
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    print(filename)
    print(str(filename))
    xyz=str(filename).split(" ")[1].split(".")
    ima=Image.open(filename)
    image=Image.open(filename)
    print(xyz[len(xyz)-1].replace("'",""))
    if xyz[len(xyz)-1].replace("'","")=="png":
        print("MAnoj sir")
        with BytesIO() as f:
            ima.save(f, format='JPEG')
            ima_jpg = ima.convert('RGB')
            image = Image.open(ima_jpg)
    try:
        text = pytesseract.image_to_string(image,lang="eng+hin") 
        return text
    except Exception as ex:
        return ex
