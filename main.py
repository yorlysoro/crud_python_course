#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

clients = 'pablo,ricardo,'


def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print("Client alerady is in the client's list")


def list_clients():
    global clients

    print(clients)


def update_client(client_name):
    global clients

    if client_name in clients:
        update_client_name = input('What is the updated client name? ')
        clients = clients.replace(client_name + ',', update_client_name + ',')
    else:
        print("Client is not in clients list")


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ",", '')
    else:
        print("Client is not in clients list")


def search_clients(client_name):
    clients_list = clients.split(',')

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True
    return False


def _add_comma():
    global clients

    clients += ','


def _print_welcome():
    print("WELCOME TO PLATZI VENTAS")
    print("*" * 50)
    print("What would you like to do today?")
    print("[C]reate client")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch client")


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name? ')

        if client_name.lower() == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit(1)

    return client_name


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()
    if command == "C":
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == "D":
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == "U":
        client_name = _get_client_name()
        update_client(client_name)
        list_clients()
    elif command == "S":
        client_name = _get_client_name()
        found = search_clients(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print("The client: {} is not in our client's list".format(client_name))

    else:
        print('Invalid command')
