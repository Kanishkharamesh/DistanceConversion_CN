from socket import *

serverName = '***.***.**.***' 
serverPort = 12002


clientSocket = socket(AF_INET, SOCK_DGRAM)

try:
    
    distance = input("Enter distance value: ").strip()
    from_unit = input("Enter the current unit (m, cm, km, ft, mi): ").strip().lower()
    to_unit = input("Enter the target unit (m, cm, km, ft, mi): ").strip().lower()


    try:
        distance_value = float(distance)
    except ValueError:
        raise ValueError("Invalid distance value. Please enter a numeric distance.")

    
    message = f"{distance_value} {from_unit} {to_unit}"
    print(f"Sending message to server: {message}")


    clientSocket.sendto(message.encode(), (serverName, serverPort))

   
    convertedMessage, serverAddress = clientSocket.recvfrom(2048)
    response = convertedMessage.decode()
    print(f"Received response from server: {response}")


    if "Error" in response or "Unsupported" in response:
        print(response)
    else:
        print(f"Converted distance: {response}")

except ValueError as e:
  
    print(f"Error: {e}")

finally:

    clientSocket.close()
