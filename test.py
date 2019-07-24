from shotdetect import shotDetector

vid = "./test.mp4"
detector = shotDetector(vid)
detector.run()
detector.pick_frame("./output/", "test_")