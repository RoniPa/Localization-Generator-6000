import os
import sys
import re
import json
import click

@click.command()
@click.option('-p', '--path', help='Source path (e.g. "./src/")')
@click.option('-o', '--output', help='Output file (e.g. "./localizations/en-US.json")')
@click.option('-e', '--encoding', default='utf-8', help='File encoding. Defaults to UTF-8.', type=click.Choice(['utf-8', 'latin-1', 'ascii']))
@click.option('-a/-na', '--append/--no-append', default=True, help='Append content - if file exists, existing translations remain. Removed or moved tags are still destroyed. Enabled by default.')
def recurse_files(path, output, encoding, append):
    
    if (path == None):
        path = click.prompt('Give source root: (e.g. "./src/")', type=str)

    if (output == None):
        output = click.prompt('Give output file: (e.g. "./localizations/en-US.json")', type=str)

    pattern = '(\'|\")\s?\|\s?translate'
    dict_map = {}
    ref_map = {}
    
    # If file exists, read in as reference
    if (append and os.path.isfile(output)): 
        try:
            with open(output, 'r', encoding=encoding) as json_data:
                ref_map = json.load(json_data)
        except:
            click.echo(click.style("Unexpected error: %s" % sys.exc_info()[0], fg="red"))
            raise click.Abort()

    for root, directories, filenames in os.walk(path):
        gen = (x for x in filenames if x.endswith('.html') or x.endswith('.ts') or x.endswith('.js'))
        for filename in gen:
            try:
                with open(os.path.join(root, filename), encoding=encoding) as f:
                    for line in f:
                        for m in re.finditer(pattern, line):
                            end = m.start(0)
                            start = line[:end].rfind(line[end])
                            tags = (line[start+1:end]).split('.')

                            d1 = dict_map
                            d2 = ref_map
                            last_i = len(tags)-1

                            for i in range(0, last_i): 
                                if tags[i] not in d1:
                                    d1[tags[i]] = {}

                                if tags[i] in d2:
                                    d2 = d2[tags[i]]

                                d1 = d1[tags[i]]
                            
                            if append and tags[last_i] in d2 and type(d2[tags[last_i]]) is str:
                                d1[tags[last_i]] = d2[tags[last_i]]  
                            else:
                                d1[tags[last_i]] = ""
                            
            except TypeError:
                click.echo(click.style("TypeError... Is a tag overwritten?", fg="red"))
                raise click.Abort()
            except:
                click.echo(click.style("Unexpected error: %s" % sys.exc_info()[0], fg="red"))
                raise click.Abort()
                
    try:
        with open(output, 'w', encoding=encoding) as f:
            f.write(json.dumps(dict_map, sort_keys=True, indent=4))
    except:
        click.echo(click.style("Unexpected error: %s" % sys.exc_info()[0], fg="red"))
        raise click.Abort()

    click.echo("File generated at %s" % output)
    click.echo("Have a nice day! :)")
