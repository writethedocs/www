import ruamel.yaml
import pprint

yaml_files = ['../_data/prague-2020-schedule.yaml']

for yaml_file in yaml_files:

    yaml = ruamel.yaml.YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.preserve_quotes = True

    with open(yaml_file) as fp:
        talks = yaml.load(fp)

    for t in talks:
        #print(t, '>', talks[t])
        #print(type(talks[t]))
        for s in talks[t]:
            # lazy time handling, split at : then increment hours by 1 and jam back together
            ot = s['time'].split(':',1)
            ot[0] = int(ot[0]) + 1
            s['time'] = str(ot[0])+':'+ot[1]


    with open(yaml_file, 'w') as fp:
        yaml.dump(talks, fp)
