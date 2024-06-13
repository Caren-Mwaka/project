import click
from models.machines import Machine
from models.parts import Part
from models.maintenance_records import MaintenanceRecord

@click.group()
def cli():
    """Part Manager CLI"""
    pass

@cli.command()
@click.option('--name', prompt='Machine name', help='The name of the machine.')
@click.option('--type', prompt='Machine type', help='The type of the machine.')
def create_machine(name, type):
    Machine.create(name, type)
    click.echo(f'Machine {name} created successfully.')

@cli.command()
@click.option('--machine-id', prompt='Machine ID', help='The ID of the machine to delete.')
def delete_machine(machine_id):
    Machine.delete(machine_id)
    click.echo('Machine deleted successfully.')

@cli.command()
def list_machines():
    machines = Machine.get_all()
    for machine in machines:
        click.echo(f'{machine["id"]}: {machine["name"]} ({machine["type"]})')

@cli.command()
@click.option('--machine-id', prompt='Machine ID', help='The ID of the machine to view.')
def view_machine(machine_id):
    machine = Machine.find_by_id(machine_id)
    if machine:
        click.echo(f'Machine: {machine["name"]} ({machine["type"]})')
        parts = Part.get_parts_by_machine(machine_id)
        if parts:
            for part in parts:
                click.echo(f'  Part: {part["name"]}, Quantity: {part["quantity"]}')
        else:
            click.echo('  No parts found.')
        records = MaintenanceRecord.get_records_by_machine(machine_id)
        if records:
            for record in records:
                click.echo(f'  Maintenance: {record["description"]}, Performed At: {record["performed_at"]}')
        else:
            click.echo('  No maintenance records found.')
    else:
        click.echo('Machine not found.')

@cli.command()
@click.option('--name', prompt='Part name', help='The name of the part.')
@click.option('--machine-id', prompt='Machine ID', help='The ID of the machine.')
@click.option('--quantity', prompt='Quantity', type=int, help='The quantity of the part.')
def create_part(name, machine_id, quantity):
    Part.create(name, machine_id, quantity)
    click.echo(f'Part {name} created successfully.')

@cli.command()
@click.option('--part-id', prompt='Part ID', help='The ID of the part to delete.')
def delete_part(part_id):
    Part.delete(part_id)
    click.echo('Part deleted successfully.')

@cli.command()
def list_parts():
    parts = Part.get_all()
    for part in parts:
        click.echo(f'{part["id"]}: {part["name"]}, Quantity: {part["quantity"]}, Machine ID: {part["machine_id"]}')

@cli.command()
@click.option('--part-id', prompt='Part ID', help='The ID of the part to view.')
def view_part(part_id):
    part = Part.find_by_id(part_id)
    if part:
        click.echo(f'Part: {part["name"]}, Quantity: {part["quantity"]}, Machine ID: {part["machine_id"]}')
    else:
        click.echo('Part not found.')

@cli.command()
@click.option('--machine-id', prompt='Machine ID', help='The ID of the machine.')
@click.option('--description', prompt='Description', help='Description of the maintenance.')
@click.option('--performed-at', prompt='Performed At', help='Date and time of the maintenance.')
def create_maintenance_record(machine_id, description, performed_at):
    MaintenanceRecord.create(machine_id, description, performed_at)
    click.echo(f'Maintenance record for machine {machine_id} created successfully.')

@cli.command()
@click.option('--record-id', prompt='Record ID', help='The ID of the maintenance record to delete.')
def delete_maintenance_record(record_id):
    MaintenanceRecord.delete(record_id)
    click.echo('Maintenance record deleted successfully.')

@cli.command()    
def list_maintenance_records():
    records = MaintenanceRecord.get_all()
    for record in records:
        click.echo(f'{record["id"]}: Machine ID: {record["machine_id"]}, Description: {record["description"]}, Performed At: {record["performed_at"]}')

@cli.command()
@click.option('--record-id', prompt='Record ID', help='The ID of the maintenance record to view.')
def view_maintenance_record(record_id):
    record = MaintenanceRecord.find_by_id(record_id)
    if record:
        click.echo(f'Maintenance Record: Machine ID: {record["machine_id"]}, Description: {record["description"]}, Performed At: {record["performed_at"]}')
    else:
        click.echo('Maintenance record not found.')

if __name__ == '__main__':
    cli()
