# Design Discord

Background is that we have some type of group or something and peopl have to members of those to see any particular messages and what not. Each channel will have messages. We need to track messages we havent seen. Users can mention each other and then you get notifications like 3 unread messages or whatever. Direct messages maybe.

## Functional Requirements

We will focus on the servers and the channels witihin the server and picking up where we left off. We also want to be able tohave a visual indicator for number of notifications for channel and server if someone mentions us. We can send messages on a channelin real time. We should see unread messages. MEssages should be real time

## Non func

latency is minimized and more availablility but latency is the most important one. Let us say we support 5M active users, 50 M msgs per day. lets say 20K is limit for server lets say 10K messages per channel in a single day. Only text. Max limit 2000 chars. 2kb per message.

## High Level Design

sendMsg
