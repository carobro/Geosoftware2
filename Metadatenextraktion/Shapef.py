import click, shapefile

@click.command()
@click.option('--path', prompt='Datapath',
              help='Path to the data.')
def metadata(path):
    """Program that extracts the boudingbox of shapefiles."""
    sf= shapefile.Reader(path)
    output=sf.bbox
    
    click.echo(output)

if __name__ == '__main__':
    metadata()
