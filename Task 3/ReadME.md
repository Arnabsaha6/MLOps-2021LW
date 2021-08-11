Task Description 📄
📌 Create Live Streaming Video Chat App without voice
using cv2 module of Python:
Live Video Streaming App using OpenCV and Socket Programming
For Camera live-streaming app over the network,
TCP(Transmission Control Protocol) or IP(Internet Protocol
)could be used. This method allows a large piece of information or
data let it be in the form of image of burst images forming a video
to be transmitted reliably, as it manages how a larger packet being
broken into smaller packets to be transmitted and again
reassembled in the right order at the the destination without
losing the property.
Another known network protocol is UDP (User Datagram
Protocol). The use of this protocol is for faster data transmission
over a network. However, UDP’s drawback is less reliable
compared to TCP/IP as there is always chance of data loss (packet
drop).
TCP Server –
1. using create(), Create TCP socket.
2. using bind(), Bind the socket to server address.
3. using listen(), put the server socket in a passive mode,
where it waits for the client to approach the server to
make a connection
4. using accept(), At this point, connection is established
between client and server, and they are ready to transfer
data.
TCP Client –
1. Create TCP socket.
2. connect newly created client socket to server.