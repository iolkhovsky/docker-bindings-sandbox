cc_binary(
    name = "app",
    srcs = ["app.cpp"],
    deps = [
        ":img_processor_lib",
    ],
    linkstatic = False,
    copts = ["-I/usr/local/include/opencv4"],
    linkopts = [
        "-L/usr/local/lib",
        "-lopencv_core",
        "-lopencv_imgcodecs",
    ],
)

cc_library(
    name = "img_processor_lib",
    srcs = [],
    hdrs = [],
    visibility = ["//visibility:private"],
    deps = [
        "//server/core:img_processor_lib"
    ],
)
