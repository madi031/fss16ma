##i Reference 

Georgios Gousios, Bogdan Vasilescu, Alexander Serebrenik, Andy Zaidman, "Lean GHTorrent: GitHub Data on Demand", MSR 2014, Proceedings of the 11th Working Conference on Mining Software Repositories

##ii Keywords

ii1. Data on demand - Customisable data dumps are being provided to user 

ii2. GHTorrent - Queriable, scalable, offline mirror of data available from GitHub REST API. 

ii3. Worker-queue model: Decentralization is achieved with this model 

ii4. Flexibility - In selecting the repositories and also ensures data dumps are available for reproducing results


##iii Notes 

iii1. It lowers the "barrier for entry" as the data-on-demand provides easier access to a specific set of GitHub data

iii2. Snapshots of data are available to ensure replicability

iii3. Research show researchers prefer data dumps over online querying

iii4. The architecture of the lean GHTorrent 
![Alt text](/read/6/Architecture.PNG/?raw=true "Optional Title")

iii5. Limitations:
  - The data dumps offer only first order dependencies
  - The dumps can take days to complete depending on request size and server load
  - No recovery action implemented
  - The request restricts to 1000 repositories.
  
##iv Improvisation

iv1. Since the data dumps are only of first order we will have to spend a lot of time in hand picking the users. 

iv2. For large scale, this is not a good option as there is GHTorrent to satisfy our needs and also this can take forever to complete. 

iv3. The author could have explained it with a much clearer case which included a problem statement and how lean GHTorrent made the mining process easy
