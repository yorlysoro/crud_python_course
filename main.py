#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import csv

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r', encoding='UTF-8') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)     


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode="w", encoding='UTF-8') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print("Client alerady is in the client's list")


def list_clients():
    print('uid |  name  | company  | email  | position ')
    print('*' * 50)

    for idx, client in enumerate(clients):
        print("{uid} | {name} | {company} | {email} | {position}".format(uid=idx, name=client['name'],
                                                                        company=client['company'], email=client['email'],
                                                            position=client['position']))


def _get_client_idx(client_name):
    for idx, client_id in enumerate(clients):
        if client_id['name'] == client_name:
            return idx


def update_client(client_id):
    global clients

    if len(clients) - 1 >= client_id:
        print(f"The client {client_id} already exists")
        print("please insert the new data")
        update_client = {}
        for field in CLIENT_SCHEMA:
            update_client[field] = _get_client_field(field)
        clients[client_id] = update_client
    else:
        print("Client is not in clients list")


def delete_client(client_id):
    global clients

    if len(clients) - 1 >= client_id:
        print(f"The client {client_id} already exists")
        clients.remove(clients[client_id])
        print(f"Client {client_id} already delete!")
    else:
        print("Client is not in clients list")


def search_clients(client_name):
    for client in clients:
        if client_name == client['name']:
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
    print("[L]ist clients")


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
    _initialize_clients_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()
    if command == "C":
        client = {}
        for field in CLIENT_SCHEMA:
            client[field] = (_get_client_field(field))
        create_client(client)
    elif command == "L":
        list_clients()
    elif command == "D":
        client_id = _get_client_field('id')
        delete_client(int(client_id))
    elif command == "U":
        client_id = _get_client_field('id')
        update_client(int(client_id))
    elif command == "S":
        client_name = _get_client_field('name')
        found = search_clients(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print("The client: {} is not in our client's list".format(client_name))

    else:
        print('Invalid command')

    _save_clients_to_storage()
