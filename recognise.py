from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from scipy import misc
import os
import tensorflow as tf
import numpy as np
from align import detect_face,facenet
import random
import pickle
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.svm import SVC
import classify

facenet_image_size=160
image_size=182
margin=44
random_orderction='store_true'
gpu_memory_fraction=1.0
detect_multiple_faces=True
model_path='models/policy/embeding.pb'
classifier_filename='models/policy/svm_classifier.pkl'
batch_size=90
facenet_image_size=160


count_rightpic=0
CLASS_PROBABILITY_THRESHOLD=0.2           #设置阈值准确度，否则识别为unknown
def faceRecognise(image_path):
    classifier_filename_exp = os.path.expanduser(classifier_filename)
    with open(classifier_filename_exp, 'rb') as infile:
        (model, class_names) = pickle.load(infile)
    img = mpimg.imread(image_path)
    images ,bounding_boxes= load_and_align_data(image_path, image_size, margin, gpu_memory_fraction)
    # Get input and output tensors
    with tf.Graph().as_default():
        with tf.Session() as sess:
           # Load the model
            facenet.load_model(model_path)

            # Get input and output tensors
            images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
            embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
            phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
                    
            predictions=[]
                    # Run forward pass to calculate embeddings
            for image in images:
                 feed_dict = {images_placeholder: [np.array(image)], phase_train_placeholder: False}
                 emb_datas = sess.run(embeddings, feed_dict=feed_dict)

              #   prediction = model.predict(emb_datas)    #预测结果
               #  predictions.append(class_names[prediction[0]])  

                 prediction = model.predict(emb_datas)
                 predict_proba=model.predict_proba(emb_datas)

                 best_class_indice = np.argmax(predict_proba, axis=1)
                 best_class_probability = predict_proba[np.arange(len(best_class_indice)), best_class_indice]
                 print(len(best_class_indice))
                 for i in range(len(best_class_indice)):
                     class_name = class_names[best_class_indice[i]]
                     class_probability = best_class_probability[i]
                     if class_probability < CLASS_PROBABILITY_THRESHOLD:
                         prediction = "unknown"
                     else:
                         prediction=class_name
                         break
                     print(prediction)
                 predictions.append(prediction)

            nrof_faces = bounding_boxes.shape[0]  # number of faces
            print("nrof_faces:%d"%nrof_faces)
            #遍历每个人脸检测框
            for i,face_position in enumerate(bounding_boxes):
                face_position = face_position.astype(int)
                print("face_position：")
                print(face_position)
                
                # cv2.putText在图片上添加水印
                cv2.rectangle(img, (face_position[0],face_position[1]),(face_position[2], face_position[3]),(0, 255, 0), 1)

                cv2.putText(img, predictions[i], (face_position[0] + 5, face_position[1] + 10),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8, (255, 0 ,0),thickness = 2, lineType = 1)

            # show result
            img = cv2.resize(img, (640, 480), interpolation=cv2.INTER_CUBIC)
            
            results=""
            for prediction in predictions:
                results +=prediction+" "+classify.classify(prediction)+" "
 
            return results,img



def load_and_align_data(image_path, image_size, margin, gpu_memory_fraction):

    minsize = 20 # minimum size of face
    threshold = [ 0.6, 0.7, 0.7 ]  # three steps's threshold
    factor = 0.709 # scale factor
    
    print('Creating networks and loading parameters')
    with tf.Graph().as_default():
        gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=gpu_memory_fraction)
        sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
        with sess.as_default():
            pnet, rnet, onet = detect_face.create_mtcnn(sess, None)

    img_list = []
    img = misc.imread(os.path.expanduser(image_path), mode='RGB')
    img_size = np.asarray(img.shape)[0:2]
    bounding_boxes, _ = detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)

    if len(bounding_boxes) < 1:
        #image_paths.remove(image)
        print("can't detect face, remove ", image_path)
    else:
        for bounding_box in bounding_boxes:
            det = np.squeeze(bounding_box)
            bb = np.zeros(4, dtype=np.int32)
            bb[0] = np.maximum(det[0]-margin/2, 0)
            bb[1] = np.maximum(det[1]-margin/2, 0)
            bb[2] = np.minimum(det[2]+margin/2, img_size[1])
            bb[3] = np.minimum(det[3]+margin/2, img_size[0])
            cropped = img[bb[1]:bb[3],bb[0]:bb[2],:]
            aligned = misc.imresize(cropped, (image_size, image_size), interp='bilinear')
            prewhitened = facenet.prewhiten(aligned)
            img_list.append(prewhitened)
    return img_list,bounding_boxes

