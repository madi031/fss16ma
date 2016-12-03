# Week 6

The code can be found [here](https://github.com/madi031/fss16ma/tree/master/code/6/Code).

The dataset is modified to have exactly 3 classes.

### Data Generator

```DataGenerator.py``` generates data in specified format.

### Data Reader

The result of Data Reader can be found [here](https://github.com/madi031/fss16ma/tree/master/code/6/Output).

```
Era 1
Class = sky, recall 0.85
Class = path, recall 0.92




Era 2
Class = sky, recall 0.90
Class = path, recall 0.92




Era 3
Class = sky, recall 0.94
Class = path, recall 0.91




Era 4
Class = sky, recall 0.87
Class = path, recall 0.98




Era 5
Class = sky, recall 0.98
Class = path, recall 0.93




Era 6
Class = sky, recall 0.91
Class = path, recall 0.96




Era 7
Class = sky, recall 0.94
Class = path, recall 0.94




Era 8
Class = sky, recall 0.96
Class = path, recall 0.98




Era 9
Class = sky, recall 0.92
Class = path, recall 0.98




Era 10
Class = sky, recall 1.00
Class = path, recall 0.93
Class = brickface, recall 0.00




Era 11
Class = sky, recall 0.88
Class = path, recall 1.00
Class = brickface, recall 0.68




Era 12
Class = sky, recall 0.73
Class = path, recall 0.90
Class = brickface, recall 0.60




Era 13
Class = sky, recall 0.77
Class = path, recall 1.00
Class = brickface, recall 0.67




Era 14
Class = sky, recall 0.69
Class = path, recall 1.00
Class = brickface, recall 0.72




Era 15
Class = sky, recall 0.82
Class = path, recall 1.00
Class = brickface, recall 0.70




Era 16
Class = sky, recall 0.90
Class = path, recall 1.00
Class = brickface, recall 0.75




Era 17
Class = sky, recall 0.64
Class = path, recall 1.00
Class = brickface, recall 0.75




Era 18
Class = sky, recall 0.78
Class = path, recall 1.00
Class = brickface, recall 0.59




Era 19
Class = sky, recall 0.80
Class = path, recall 0.91
Class = brickface, recall 0.64




Era 20
Class = sky, recall 0.74
Class = path, recall 0.92
Class = brickface, recall 0.92
```

###Incremental NB

The result of the Incremental NB can be found [here](https://github.com/madi031/fss16ma/tree/master/code/6/Output).

```
Era 1
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -58.43
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -61.01
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -59.58
Expected = path, 	 Predicted = path, 	 Log of the likelihood = -54.43
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -65.01
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -59.23
Expected = path, 	 Predicted = path, 	 Log of the likelihood = -58.94
Expected = path, 	 Predicted = path, 	 Log of the likelihood = -58.06
Expected = path, 	 Predicted = path, 	 Log of the likelihood = -52.49
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -59.03
Expected = path, 	 Predicted = path, 	 Log of the likelihood = -54.09
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -87.29
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -81.95
Expected = path, 	 Predicted = path, 	 Log of the likelihood = -50.16
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -57.84
Expected = path, 	 Predicted = path, 	 Log of the likelihood = -58.09
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -60.73
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -82.10
Expected = path, 	 Predicted = path, 	 Log of the likelihood = -59.32
Expected = path, 	 Predicted = path, 	 Log of the likelihood = -59.12
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -61.44
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -60.65
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -60.73
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -79.35
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -79.74
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -70.66
Expected = path, 	 Predicted = path, 	 Log of the likelihood = -57.53
Expected = path, 	 Predicted = path, 	 Log of the likelihood = -52.67
Expected = path, 	 Predicted = path, 	 Log of the likelihood = -54.13
Expected = path, 	 Predicted = sky, 	 Log of the likelihood = -84.31
...
```

###Anamoly Detector
A12 test is performed and if the score is greater than 0.7, it is detected as anamoly. The result of the Anamoly Detector can be found [here](https://github.com/madi031/fss16ma/tree/master/code/6/Output).

```
Era 1
Class = path, recall 0.81
Class = sky, recall 0.88




Era 2
Class = path, recall 0.91
Class = sky, recall 0.89




Era 3
Class = path, recall 0.91
Class = sky, recall 0.89




Era 4
Class = path, recall 0.98
Class = sky, recall 0.93




Era 5
Class = path, recall 0.94
Class = sky, recall 0.96




Era 6
Class = path, recall 0.95
Class = sky, recall 0.91




Era 7
Class = path, recall 0.98
Class = sky, recall 0.98




Era 8
Class = path, recall 0.95
Class = sky, recall 0.92




Era 9
Class = path, recall 0.98
Class = sky, recall 0.98




Era 10
Class = path, recall 1.00
Class = sky, recall 0.94
Class = brickface, recall 0.00
Anamoly detected





Era 11
Class = path, recall 1.00
Class = sky, recall 0.78
Class = brickface, recall 0.74




Era 12
Class = path, recall 0.88
Class = sky, recall 0.72
Class = brickface, recall 0.63




Era 13
Class = path, recall 1.00
Class = sky, recall 0.74
Class = brickface, recall 0.69




Era 14
Class = path, recall 1.00
Class = sky, recall 0.79
Class = brickface, recall 0.66




Era 15
Class = path, recall 1.00
Class = sky, recall 0.73
Class = brickface, recall 0.75




Era 16
Class = path, recall 0.90
Class = sky, recall 0.77
Class = brickface, recall 0.76




Era 17
Class = path, recall 1.00
Class = sky, recall 0.78
Class = brickface, recall 0.64




Era 18
Class = path, recall 1.00
Class = sky, recall 0.76
Class = brickface, recall 0.63




Era 19
Class = path, recall 0.89
Class = sky, recall 0.72
Class = brickface, recall 0.67




Era 20
Class = path, recall 0.96
Class = sky, recall 0.75
Class = brickface, recall 0.75
```
