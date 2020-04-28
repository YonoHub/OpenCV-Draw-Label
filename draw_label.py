'''
    Draw Label Block's source code
    Auther: Ahmed Hendawy - YonoHub Developer Advocate
    Date: 23.04.2020
'''

# Vision
import cv2
# Yonoarc Utils
from yonoarc_utils.image import from_ndarray, to_ndarray
from yonoarc_utils.header import set_timestamp
# Messages
from std_msgs.msg import Header

def write_classification(image,label):
        # Resize to have a clear label for small sized images
        aspect_ratio=image.shape[1]/image.shape[0]
        dim=(int(500 * aspect_ratio),int(500 * aspect_ratio)) #  Using 500 x 500 as a baseline
        resized_image=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
        print(resized_image.shape)
        top = int(0.08 * resized_image.shape[0])  # shape[0] = rows
        bottom = top
        left = int(0.08 * resized_image.shape[1])  # shape[1] = cols
        right = left
        borderType = cv2.BORDER_CONSTANT
        value = [0,0,0]
        
        output_image = cv2.copyMakeBorder(resized_image, top, bottom, left, right, borderType, None, value)
        output_image=cv2.putText(output_image,label.class_name,(right,int(output_image.shape[0]-bottom/2)), cv2.FONT_HERSHEY_SIMPLEX, ((output_image.shape[0]+output_image.shape[1])/1000),(255,255,255),2)

        return output_image

class draw_label:
    def on_new_messages(self,messages):
        labeled_image=write_classification(to_ndarray(messages['image']),messages['label'])
        self.publish("labeled_image",from_ndarray(labeled_image,messages['image'].header))
