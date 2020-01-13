"""This module is the TCP Listener, Softwares like putty can also be used instead"""
import asyncio
import signal
from os import system, name
signal.signal(signal.SIGINT, signal.SIG_DFL)


async def tcp_echo_client():
    """Handles putgoing connection and manages the data to recevie and send to the TCP SERVER"""
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8080)
    message = ''
    print("Connected to : 127.0.0.1:8080")
    data = await reader.read(1024)
    print(f'Received: {data.decode()}')
    data = await reader.read(1024)
    print(f'Received: {data.decode()}')
    while True:
        message = input('[Enter Command] : ')
        if message == 'clear':
            # clear command to clear the command window
            if name == 'nt':
                # nt represents windows systems-
                _ = system('cls')
            else:
                # mac and linux based systems
                _ = system('clear')
            print("Connected to : 127.0.0.1:8080")
        elif message != 'quit':
            # Writes command to the TCP Stream
            writer.write(message.encode())
            data = await reader.read(1024)
            # Reads the TCP SERVER response
            print(f'Received: {data.decode()}')
        else:
            # quit command to close the command terminal
            writer.write(message.encode())
            break
    print('Close the connection')
    writer.close()


asyncio.run(tcp_echo_client())
