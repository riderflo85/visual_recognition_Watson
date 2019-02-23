#! /usr/env python3
# conding: utf-8

import json
import os
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    version = '2018-03-19',
    iam_apikey = 'sRbpnBe1LY_z9q0xNU4LVF1VxqYciJsv1avlLESc9yEy'
)

directory = os.path.dirname(__file__)
folder = "ressources"

item = os.path.join(directory, folder, 'test5.jpg')
food = os.path.join(directory, folder, 'food1.jpg')
face = os.path.join(directory, folder, 'face_test.jpg')

def reco_item_default():

    with open(item, 'rb') as image:
        classify = visual_recognition.classify(
            images_file = image,
            accept_language = 'fr',
            classifier_ids = ["default"]).get_result()
    result = json.dumps(classify, indent=2, ensure_ascii=False)
    print(result)

def reco_item_food():

    with open(food, 'rb') as image:
        classify = visual_recognition.classify(
            images_file = image,
            accept_language = 'fr',
            classifier_ids = ['food']).get_result()
    result = json.dumps(classify, indent=2, ensure_ascii=False)
    print(result)

def reco_face():

    with open(face, 'rb') as image:
        faces = visual_recognition.detect_faces(
            images_file = image,
            accept_language = 'fr').get_result()
    result = json.dumps(faces, indent=2, ensure_ascii=False)
    print(result)


def main():

    reco_item_default()

main()