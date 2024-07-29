import subprocess


class AudioRecording:
    import subprocess

    def recording(self, url, time, file_name='test', format='aac'):  # time format > '00:01:00'
        command = [
            'ffmpeg',
            '-i', url,
            '-vn',
            '-acodec', 'copy',
            '-t', time,
            f'{file_name}.{format}'
        ]
        print(f"Running command: {' '.join(command)}")
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("Audio yozib olish boshlandi!")
            print(result.stdout.decode())
            print(result.stderr.decode())
        except subprocess.CalledProcessError as e:
            print(f"Audio yozib olishda xatolik yuz berdi: {e}")
            print(e.stderr.decode())
        except FileNotFoundError as e:
            print(f"ffmpeg topilmadi: {e}")
        except Exception as e:
            print(f"Yozib olishda kutilmagan xatolik yuz berdi: {e}")

    def change_format(self, new_format, audio):
        command = [
            'ffmpeg',
            '-i', audio,
            '-acodec', 'libmp3lame',
            f"{audio.split('.')[0]}.{new_format}"
        ]
        try:
            subprocess.run(command, check=True)
            print("Format uzgartirildi !")
        except subprocess.CalledProcessError as e:
            print(f"Formatni uzgartirishda xatolik yuz berdi: {e}")

    def filter_audio(self, audio, file_name):
        command = [
            'ffmpeg',
            '-i', audio,
            '-af', 'silenceremove=stop_periods=-1:stop_duration=0.5:stop_threshold=-30dB',
            file_name
        ]
        subprocess.run(command, check=True)


url = ('rtsp://admin:UNAHTY@''impactt1.max.uz:10553/Streaming/Channels/102')

obj = AudioRecording()
# obj.recording('rtsp://admin:UNAHTY@impactt1.max.uz:10553/Streaming/Channels/102', time='00:00:10')
obj.change_format('mp3', 'test.aac')
