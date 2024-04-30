cc_binary(
    name = "app",
    srcs = ["app.cpp"],
    deps = [
        "//server/core:img_processor_lib"
    ],
    linkstatic = False,
    copts = ["-I/usr/local/include/opencv4"],
    linkopts = [
        "-L/usr/local/lib",
        "-lopencv_core",
        "-lopencv_imgcodecs",
    ],
)
