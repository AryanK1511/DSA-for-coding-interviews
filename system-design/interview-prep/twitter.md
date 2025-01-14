# Designing Twitter

Twitter is a social network people can follow other people. Some people might be more popular than others. This is going to be a very read heavy system

## Functional Requirements

Be able to follow other people, create a tweet, view feed (can be very complicated). For this case, we only see thhe tweets that we follow. Ask your interviewer what they want. With socials you will end up with video and images most of the time.

## Non functional requiremenst

500 M total users for example and 200 M daily users for instance

Most people will be viewing people and each people read about 100 tweets per day so 20B reads per day. For each tweet approx 1MB for each tweet. 20 Gigs of data is 20 PB data reading per day. Very read heavy. Eventual consistency should be enough. Lets say 50M tweets created per day. We will write much less data then we are reaiding. Average user follows about 100 isers per day for example. People can have a lot of followers as well

## High Level Design

User hits the App servers. We will have a load balancer and horizontally scale. Lets say we have a SQL database. We do have a very relational model in this case. In theory it will be easier to scale NoSQL but then you can also have a graph DB with NoSQL. For now lets say SQL. We should have a caching layer o we huit it first before hitting our DB. We will have some object storage for the media and stuff. The objects are static in nature so we can distribute them over a CDN. The client can then make a request to our CDN which is then tied to Object storage. We will be using apull based CDN.

## Design Details

createTweet(text, media: Optional, uid) id and stuff would be server side for auth header would have like a token or something. you should not send uid in this stuff. get feed doesnt need any info at all the auth will just have user id. User can follow another person you pass the user id of the person the person wants to follow

Follow table
followee: str -> Being followed
follower:

Indexing based on the follower

Tweet Table
Tweeid
Timestamp
text

We will be storing a massive amount of data. We will have so many reads so the obvious thing to do is have read only replicas. We use sharding to scale our writes. It is okay if single instance is written and async pouplation for the other replicas so its bascially eventually consistent. UID is the best for sharding key. We will hid the shard that has the tweets for epopel that the user follows. Since we dont have joins we can do this. Now we have to order them. So how to do that . Current system: User creates a tweet, it will go through server based on id we will find shard and store tweet store on start and media on object storage when user views feed, we query releavnt shards order stuff and send. in theor most popular tweets will be stored in the caching learn LRU cache. What if 19 are cached and some person wants 20 and we need to get all the problem is latency. As we break data with sharding we get less latency. We should henerate the news feed asynchronously and we will only regen for pepople that are actuve for the last 30 days or something. We can have a pub sub queue and this will feed data into cluster/workers and this will feed into a feed cache the app servers will hit feed cache. This is a huge cache and we will have to shard this since there are so many data points
