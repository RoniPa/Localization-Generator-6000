import os
import sys
import re
import json
import click

@click.command()
@click.option('--p', help='Source path (e.g. "./src/")')
@click.option('--o', help='Output file (e.g. "./localizations/en-US.json")')
@click.option('--e', default='utf-8', help='File encoding (e.g. "utf-8")')
def recurse_files(p, o, e):
    
    if (p == None):
        p = click.prompt('Give source root: (e.g. "./src/")', type=str)

    if (o == None):
        o = click.prompt('Give output file: (e.g. "./localizations/en-US.json")', type=str)

    pattern = '(\'|\")\s?\|\s?translate'
    dict_map = {}

    for root, directories, filenames in os.walk(p):
        gen = (x for x in filenames if x.endswith('.html') or x.endswith('.ts') or x.endswith('.js'))
        for filename in gen:
            try:
                with open(os.path.join(root, filename), encoding=e) as f:
                    for line in f:
                        for m in re.finditer(pattern, line):
                            end = m.start(0)
                            start = line[:end].rfind(line[end])
                            tags = (line[start+1:end]).split('.')

                            d = dict_map
                            last_i = len(tags)-1
                            for i in range(0, last_i): 
                                if tags[i] not in d:
                                    d[tags[i]] = {}
                                d = d[tags[i]]
                            d[tags[last_i]] = ""
            except:
                click.echo(click.style("Unexpected error: %s" % sys.exc_info()[0], fg="red"))
                raise click.Abort()
                
    try:
        with open(o, 'w', encoding=e) as f:
            f.write(json.dumps(dict_map, sort_keys=True, indent=4))
    except:
        click.echo(click.style("Unexpected error: %s" % sys.exc_info()[0], fg="red"))
        raise click.Abort()

    click.echo("File generated at %s" % o)
    click.echo("Have a nice day! :)")
