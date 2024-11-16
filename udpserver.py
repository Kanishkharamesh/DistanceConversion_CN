from socket import *


serverPort = 12002
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")


to_meters_factors = {
    'm': 1,           # meters to meters
    'cm': 0.01,       # centimeters to meters
    'km': 1000,       # kilometers to meters
    'ft': 0.3048,     # feet to meters
    'mi': 1609.34     # miles to meters
}

from_meters_factors = {
    'm': 1,           # meters to meters
    'cm': 100,        # meters to centimeters
    'km': 0.001,      # meters to kilometers
    'ft': 3.28084,    # meters to feet
    'mi': 0.000621371 # meters to miles
}

while True:
    
    message, clientAddress = serverSocket.recvfrom(2048)

    try:
        
        data = message.decode().strip().split()
       
        
        if len(data) != 3:
            raise ValueError("Invalid format. Please use '<value> <from_unit> <to_unit>'")

       
        distance_value = float(data[0])  
        from_unit = data[1].lower()
        to_unit = data[2].lower()

       
        if from_unit in to_meters_factors and to_unit in from_meters_factors:
           
            distance_in_meters = distance_value * to_meters_factors[from_unit]
            converted_distance = distance_in_meters * from_meters_factors[to_unit]
            modifiedMessage = f"{converted_distance} {to_unit}"
        else:
            modifiedMessage = f"Unsupported units. Supported units are: {', '.join(to_meters_factors.keys())}"

        
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)

    except ValueError as e:
       
        errorMessage = f"Error: {str(e)}"
        serverSocket.sendto(errorMessage.encode(), clientAddress)