# D:\project\Tee Rpojets\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec

# train the cascade classifier model using:
# $ C:/Users/Ben/learncodebygaming/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -numPos 200 -numNeg 100 -numStages 10 -w 24 -h 24

# $ ..\..\..\..\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data cascade\ -vec pos.vec -bg neg.txt -numPos 20 -numNeg 15 -numStages 10 -w 24 -h 24

``` anotation
-   C:/Users/Ben/learncodebygaming/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=pos.txt --images=positive/
-   ..\..\..\..\opencv\build\x64\vc15\bin\opencv_annotation.exe --annotations=pos.txt --images=data/images
-   ..\..\..\opencv\build\x64\vc15\bin\opencv_annotation.exe --annotations=pos.txt --images=data/images
```

config\opencv_createsamples.exe -info data\comppos.txt -w 24 -h 24 -num 6000 -vec data\comppos.vec



..\..\..\..\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data ..\cascade\resistor -vec respos.vec -bg resneg.txt -numPos 1 -numNeg 200 -numStages 10 -w 40 -h 40

config\opencv_createsamples.exe -info data\DCSpos.txt -w 24 -h 24 -num 1000 -vec data\DCSpos.vec
..\..\..\..\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data ..\cascade\battery -vec DCSpos.vec -bg DCSneg.txt -numPos 320 -numNeg 400 -numStages 10 -w 24 -h 24


# lab
..\..\..\..\opencv\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info indpos.txt -w 16 -h 16 -num 400 -vec ind.vec
..\..\..\..\opencv\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data ..\cascade\inductor -vec ind.vec -bg indneg.txt -numPos 350 -numNeg 350 -numStages 10 -w 16 -h 16