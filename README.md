# Alamara

## Create Contour for human body

1. Implemented skin detection. To test from body_detection directory run

        python .\body_detection\skin_detection.py --image .\img\test_1.JPG

    ![Skin Detection](output/skin_detection.png)


2. Body Detection

        python .\body_detection\watershed_algorithm.py --image .\img\test_1.JPG
    
    ![Body Detection](output/watershed.png)

3. Vide Body Detection

         python .\body_detection\live_detection.py
        
    ![Body Detection](output/video_output.gif)
    
    
## After human contour done, need to calculate size of the body

1. Tried to implement object_size calculation. To test go to body_size directory

        python .\body_size\object_size.py --image .\img\test_1.JPG --width 9
    
    ![Object Detection](output/object_size.png)
    ![Object Detection](output/human_size.png)
