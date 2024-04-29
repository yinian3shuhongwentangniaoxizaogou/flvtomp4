import ffmpeg

def convert_video(input_file, output_file):
    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_file, vcodec='h264_nvenc', preset='fast')
            .run()
        )
        print("转换成功！文件保存在：", output_file)
    except ffmpeg.Error as e:
        print("转换失败：", e)

# 调用函数
convert_video('06.试卷解析u0026计算机网络强化结课总结.flv', '06.试卷解析u0026计算机网络强化结课总结.mp4')
convert_video('结课直播（读写者问题在这里）.flv', '结课直播（读写者问题在这里）.mp4')
