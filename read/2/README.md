##i Reference

 Pat Helland, "If you have too much data, then 'good enough' is good enough". Communications of the ACM, vol. 54, pp. 40–47, Jun. 2011.
 
##ii Keywords

ii1. Unlocked data - The data allows changes. This is how the real world data is.

ii2. Locked data - Data which doesn't have change in semantics.Classic SQL depends on locked data.
 
ii3. ETL - Extract, Load, Transform - Data from multiple sources can be handled through NoSQL using ETL. 
 
ii4. Lossy answers - Answers are not perfect.

##iii Notes

iii1. Motivation - The classical SQL is no longer sufficient to solve all our problems. Humungous data accumulated nowadays are unstructured, the semantics keeps changing if it exists, the answers are not accurate. However the business problems sometimes needs just the lossy answers. 

iii2. Observations - Huge scale has implications on the consistency semantics of the data. NoSQL cannot handle transactions across all the data. The data undergoes DDL transformation to be saved in a database, but unlocked data is supposed to be immutable. The information can be gained from inferences where we can find two disparate things are actually the same. 

iii3. Conclusion - There needs to be a new theory for unlocked data, how to evaluate the lossyness until which it is acceptable. There has to be some work on identifying the patterns and inferences to gain knowlegde from the data because data can no longer give the accurate information. 

##iv Improvisation

iv1. The author can mention statistical proof or example to justify the conclusion.

iv2. The author feels there needs to be a new theory to sort out the current scenario. 

iv3. The paper is a conclusion and not questioning something and hence doesn't have any improvements unless someone can refute the author. 
