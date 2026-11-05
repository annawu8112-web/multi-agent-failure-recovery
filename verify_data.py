from pathlib import Path
import hashlib,shutil,json
r=Path(__file__).resolve().parent;p=r/'data/accounting.sqlite'
assert p.exists(),'Obtain gated BookSQL/accounting.sqlite and place it in data/accounting.sqlite'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='89f890e3d55db08fe7f32fcfead6f56e22a3ab2615f9fc382f30e29ce9b94763','Database checksum mismatch'
(r/'source/data').mkdir(parents=True,exist_ok=True)
target=r/'source/data/accounting.sqlite'
if not target.exists():target.symlink_to(p)
shutil.copy2(r/'tasks.json',r/'source/audited_tasks.json')
print('Pinned database verified; local source paths ready.')
