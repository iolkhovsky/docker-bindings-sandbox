cc_library(
    name = "img_processor_lib",
    srcs = [
        "img_processor.cpp",
    ],
    hdrs = [
        "img_processor.hpp",
    ],
    visibility = [
        "//visibility:public",
    ],
    copts = ["-I/usr/local/include/opencv4"],
    linkopts = [
        "-L/usr/local/lib",
        "-lopencv_core",
        "-lopencv_imgproc",
    ],
)
