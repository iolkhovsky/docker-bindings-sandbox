#include "img_processor.hpp"

#include <opencv2/opencv.hpp>

namespace img_processor {

cv::Mat blur(const cv::Mat& input) {
    cv::Mat output;
    cv::GaussianBlur(input, output, cv::Size(31, 31), 5.0);
    return output;
}

}  // namespace img_processor
