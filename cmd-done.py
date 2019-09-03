import subprocess
import tempfile

# cmd = "ffmpeg -i video.avi video.mp3"
cmd = "python --version"

with tempfile.TemporaryFile() as temp_file:
    proc = subprocess.Popen(cmd, stdout=temp_file)
    proc.wait()
    temp_file.seek(0)
    print (temp_file.read().decode("UTF-8"))
    print("+------+")
    print("| DONE |")
    print("+------+")