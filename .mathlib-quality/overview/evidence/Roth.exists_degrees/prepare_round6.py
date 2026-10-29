from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
s=(D/'composition5-executed.lean.txt').read_text().replace('\n#check @Nat.ceil_lt_mul\n#check @Nat.ceil_le_mul\n','\n')
def req(label,s):
 assert max(map(len,s.splitlines()))<=100
 p=D/(label+'6-executed.lean.txt');p.write_text(s)
 (D/'root-requests'/(label+'06.json')).write_text(json.dumps(dict(id=label+'06',operation='run_code',source=p.name,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),receipt=label+'06-receipt.json',arguments={}),indent=2)+'\n')
req('composition',s)
prefix=(D/'isolated-prefix.lean.txt').read_text()+'import Mathlib.Algebra.Order.Floor.Semifield\n'
(D/'candidate-prefix.lean.txt').write_text(prefix)
(D/'native-prefix-authorization.json').write_text(json.dumps(dict(declaration='Roth.exists_degrees',prefix_sha256=[hashlib.sha256(prefix.encode()).hexdigest()],modules=['Mathlib.Algebra.Order.Floor.Semifield'],root_review='Fresh278 explicit authorization after independent pinned Floor.Semifield header/proof read lines56–84. Dedicated candidate06 only; exact stable18+this one module, no shared18 or disk9 mutation. No earlier exception inherited.'),indent=2)+'\n')
req('candidate',prefix+'''
#check_failure Roth.exists_degrees
#check @Nat.ceil_lt_mul
#check @Nat.ceil_le_mul
namespace Degrees278Candidate
-- The closest existing scalar bound works once its single-coordinate threshold is supplied.
example {K : Type*} [Field K] [LinearOrder K] [IsOrderedRing K] [FloorSemiring K]
    {a ε : K} (hε : 0 < ε) (ha : (⌈ε⁻¹⌉₊ : K) / (1 + ε) < a) :
    (⌈a⌉₊ : K) < (1 + ε) * a := by
  exact Nat.ceil_lt_mul (by linarith) (by simpa using ha)
end Degrees278Candidate
''')
print('composition06 stable18 and candidate06 authorized19 ready')
print(hashlib.sha256(prefix.encode()).hexdigest())
