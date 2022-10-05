## How AI helps predict traffic and determine routes?

Every day, over 1 billion kilometers are driven with Google Maps in more than 220 countries and territories around the world. When you hop in your car or on your motorbike and start navigating, you’re instantly shown a few things: which way to go, whether the traffic along your route is heavy or light, an estimated travel time, and an estimated time of arrival (ETA). While all of this appears simple, there’s a ton going on behind the scenes to deliver this information in a matter of seconds.

Today, we’ll break down one of our favorite topics: traffic and routing. If you’ve ever wondered just how Google Maps knows when there’s a massive traffic jam or how we determine the best route for a trip, read on. 

### Live traffic, powered by drivers all around the world

When people navigate with Google Maps, aggregate location data can be used to understand traffic conditions on roads all over the world. But while this information helps you find current traffic estimates —whether or not a traffic jam will affect your drive right now—it doesn’t account for what traffic will look like 10, 20, or even 50 minutes into your journey. This is where technology really comes into play.



### Predicting traffic with advanced machine learning techniques, and a little bit of history

To predict what traffic will look like in the near future, Google Maps analyzes historical traffic patterns for roads over time. For example, one pattern may show that the 280 freeway in Northern California typically has vehicles traveling at a speed of 65mph between 6-7am, but only at 15-20mph in the late afternoon. We then combine this database of historical traffic patterns with live traffic conditions, using machine learning to generate predictions based on both sets of data. 

Recently, we partnered with DeepMind, an Alphabet AI research lab, to improve the accuracy of our traffic prediction capabilities. Our ETA predictions already have a very high accuracy bar–in fact, we see that our predictions have been consistently accurate for over 97% of trips. By partnering with DeepMind, we’ve been able to cut the percentage of inaccurate ETAs even further by using a machine learning architecture known as Graph Neural Networks–with significant improvements in places like Berlin, Jakarta, São Paulo, Sydney, Tokyo, and Washington D.C. This technique is what enables Google Maps to better predict whether or not you’ll be affected by a slowdown that may not have even started yet! 



### Keeping it fresh

For most of the 13 years that Google Maps has provided traffic data, historical traffic patterns have been reliable indicators of what your conditions on the road could look like—but that's not always the case. Since the start of the COVID-19 pandemic, traffic patterns around the globe have shifted dramatically. We saw up to a 50 percent decrease in worldwide traffic when lockdowns started in early 2020. Since then, parts of the world have reopened gradually, while others maintain restrictions. To account for this sudden change, we’ve recently updated our models to become more agile—automatically prioritizing historical traffic patterns from the last two to four weeks, and deprioritizing patterns from any time before that.



### How Google Maps selects routes

Our predictive traffic models are also a key part of how Google Maps determines driving routes. If we predict that traffic is likely to become heavy in one direction, we’ll automatically find you a lower-traffic alternative. We also look at a number of other factors, like road quality. Is the road paved or unpaved, or covered in gravel, dirt or mud? Elements like these can make a road difficult to drive down, and we’re less likely to recommend this road as part of your route. We also look at the size and directness of a road—driving down a highway is often more efficient than taking a smaller road with multiple stops.

Two other sources of information are important to making sure we recommend the best routes: authoritative data from local governments and real-time feedback from users. Authoritative data lets Google Maps know about speed limits, tolls, or if certain roads are restricted due to things like construction or COVID-19. And incident reports from drivers let Google Maps quickly show if a road or lane is closed, if there’s construction nearby, or if there’s a disabled vehicle or an object on the road. Both sources are also used to help us understand when road conditions change unexpectedly due to mudslides, snowstorms, or other forces of nature.



### Putting it all together

So how exactly does this all work in real life? Say you’re heading to a doctor’s appointment across town, driving down the road you typically take to get there. When you leave the house, traffic is flowing freely, with zero indication of any disruptions along the way. With Google Maps’ traffic predictions combined with live traffic conditions, we let you know that if you continue down your current route, there’s a good chance you’ll get stuck in unexpected gridlock traffic about 30 minutes into your ride—which would mean missing your appointment. As a result, Google Maps automatically reroutes you using its knowledge about nearby road conditions and incidents—helping you avoid the jam altogether and get to your appointment on time.

Predicting traffic and determining routes is incredibly complex—and we'll keep working on tools and technology to keep you out of gridlock, and on a route that's as safe and efficient as possible.