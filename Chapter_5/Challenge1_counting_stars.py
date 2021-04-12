import cv2

img1 = cv2.imread('5_no_transient_left.png', cv2.IMREAD_GRAYSCALE)

## threshold
th, threshed = cv2.threshold(img1, 1, 255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)

## show plots
cv2.imshow( 'original',img1)
cv2.waitKey(2500)
cv2.imshow( 'Apply threshold',threshed)
cv2.waitKey(2500)

## findcontours
cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]

## min area; max area
#min_area = 1000
#max_area = 1
#for cnt in cnts:
#    area = cv2.contourArea(cnt)
#    if area < min_area:
#        min_area = area
#    if area > max_area:
#        max_area = area
        
max_area = max(map(cv2.contourArea,cnts)) #60
min_area = min(map(cv2.contourArea,cnts)) #0

## filter by area
s1 = 0.1
s2 = max_area
xcnts = []
for cnt in cnts:
    area = cv2.contourArea(cnt)
    if s1 <= area <= s2:
        xcnts.append(cnt)

print("Dots number: {}".format(len(xcnts)))
#Dots number: 726

