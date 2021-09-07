import cv2

faceCascade = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')

def face_detection(image_path):
    image = cv2.imread(image_path)
    image_gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # print('image_gray_scale', image_gray_scale)
    faces = faceCascade.detectMultiScale(image_gray_scale, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))
    # print('faces', faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = image_gray_scale[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
    filename = "output/grey.jpg"
    # saving the image
    cv2.imwrite(filename, roi_gray)
    # print("done")
    return "done"

def similarity_check(image1, image2):
    image1 = cv2.imread(image1)
    histogram1 = cv2.calcHist([image1], [0],None, [256], [0, 256])
    # print('histogram1', len(histogram1))
    image2 = cv2.imread(image2)
    histogram2 = cv2.calcHist([image2], [0],None, [256], [0, 256])
    # print('histogram2', len(histogram2))
    d = cv2.compareHist(histogram1, histogram2, cv2.HISTCMP_CORREL)
    # d = cv.CompareHist(histogram1, histogram1, CV_HISTCMP_CORREL)
    # compareHist( hist_base, hist_base, CV_COMP_CORREL)
    if d < 0.8:
        return "matched"
    else:
        return "not matched"
    # METHOD #1: UTILIZING OPENCV
    # initialize OpenCV methods for histogram comparison
    # OPENCV_METHODS = (
    #     ("Correlation", cv2.HISTCMP_CORREL),
    #     ("Chi-Squared", cv2.HISTCMP_CHISQR),
    #     ("Intersection", cv2.HISTCMP_INTERSECT),
    #     ("Hellinger", cv2.HISTCMP_BHATTACHARYYA))
    # # loop over the comparison methods
    # for (methodName, method) in OPENCV_METHODS:
    #     # initialize the results dictionary and the sort
    #     # direction
    #     results = {}
    #     reverse = False
    #     # if we are using the correlation or intersection
    #     # method, then sort the results in reverse order
    #     if methodName in ("Correlation", "Intersection"):
    #         reverse = True
    #         	# loop over the index
    #     for (k, hist) in index.items():
    #         # compute the distance between the two histograms
    #         # using the method and update the results dictionary
    #         d = cv2.compareHist(index["doge.png"], hist, method)
    #         results[k] = d
    #     # sort the results
    #     results = sorted([(v, k) for (k, v) in results.items()], reverse = reverse)

    # print("result", results)



# def sim(image1, image2):
#     CV_COMP_CORREL
#     compareHist( hist_base, hist_base, CV_COMP_CORREL)
#     cv2.resize(image1, dim, interpolation = cv2.INTER_AREA)
#     image1 = cv2.imread(image1)
#     image2 = cv2.imread(image2)
#     s = ssim(image1, image2) 
#     print("similarity", s)


image_path = 'data/katrina.jpg'
image_path1 = 'data/micheal.jpeg'
# cv2.normalize(histogram1, histogram2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

# face_detection(image_path)
# face_detection(image_path1)

image1 = 'output/grey.jpg'
image2 = 'output/grey1.jpg'

similarity_check(image1, image2)