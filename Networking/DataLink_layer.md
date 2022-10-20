### Data Link Layer
Data link layer is the second layer from bottom in the OSI model.It deals with the following cases in a networking circuit:

- Hop to Hop Delivery : Helps in transporting packet from one router to another router. 
- Flow Control : Deals with the control of flow of packets from one netwrok to another network.
- Error Control : Means help in control of any error that occurs in the bits transported over the newtork.
- Access Control : Means to allow only one  packet to transfer data from one router to another and not allowing others:

#### Data link layer is divided into two sublayer:

- **The logical Link Control:**

This is also called data link control, responsible for framing, flow and error control. This is upper sublayer.

- **The Media Access Control:**

This is lower sublayer responsible for sharing of common media across multiple networking devices.
It is responsible for resolving access to shared media such that no tow devices use the shared media at the same time leading to any collision
This layer is not required if each device has a dedicated channel

#### Flow Control:

The Data Link layer employs the following algorithm to ensure flow control:

- Stop N Wait(SNW) protocol :- In this protocol the sender sends only one frame from sender to the receiver and waits till an ACK is received.
- Go Back N Control :- In this protocol we cand send muktiple frames at one time. In this protocol one can send a frame size equals to 2 power n .
                      Multiple data items can be sent at particular moment but only one accepted at a moment.
- Selective Repeat ARQ :- Selective-Repeat ARQ technique is more efficient than Go-Back-N ARQ.
                         In this technique, only those frames are retransmitted for which negative acknowledgement (NAK) has been received.
                         The receiver storage buffer keeps all the damaged frames on hold until the frame in error is correctly received.
                         The receiver must have an appropriate logic for reinserting the frames in a correct order.
                         The sender must consist of a searching mechanism that selects only the requested frame for retransmission.
#### Error Detection: 

The Data Link layer employs the following algorithm to ensure error control:

There are two types of errors:
- **Single bit error** : when there is an error in only one bit.
- **Burst errors** : When the is error in more than one bits.

##### Algorithms for error corrections:

-  Hamming Code:

**Parity bits** : The bit which is appended to the original data of binary bits so that the total number of 1s is even or odd.

**Even parity** : To check for even parity, if the total number of 1s is even, then the value of the parity bit is 0.
                      If the total number of 1s occurrences is odd, then the value of the parity bit is 1.

**Odd Parity** : To check for odd parity, if the total number of 1s is even, then the value of parity bit is 1.
                     If the total number of 1s is odd, then the value of parity bit is 0.

##### Algorithm of Hamming Code:

- An information of 'd' bits are added to the redundant bits 'r' to form d+r.
- The location of each of the (d+r) digits is assigned a decimal value.
- The 'r' bits are placed in the positions 1,2,.....2k-1.
- At the receiving end, the parity bits are recalculated. The decimal value of the parity bits determines the position of an error



