import click
from tabulate import tabulate

from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
    """Manage The clients lifecicycle"""
    pass


@clients.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help="The client's name")
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help="The client's company")
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help="The client's email")
@click.option('-p', '--position',
              type=str,
              prompt=True,
              help="The client's position")
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client = Client(name, company, email, position)
    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients = client_service.list_clients()
    headers = [field.capitalize() for field in Client.schema()]
    table = []
    # click.echo('ID  |   Name    |   Company     |   Email   |   Position')
    # click.echo('-' * 100)
    for client in clients:
        table.append([
            client['uid'],
            client['name'],
            client['company'],
            client['email'],
            client['position']
        ])
    click.echo(tabulate(table, headers))


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def update(ctx, client_uid):
    """Updates a single client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client = [client for client in client_service.list_clients() if client['uid'] == client_uid]
    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)
        click.echo('Client updated')
    else:
        click.echo('Client not found')


def _update_client_flow(client):
    click.echo("Leave empty if you don't want to modify a value")
    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)

    return client


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def delete(ctx, client_uid):
    """Delete a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    if click.confirm('Are you sure want to delete the client with uid: {}'.format(client_uid)):
        client_service.delete_client(client_uid)


all = clients
