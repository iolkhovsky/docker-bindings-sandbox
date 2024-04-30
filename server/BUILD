cc_binary(
    name = "blur_image",
    srcs = ["test_app.cpp"],
    copts = ["-I/usr/local/include/opencv4"],
    linkopts = [
        "-L/usr/local/lib",
        "-lopencv_core",
        "-lopencv_imgproc",
        "-lopencv_imgcodecs",
    ],
)
