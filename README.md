**![SPM is supported](https://img.shields.io/badge/education-Experience_meeting-orange)**

# Experience_meeting

# Overview
ソフト班体験会用

# Description

## [src](https://github.com/Happy-wada/Experience_meeting/tree/main/src)
- ### [Keyboard_Control.py ](https://github.com/Happy-wada/Experience_meeting/blob/main/src/Keyboard_Control.py)
  >キーボドで走らせるプログラム ラジコンもどき  
  
- ### [Keyboard_Control1.py](https://github.com/Happy-wada/Experience_meeting/blob/main/src/Keyboard_Control1.py)
  >キーボドで走らせるプログラム(gazebo) ラジコンもどき  
 
class FeatureFromRecog():
    def __init__(self):
        # Service
        #self.height_srv = rospy.ServiceProxy('/person_feature/height_estimation', SetFloat)
        #服
        self.cloth_srv  = rospy.ServiceProxy('/person_feature/cloth_color', SetStr)
        #ズボン
        self.pants_srv = rospy.ServiceProxy('/person_feature/pants_color', SetStr)
        #顔
        self.skin_srv = rospy.ServiceProxy('/person_feature/skin_color', SetStr)
        #髪
        #self.hair_srv = rospy.ServiceProxy('/person_feature/hair_color', SetStr)
        # Value
        self.height      = "null"
        self.cloth_color = "null"
        self.skin_color = "null"
        self.pants_color = "null"
        #selk.hair_color = "null"
        self.mask ="null"
        #Topic
        #self.head_pub = rospy.Publisher('/servo/head', Float64, queue_size = 1)
        #self.bc = BaseControl()
    
    def getPansColor(self):
        self.pants_color = "null"
        self.pants_color = self.pants_srv().result
        
        if self.pants_color == '':
            return "none"

        else:
            return self.pants_color


    def getSkinColor(self):
        self.skin_color = "null"
        self.skin_color =  self.skin_srv().result
        
        if self.skin_color == '':
            return "none"
    #    else if self.skin_color == 'white':
    #        self.mask = "mask"
    #        return "none"
        
        else:
            return self.skin_color
    
    def getMask(self):
        self.mask = "null"
        self.mask = self.skin_srv().result

        if self.skin_color == 'white':
            self.mask = "wearing a mask"
            return "none"
        else:
            self.mask = "not wearing a mask"


    def getHairColo(self):
        self.hair_color = "null"
        self.hair_color = self.hair_srv().result
        if self.hair_color == '':
            return "none"
        else:
            return self.hair_color


    #def getHeight(self):
    #    self.head_pub.publish(0)
    #    self.base_control.translateDist(-0.5,0.2)
    #    
    #     height = SetFloat()
    #    height = self.height_srv()
    #    
    #    if height.data == -1:
    #        return False
    #    else:
    #        self.height = str(round(height.data))
    #        return self.height

    def getClothColor(self):
        self.cloth_color = "null"
        self.cloth_color = self.cloth_srv().result
        if self.cloth_color == '':
            return "none"
        else:
            return self.cloth_color
