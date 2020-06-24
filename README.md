# alamara

## Create Contour for human body

1. Implemented skin detection. To test from body_detection directory run

        python .\try.py --image ..\img\test_4.jpg

    ![Skin Detection](output\skin_detection.png)

## After human contour done, need to calculate size of the body

1. Tried to implement object_size calculation. To test go to body_size directory

        python object_size.py --image ..\img\test_3.jpg --width 3.5
    
    ![Skin Detection](output\object_size.png)
