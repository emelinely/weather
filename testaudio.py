import simpleaudio as sa



wav_obj1 = sa.WaveObject.from_wave_file('/home/pi/weather/sounds/rain.wav')
wav_obj2 = sa.WaveObject.from_wave_file('/home/pi/weather/sounds/clear.wav')
play_obj1 = wav_obj1.play()
play_obj2 = wav_obj2.play()
play_obj1.wait_done()
play_obj2.wait_done()

