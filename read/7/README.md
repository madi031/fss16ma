##i Reference 

Kelly Blincoe, Francis Harrison and Daniela Damian, "Ecosystems in GitHub and a method for ecosystem identification using reference coupling", Proceeding MSR '15 Proceedings of the 12th Working Conference on Mining Software Repositories.
 
##ii Keywords 
 
ii1. Technical dependency

ii2. Reference coupling: Cross-references to other repositories appearing in GitHub comments indicating the existence of a technical
dependency is termed as refernce coupling. 

ii3. Louvain community detection method: It is a greedy optimization method to partition into communities of densely connected nodes and
optimize the modularity. It outperforms both in optimizing modularity and computation time. 

##iii Notes

iii1. Research Question 1: Does cross-references to other projects in issue, pull request, and commit comments indicate the existence of a technical dependency between the two projects? 

Identify if the comments for the cross reference is a technical dependency and if it is a direct or indirect dependency.
The direct dependency was directly between two projects where the issue/fix depended on the other repository or if the project needs update based on the other repository. Indirect dependency where both projects will depend on a third-project which is not cross-referenced.

iii2. Research Question 2: What ecosystems exist across GitHub-hosted projects and what is their structure? 

High modularity indicated dense connection within communities and sparse connection between communities. High modularity was obtained proving close technical dependency than a random graph. 

iii3. Research Question 3: Do the project owners’ and contributors’ social behaviours align with the technical dependencies?

The social behaviour of project contributors is not aligned with project dependencies. Contributor follower network communities do not have one central project and the network is much more densely connected. 

iii4. Properties of an ecosystem

  - Ecosystems revolve around one central project
  
  - Predominant type of ecosystems is software development support
  
  - Ecosystems are interconnected

##iv Data

Data was extracted from GHTorrent which is a mirror of GitHub API data. 

##v Improvisation

v1. The cross-reference dependency where analysed from comments which were sampled and where read and interpreted manually. There can be a application to identify if the dependency is technical/ if they are direct or indirect dependency. 

v2. The ecosystems being interconnected and one project being central were a little self evident. 

 
