#include <boost/python.hpp>
#include <boost/python/numpy.hpp>
#include <opencv2/opencv.hpp>

#include "core/img_processor.hpp"

namespace bp = boost::python;
namespace np = boost::python::numpy;

char const* py_about() {
   return "img processor lib";
}

cv::Mat array_to_mat(const np::ndarray& array) {
    int rows = bp::extract<int>(array.attr("shape")[0]);
    int cols = bp::extract<int>(array.attr("shape")[1]);
    int channels = bp::extract<int>(array.attr("shape")[2]);

    cv::Mat result(rows, cols, CV_8UC(channels));
    std::memcpy(result.data, array.get_data(), rows * cols * channels * sizeof(uint8_t));
    return result;
}

np::ndarray mat_to_array(const cv::Mat& mat) {
    np::dtype dt = np::dtype::get_builtin<uint8_t>();
    bp::tuple shape = bp::make_tuple(mat.rows, mat.cols, mat.channels());
    np::ndarray array = np::zeros(shape, dt);
    std::memcpy(array.get_data(), mat.data, mat.rows * mat.cols * mat.channels() * sizeof(uint8_t));
    return array;
}

np::ndarray py_blur(const np::ndarray& input_array) {
    auto input_mat = array_to_mat(input_array);
    cv::Mat output_mat = img_processor::blur(input_mat);
    return mat_to_array(output_mat);
}

BOOST_PYTHON_MODULE(img_proc_lib) {
    using namespace boost::python;

    Py_Initialize();
    np::initialize();

    def("blur", py_blur);
    def("about", py_about);
}
