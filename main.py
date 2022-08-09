#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineering'
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineering'
    }
]


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print("Client alerady is in the client's list")


def list_clients():
    for idx, client in enumerate(clients):
        print("{uid} | {name} | {company} | {email} | {position}".format(uid=idx, name=client['name'],
                                                                        company=client['company'], email=client['email'],
                                                            position=client['position']))


def _get_client_idx(client_name):
    for idx, client_id in enumerate(clients):
        if client_id['name'] == client_name:
            return idx


def update_client(client_name):
    global clients

    if search_clients(client_name):
        print(f"The client {client_name} already exists")
        print("please insert the new data")
        update_client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        index = _get_client_idx(client_name)
        clients[index] = update_client
    else:
        print("Client is not in clients list")


def delete_client(client_name):
    global clients

    if search_clients(client_name):
        clients.remove(clients[_get_client_idx(client_name)])
    else:
        print("Client is not in clients list")


def search_clients(client_name):
    for client in clients:
        if client['name'] != client_name:
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


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}? '.format(field_name))

    return field.capitalize()


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name? ')

        if client_name.lower() == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit(1)

    return client_name.capitalize()


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()
    if command == "C":
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
        list_clients()
    elif command == "D":
        client_name = _get_client_field('name')
        delete_client(client_name)
        list_clients()
    elif command == "U":
        client_name = _get_client_field('name')
        update_client(client_name)
        list_clients()
    elif command == "S":
        client_name = _get_client_field('name')
        found = search_clients(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print("The client: {} is not in our client's list".format(client_name))

    else:
        print('Invalid command')
