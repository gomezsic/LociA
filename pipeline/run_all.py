import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import ingest, embed, project, cluster, render, manifest

print("=== lociA pipeline ===\n")
print("1/6 ingest")
ingest.run()
print("\n2/6 embed")
embed.run()
print("\n3/6 project")
project.run()
print("\n4/6 cluster")
cluster.run()
print("\n5/6 render")
render.run()
print("\n6/6 manifest")
manifest.run()
print("\n=== done ===")
