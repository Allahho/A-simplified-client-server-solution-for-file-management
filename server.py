"""
This module handles the TCP server logic.
"""

import asyncio
import signal
from ServerManager import ServerManager
signal.signal(signal.SIGINT, signal.SIG_DFL)


async def handle_echo(reader, writer):
    """
    TCP SERVER connections are binded to this method
    this method utilizes the ServerManager module to handle all the read
    and write operations for the connected clients
    """
    addr = writer.get_extra_info('peername')
    message = f"{addr} is connected !!!!"
    writer.write(
        ('Proceed with command(login <username> <password>).\n').encode())
    await writer.drain()
    writer.write(
        ('To register a new user, use command (register <username> <password> <privilige>)\n').encode())
    await writer.drain()
    manager = ServerManager()
    try:
        while True:
            data = await reader.read(100)
            message = data.decode().strip()
            if message == 'quit':
                break
            elif message.startswith('help'):
                data = manager.help()
            elif message.startswith('change_folder'):
                if len(message.split(' ')) == 2:
                    data = manager.changeFolder(message.split(' ')[
                        1])
                else:
                    data = "Please provide a folder name"
            elif message.startswith('list'):
                if len(message.split(' ')) == 1:
                    data = manager.list()
                else:
                    data = "Please provide a filename"
            elif message.startswith('read_file'):
                if len(message.split(' ')) == 2:
                    data = manager.readFile(message.split(' ')[
                        1])
                else:
                    data = "Please provide a filename"
            elif message.startswith('write_file'):
                if len(message.split(' ')) == 3:
                    data = manager.writeFile(message.split(' ')[
                        1], message.split(' ')[2])
                else:
                    data = "Please provide a filename and data"
            elif message.startswith('create_folder'):
                if len(message.split(' ')) == 2:
                    data = manager.createFolder(message.split(' ')[
                        1])
                else:
                    data = "Please provide a foldername"
            elif message.startswith('register'):
                if len(message.split(' ')) == 4:
                    data = manager.register(message.split(' ')[
                        1], message.split(' ')[2], message.split()[3])
                else:
                    data = "Please provide a username, password and privilege."
            elif message.startswith('login'):
                if len(message.split(' ')) == 3:
                    data = manager.login(
                        message.split(' ')[1], message.split(' ')[2])
                else:
                    data = "Please provide a username and password."
            elif message.startswith('delete'):
                if len(message.split(' ')) == 3:
                    data = manager.delete(
                        message.split(' ')[1], message.split(' ')[2])
                else:
                    data = "Please provide a username and password."
            else:
                data = 'Command not recognized'
            if data:
                writer.write((data + '\n').encode())
                await writer.drain()
            else:
                writer.write(
                    ('There was an error. you can user command help to get available commands' + '\n').encode())
                await writer.drain()
    except ConnectionRefusedError:
        await asyncio.sleep(0.1)
        return
    except asyncio.CancelledError:
        return
    except ConnectionAbortedError:
        print("A Connection was closed")
        return
    except ConnectionResetError:
        print(f"A Connection was closed :{addr}")
        return
    except Exception:
        raise
    else:
        print("Close the connection")
        writer.close()


async def main():
    """
    This is the main method. A TCP SERVER is initiated and set to listen for client connects useing the asyncio lib
    """
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8080)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        try:
            await server.serve_forever()
        except Exception:
            raise

asyncio.run(main())
