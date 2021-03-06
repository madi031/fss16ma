##i Reference

G Gousios and D Spinellis, "GHTorrent: Github’s Data from a Firehose". Mining Software Repositories (MSR), 2012 9th IEEE Working Conference. 

##ii Keywords

ii1. Events - Aggregated pointers to the data generated through actions performed by users on their repositories. They are useful for tracking the project's timeline.

ii2. Raw data - Data pointed to by the events. These are divided among the various entities stored in GitHub: users, organizations, teams, commits, issues, repositories, pull requests, issue comments, milestones, and pull request comments.

ii3. State data - Data generated by post-processing the raw data to recreate the project's state at certain points in the project's timeline.

ii4. Pull request - It is associated with the repository and presents some changes that a user can integrate into the repository. It can have comments associated with it.

##iii Notes

iii1. Motivational Statements - GitHub has emerged as a popular project hosting, mirroring and collaboration platform. GitHub provides an extensive REST APT, which enables researchers to retireve both the commits to the projects' repositories and events generted through user actions on project resources. This paper aims to create a scalable off line mirror of GitHub's event streams and persistent data, and offer it to the research community as a service.

iii2. Sampling Procedures - GitHub is hosting almost 4 million repositories from 1.5 million users, receiving more than 70,000 commits per day. As a result, the processing, storage and network capacity requirements to process entire stream can be quite steep. GHTorrent address this issue through the distribution of the data collection and its replication among research teams. They collected commits through GitHub's RSS feed and its commit stream page when the RSS feed became unavailable. Then they changed the collection to be based on events and expanded the collection operation to use event data as the starting point.

iii3. Patterns - There can be period of inactivity while processing these huge amount of datas and there should be some kind of monitoring to identify this. Here, they have employed a mechanism to monitor the daily event retrieval activity in order to make sure that such problems will not remain undetected for more than a few hours. When we retrieve huge amount of data, it is best to distribute the data among different system to manage the network and storage capacity and implement a mechanism to consolidate the data.

iii4. Related work - Howison et al, in the FLOSSmole project, collected meta data from OSS projects hosted on the Sourceforge site and offers both dataset and an online query interface. Alitheia Core project, provides an analysis platform and an accompanying dataset containing process and project metrics. Rahman and Devanbu exploited Git's strong authorship capabilities to study the impact of ownership and developer experience on software defects. Capilupi and Cortazar used Git's ability to track commit time at the developer's cite to produce a round the clock development bar chart similar to this paper.

## iv Improvements

iv1. GHTorrent uses currently retrieve raw event contents and store them in MongoDB collections. To reconstruct the GitHub's data scheme, it has to restart the events from the initial state, which might not be available all the time.

iv2. They can also automate the generation and distribution of torrent files through RSS feeds and scripts and automatically download and update remote databases.

iv3. They can also write tools or platforms that are able to process the vast amount of data that GHTorrent offers, which will help the research team community to access the data easier.
