#Week2

##Active Shooter Exercise

###Things not to do: 
1. Do not panic or shout during rescue.
2. Do not wait for someone else to confirm a gunshot. Trust your instinct.  

###Things to do: 
1. Call 911. Give clear instructions.
2. Block or show active resistance to the shooter if we have to hide.
3. Know the clear exit/escape routes in the building.
 
##ZeroR Learner

The code for ZeroR learner is [here](https://github.com/madi031/fss16ma/blob/master/code/2/zeroRPredictor.py).

The function zeror and eg11 are below:
```
zeror() {
	python -B $Here/zeroRPredictor.py $1 $2
}

eg11() {
    local data="data/jedit-4.1.arff"         # edit this line to change the data
    local learners="j48 jrip nb rbfnet bnet zeror" # edit this line to change the leaners
    local goal=true                          # edit this line to hunt for another goal
    
    local i="$Tmp/eg11"
    if [ -f "$i.pd" ]; then
       report pd "$i"
       report pf "$i"
    else
        crossval 5 5 "$data" $Seed $learners | grep $goal >"$i"
        gawk  '{print $2,$10}' "$i" > "$i.pd"
        gawk  '{print $2,$11}' "$i" > "$i.pf"
        eg11
   fi
}
```
The output of the learner is below:
```
pd

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,           nb ,      45  ,    18 (      ----   * |---           ),25.00, 36.00, 45.00, 53.00, 60.00
   1 ,       rbfnet ,      47  ,    20 (      ------- *|   --         ),25.00, 43.00, 47.00, 60.00, 67.00
   2 ,         jrip ,      60  ,    23 (         ------|   *  ----    ),33.00, 50.00, 60.00, 71.00, 80.00
   2 ,         bnet ,      60  ,    17 (           ----|-  * -        ),40.00, 55.00, 60.00, 67.00, 71.00
   3 ,          j48 ,      72  ,    16 (               |----   *  --  ),50.00, 65.00, 72.00, 81.00, 87.00
pf

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,           nb ,       7  ,     6 (     --   *   -|-             ), 4.00,  5.00,  7.00, 10.00, 12.00
   1 ,          j48 ,       7  ,     6 (     --   *  --|---           ), 4.00,  5.00,  7.00,  9.00, 13.00
   1 ,         jrip ,       9  ,    10 (  ---        * |------        ), 2.00,  4.00,  9.00, 11.00, 15.00
   1 ,       rbfnet ,       9  ,     5 (     -----   * |----          ), 4.00,  7.00,  9.00, 11.00, 14.00
   1 ,         bnet ,      11  ,     6 (        -----  |*   ------    ), 6.00,  9.00, 11.00, 14.00, 18.00
   
```

## Table Reader

Check out the code [here] (https://github.com/madi031/fss16ma/tree/master/code/2).

The output of the reader is below:

```
outlook
Mode: sunny     Entropy: 1.57740628285
temperature-
Mean: 73.5714285714     Standard deviation: 6.57166745863
<humidity
Mean: 81.6428571429     Standard deviation: 10.285218242
windy
Mode: FALSE     Entropy: 0.985228136034
>play
Mean: 1.07142857143     Standard deviation: 0.997248963151
```
