import speedtest


test = speedtest.Speedtest()

downloaded = test.download()
upload = test.upload()




print(f"Download Speed: {downloaded} \n Upload speed: {upload}")

