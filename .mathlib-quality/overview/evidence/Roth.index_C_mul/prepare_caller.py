from pathlib import Path
D=Path(__file__).resolve().parent
s=Path('/Users/ramin/LEAN/Roth/Roth/Theta.lean').read_text()
a=s.index('theorem sum_max_sub_le_index_det ');b=s.index('\nomit [DecidableEq τ] in',a)
t=s[a:b].replace('theorem sum_max_sub_le_index_det ','theorem callerReplay ')
t=t.replace('index_C_mul (Int.cast_ne_zero.2 (Units.ne_zero (Equiv.Perm.sign s)))','IndexCMul147.replacement (Int.cast_ne_zero.2 (Units.ne_zero (Equiv.Perm.sign s)))')
(D/'caller-probe-prep.lean.txt').write_text('namespace IndexCMulCaller147\nopen MvPolynomial Roth\nvariable {τ : Type*} [Fintype τ]\n'+t+'\n#print axioms callerReplay\nend IndexCMulCaller147\n')
