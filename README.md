# DistanceConversion_CN

UDP Distance Converter
This project implements a simple UDP-based Distance Converter using Python. It consists of a client-server model where the client sends a distance value along with its units to the server, and the server responds with the converted value in the requested units.

Features
Converts distances between various units: meters (m), centimeters (cm), kilometers (km), feet (ft), and miles (mi).
Implements the UDP protocol for communication between the client and server.
Includes error handling for invalid input, unsupported units, or incorrect message formats.
File Structure
udpclient.py
Role: Acts as the client, allowing users to input a distance value and request conversion.
Key Functions:
Takes input for the distance, its current unit, and the target unit.
Sends the request to the server over UDP.
Displays the converted value or error messages received from the server.
udpserver.py
Role: Acts as the server, processing conversion requests and responding to the client.
Key Functions:
Listens for incoming UDP requests.
Converts distances using predefined conversion factors.
Handles errors and unsupported units gracefully.
How to Run
Prerequisites
Python 3.x installed on your system.
Steps
Clone this repository:
bash
Copy code
git clone https://github.com/yourusername/udp-distance-converter.git
cd udp-distance-converter
Open two terminal windows:
Terminal 1: Run the server:
bash
Copy code
python udpserver.py
Terminal 2: Run the client:
bash
Copy code
python udpclient.py
Enter the required inputs in the client terminal:
Example:
text
Copy code
Enter distance value: 100
Enter the current unit (m, cm, km, ft, mi): m
Enter the target unit (m, cm, km, ft, mi): km
Output:
text
Copy code
Converted distance: 0.1 km
Supported Units
Meters (m)
Centimeters (cm)
Kilometers (km)
Feet (ft)
Miles (mi)
Error Handling
Invalid input format: The server validates the message format and provides an appropriate error message.
Unsupported units: If an unsupported unit is used, the server responds with a list of supported units.
