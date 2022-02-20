from keras.models import load_model
import pickle
import cv2
import os
from PIL import Image


class Captcha:
    def __init__(self):
        self.predicted_captcha = list()
        pass

    def crop_captcha(self, path_name):
        img = Image.open(path_name)
        area1=(27,0,51,37)
        img1 = img.crop(area1)

        area2=(51,0,70,37)
        img2 = img.crop(area2)

        area3=(68,0,86,37)
        img3 = img.crop(area3)

        area4=(86,0,102,37) #
        img4 = img.crop(area4)

        area5=(102,0,123,37)
        img5 = img.crop(area5)

        img1.save("11"+".jpg")
        img2.save("22"+".jpg")
        img3.save("33"+".jpg")
        img4.save("44"+".jpg")
        img5.save("55"+".jpg")

    def prescript(self, file):
        image = cv2.imread(file)
        output = image.copy()
        image = cv2.resize(image, (16, 37))


        image = image.astype("float") / 255.0


        if 1 > 0:
            image = image.flatten()
            image = image.reshape((1, image.shape[0]))


        else:
            image = image.reshape((1, image.shape[0], image.shape[1],
            image.shape[2]))


        model = load_model('./simple_nn.model')
        lb = pickle.loads(open('simple_nn_lb.pickle', "rb").read())

        preds = model.predict(image)

        i = preds.argmax(axis=1)[0]
        label = lb.classes_[i]

        text = "{}: {:.2f}%".format(label, preds[0][i] * 100)
        self.predicted_captcha.append(text[0])



    def run_predict(self):
        self.prescript("11.jpg")
        self.prescript("22.jpg")
        self.prescript("33.jpg")
        self.prescript("44.jpg")
        self.prescript("55.jpg")

        solved_captcha: str = ''.join(self.predicted_captcha)

        return solved_captcha

    def delete_croped_image(self):
        os.remove("11.jpg")
        os.remove("22.jpg")
        os.remove("33.jpg")
        os.remove("44.jpg")
        os.remove("55.jpg")
