import cv2
import img_proc_lib as proc


if __name__ == '__main__':
    img = cv2.imread('/repos/sandbox/lenna.jpg')
    result = proc.blur(img)
    cv2.imwrite('/repos/sandbox/output2.jpg', result)
