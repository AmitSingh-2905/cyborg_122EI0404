import numpy as np
import cv2
img=255*np.ones([600,750,4],np.uint8)
# for 1
img=cv2.rectangle(img,(230,320),(320,410),(164,154,14),-1)
img=cv2.circle(img,(275,365),8,(255,255,255),-1)

# for 5
img=cv2.rectangle(img,(230,230),(320,320),(7,65,202),-1)
img=cv2.circle(img,(275,275),8,(255,255,255),-1)
img=cv2.circle(img,(250,250),8,(255,255,255),-1)
img=cv2.circle(img,(250,300),8,(255,255,255),-1)
img=cv2.circle(img,(300,300),8,(255,255,255),-1)
img=cv2.circle(img,(300,250),8,(255,255,255),-1)
# img=cv2.line(img,(230,230),(320,230),(255,255,255),5)

#for 6
img=cv2.rectangle(img,(230,140),(320,230),(0,153,255),-1)
img=cv2.circle(img,(250,160),8,(255,255,255),-1)
img=cv2.circle(img,(275,160),8,(255,255,255),-1)
img=cv2.circle(img,(300,160),8,(255,255,255),-1)
img=cv2.circle(img,(250,210),8,(255,255,255),-1)
img=cv2.circle(img,(275,210),8,(255,255,255),-1)
img=cv2.circle(img,(300,210),8,(255,255,255),-1)


#for 3
img=cv2.rectangle(img,(320,230),(410,320),(169,47,82),-1)
img=cv2.circle(img,(340,300),8,(255,255,255),-1)
img=cv2.circle(img,(365,275),8,(255,255,255),-1)
img=cv2.circle(img,(390,250),8,(255,255,255),-1)

#for 2
img=cv2.rectangle(img,(410,230),(500,320),(224,138,56),-1)
img=cv2.circle(img,(430,300),8,(255,255,255),-1)
img=cv2.circle(img,(480,250),8,(255,255,255),-1)

#for 4
img=cv2.rectangle(img,(230,230),(140,320),(95,39,161),-1)
img=cv2.circle(img,(160,250),8,(255,255,255),-1)
img=cv2.circle(img,(160,300),8,(255,255,255),-1)
img=cv2.circle(img,(210,250),8,(255,255,255),-1)
img=cv2.circle(img,(210,300),8,(255,255,255),-1)
# spacing
img=cv2.line(img,(140,230),(500,230),(255,255,255),2)
img=cv2.line(img,(140,320),(500,320),(255,255,255),2)
img=cv2.line(img,(230,140),(230,410),(255,255,255),2)
img=cv2.line(img,(320,140),(320,410),(255,255,255),2)
img=cv2.line(img,(410,230),(410,320),(255,255,255),2)
font=cv2.FONT_ITALIC
img=cv2.putText(img,"Amit Prasad Singh",(440,500),font,1,(1,1,1),2)
img=cv2.putText(img,"122EI0404",(440,530),font,1,(1,1,1),2)
img=cv2.putText(img,cv2.__version__,(440,560),font,1,(1,1,1),2)




output_med=cv2.medianBlur(img,3)


cv2.imshow("Image",output_med)

cv2.waitKey(0)