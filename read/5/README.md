##i Reference
Georgios Gousios, "The GHTorent Dataset and Tool Suite",Proceeding MSR '13 Proceedings of the 10th Working Conference on Mining Software Repositories.

##ii Keywords

ii1. Dataset - The dataset used in GHTorent and the details and construction process, the challenges and opportunities of working with this data. 

ii2. Querying- Range and resource querying is supported by REST API  

ii3. Decentralized

##iii Notes

iii1. The existing limit of 5000 requests per hour is less than the actual rate of 8,300 an hour. A single account is not sufficient to get the image. GHTorent overcomes this. 

iii2. Memoization is done and hence the data is cacheable. The result has dependency resolution that can fail and that can lead to failure in retrieving the result on the whole.

iii3. Limitations:
  - The data is additive. The deletions made in Github is ignored in GHTorent.
  - Watch/follow actions are timestamped only after GHTorent started saving the data. Github doesn't timestamp some important entities
  - Issues and pull requests are dual: Data might have to be pulled from different sources.
  - There are lots of fake user data in GHTorent that were created to resolve the commit users
  - Pull requests might be handled outside git. Also, authorship is lost when there are commit-squashing
  - Bug characters cannot be examined across repositories as they are all textual description
  - REST queries returns modified results leading to duplicate data at times
  - Some events may go missing and it cannot be fixed as only 300 newest events are visible per repository
  
iii4. Opportunities:
  - Developer identities can be studied as we have a unified source
  - The ecosystem can be understood as GHTorent has time-stamped information
  - Promotion and collaboration can be done better 
  - Replication of existing studies can be done by identifying the homogeneity.
  - Custom analysis and data extension can be performed all the time
  - Network analysis can be performed 

##iv Comments

iv1. The limitations of the GHTorent was brought out well. 

iv2. The paper did not however bring out the advantage of the tool although it mentioned about the future with the tool.

iv3. Also, the important factor that the actual useful repositories that can be useful in the research might be just a few hundreds against the thousands of repositories we have at hand. GHTorent doesn't consider this while performing any research.
