### Question:

Google and Facebook (now Meta) historically maintain monolithic codebases instead of microservices. How might such systems still scale to millions of users? Consider load balancing, horizontal scaling, and distributed infrastructure.

*Note: This is a system design discussion question — no code required.*

### Answer:

Both companies aggressively invested in global data center infrastructure, allowing them to manage traffic internally rather than relying on third-party cloud providers. Data centers spread across multiple regions minimize latency for users worldwide.

Monolithic systems scale horizontally by running multiple identical replicas of the application behind a load balancer. Google uses Maglev, an internal software-based load balancer that runs on commodity Linux servers, avoiding expensive proprietary hardware. Meta uses a multi-layered load balancing architecture to efficiently distribute traffic across its infrastructure.

Both companies also developed custom data stores optimized for their specific workloads. Google's Bigtable is a distributed NoSQL database designed for horizontal scaling across Google's diverse product data. Meta's TAO is a distributed data store built on top of MySQL and memcached, optimized for the graph-like structure of social connections.
