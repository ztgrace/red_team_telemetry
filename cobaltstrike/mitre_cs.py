#!/usr/bin/env python

from stix2 import TAXIICollectionSource, Filter
from taxii2client import Collection

# Initialize dictionary to hold Enterprise ATT&CK content
attack = {}

# Establish TAXII2 Collection instance for Enterprise ATT&CK collection
collection = Collection("https://cti-taxii.mitre.org/stix/collections/95ecc380-afe9-11e4-9b6c-751b66dd541e/")

# Supply the collection to TAXIICollection
tc_source = TAXIICollectionSource(collection)

# Create filters to retrieve content from Enterprise ATT&CK based on type
filter_objs = {"techniques": Filter("type", "=", "attack-pattern"),
          "mitigations": Filter("type", "=", "course-of-action"),
          "groups": Filter("type", "=", "intrusion-set"),
          "malware": Filter("type", "=", "malware"),
          "tools": Filter("type", "=", "tool"),
          "relationships": Filter("type", "=", "relationship")
}

# Retrieve all Enterprise ATT&CK content
for key in filter_objs:
          attack[key] = tc_source.query(filter_objs[key])

print("%attack = %(")
for t in attack['techniques']:
    phase = t['kill_chain_phases'][0]['phase_name']
    for ref in t['external_references']:
        if ref.get('source_name', None) == 'mitre-attack':
            tactic = ref['external_id']
            #print "%s:%s:%s" % (t['name'], phase, ref['external_id'])
            print(tactic + " => %(phase => '" + phase + "', name => '" + t['name'] + "'),")
print(");")
