python container.py | \
ffmpeg -y \
    -re \
    -r 30 \
    -hwaccel cuda -hwaccel_output_format cuda \
    -f rawvideo \
    -pix_fmt bgr24 \
    -s 640x480 \
    -i - \
    -c:v h264_nvenc \
    -preset p6 \
    -tune ull \
    -f hls \
    -hls_time 1 \
    -hls_list_size 10 \
    -hls_flags delete_segments \
    -zerolatency 1 \
    -r 30 \
    -g 30 \
    /dev/shm/hls/live.m3u8