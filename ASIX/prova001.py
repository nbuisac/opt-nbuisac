import click

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--message", prompt="Missatge -> ", help="Missatge que volem mostrar.")
@click.option('-l', '--lower', type=bool, default=False)

def hello(count, message, lower):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"{message}")
        click.echo(f"{lower}")

if __name__ == '__main__':
    hello()

