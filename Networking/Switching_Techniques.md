### Switching Techniques
In large networks, there can be multiple paths from sender to receiver. In this, the best path is to be selected in order to avoid the transmission delay. Switching technique is used to connect the systems for making one-to-one communication.

#### Switching is broadly classified into three categories listed below:

- **Circuit Switching**
- **Packet Switching**
- **Message Switching**

Each of the techniques is discussed in detail below:

#### 1. Circuit Switching

In switching technique a dedicated path is established between sender and the receiver. Once the connection is established, then the dedicated path will remain to exist until the connection is terminated.
A complete end-to-end path must exist before the communication takes place. Best analogy of circuit switching is telephone networks. It is used for voice transmission.

In case of circuit switching technique, when any user wants to send the data, be it audio, image or video a request signal is sent to the receiver. The receiver sends back the acknowledgment to ensure the availability of the dedicated path. After receiving the acknowledgment, dedicated path transfers the data.
Communication via circuit switching takes place in 3 phases:

- **Circuit Establishment**
- **Data Transfer**
- **Circuit Termination**

Advantages of Circuit Switching are:
1. Reliable data transfer takes place once the connection is established.
2. Data transfer occurs at comparatively fast rate

Disadvantages of Circuit Switching are:
1. Wastage of Bandwidth occurs when the dedicated path is established, but no data transfer takes place
2. It takes a long time to establish connection.

#### 2. Packet Switching

In packet switching the message is transmitted in one go, but it is divided into smaller pieces, and they are sent individually.
Smaller data pieces are known as packets and each packet is assigned a unique number to identify and rearrange at the receiving end. In addition to unique identifying number, a packet also contains the source address and destination address in it's header.
The information is provided so as to avoid loss of data packets. 

If any packet is missing or corrupted, then the message will be sent to resend the message.
Packets will travel across the network, taking the shortest path as possible.
All the packets are reassembled at the receiving end in correct order.
If the correct order of the packets is reached, then the acknowledgment message will be sent.
There are two approaches to packet switching:

1. Datagram Packet Switching
2. Virtual circuit Switching

Datagram switching, also known as connectionless switching uses datagram (packets) to transmit and receive data. In this, the path is not fixed. Datagram takes the shortest route available to reach it's destination.
Virtual Circuit Switching, also known as connection-oriented switching uses a pre-determined path to transmit and receive data. It works similiar to circuit switching but makes use of packets instead of transmitting data as a whole.

Advantages of Packet Switching are:
1. It is cost-effective as secondary devices are not required to store data.
2. It is an efficient switching technique because it does not establish any pre-determined path prior to communication and many users an use the same channel simultaneously

Disadvantages of Packet Switching are:
1. High installment cost
2. It makes use of complex networking protocols

#### 3. Message Switching

Message or store-and-forward switching is a switching technique in which a message is transferred as a complete unit and routed through intermediate nodes at which it is first stored and then forwarded.
There is no establishment of a dedicated path between the sender and receiver. The destination address is appended to the message. 

Message Switching provides a dynamic routing as the message is routed through the intermediate nodes based on the information available in the message.
It treats each message as an independent entity. Every node store the message and when the suitable channel is available for transmission, the message is forwarded.

Advantages of Message Switching are:
1. Congestion in networks due to high traffic is greatly reduced in message switching. This happens because the message is first stored in the node.
2. Efficiency of bandwidth is enhanced as many nodes can use the same channel for communicating at a single time

Disadvantages of Message Switching are:
1. This technique demands sufficient storage devices in order to store the incoming and outgoing message.
2. Delay can occur due to store and forward mechanism