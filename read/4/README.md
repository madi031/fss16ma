##i Reference

C. Bird, P. C. Rigby, E. T. Barr, D. J. Hamilton, D. M. German, and P. Devanbu, “The promises and perils of mining Git,” in MSR ’09. 

##ii Keywords

ii1. Decentralization - The development is moving from centralized source code management to distributed. 

ii2. DAG - Git has commits in a directed acyclic graph form.

##iii Notes

iii1. Promises 
* The personal experiments and false starts are not lost in DSCM(Decentralized Source Code Management). 
* Git facilitates recovery of richer project history
* Git has private logs 
* Paper trails can be achieved by signed-off-by
* Git explicitly records authorship information for contributors who are not part of the core set of developers.
* In git all metadata, notably history, is local
* Git tracks content, so it can track the history of lines as they are moved or copied
* Git is faster and often uses less space than centralized repositories
* Most SCMs can be converted to git with the history of branches, merges and tags intact

iii2. Perils
* The nomenclature is conflicting between centralized and DSCM
* DSCM has implicit branching, which can confusing for CSCM developers
* Rebasing allows modifying the history
* Determining the branch on which commit was made is not always possible 
* Tracking merge is always not possible

iii3. The data was mainly public data available in git, sometimes included the private logs of users in certain cases. The comparison also uses SVN and CVS data against git data. 


##iv Improvisation

iv1. The analysis provided gives a good insight to how beneficial git can be. 

iv2. It is a paper which gives a clear briefing about the advantages and drawbacks of git. It also calls out  the advantage of SCM for developers to decide which one is better over the other. 
 
