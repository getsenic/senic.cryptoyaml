import click
from os import path

from . import api


@click.group(help='create, read and edit encrypted YAML files')
def main():
    pass


@click.command(help='generate a new private key on filesystem')
@click.argument('keyfile')
def generate_key(keyfile):
    fs = path.abspath(path.expanduser(keyfile))
    click.echo('Created new private key at {}'.format(fs))


@click.command(help='create a new encrypted YAML file from scratch')
@click.argument('filepath')
@click.option('--key', default=None, help='secret key')
@click.option('--keyfile', default=None, help='path to secret keyfile')
def create(filepath, key=None, keyfile=None):
    click.echo('created new file')


@click.command(help='decrypt and print the contents of a settings file to stdout')
def cat():
    click.echo('decrypting file')


main.add_command(generate_key)
main.add_command(create)
main.add_command(cat)
