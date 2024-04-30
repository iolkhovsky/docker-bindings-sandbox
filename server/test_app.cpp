#include <string>
#include <iostream>

#include <opencv2/opencv.hpp>


int main(int argc, char **argv) {
    std::string input_path(argv[1]);
    std::cout << "Input image path: " << input_path << std::endl;
    std::string output_path(argv[2]);
    std::cout << "Output image path: " << output_path << std::endl;

    cv::Mat image = cv::imread(input_path.c_str(), cv::IMREAD_COLOR);
    if (image.empty()) {
        std::cerr << "Could not read the image." << std::endl;
        return 1;
    }

    cv::Mat blurredImage;
    cv::GaussianBlur(image, blurredImage, cv::Size(31, 31), 5.0);

    cv::imwrite(output_path.c_str(), blurredImage);

    return 0;
}
