import argparse,pathlib,sys,importlib
p=argparse.ArgumentParser();p.add_argument('--task',choices=['b03','multitask'],required=True);p.add_argument('--results',required=True);a=p.parse_args();root=pathlib.Path(__file__).resolve().parent;target=pathlib.Path(a.results).resolve()
if a.task=='b03':
 code=(root/'source/b03/analyze.py').read_text();old="B=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(__file__).resolve().parents[1];P=B/'codex_v2_main'";assert old in code;code=code.replace(old,'B=pathlib.Path('+repr(str(root/'source'))+');P=pathlib.Path('+repr(str(target))+')',1);exec(compile(code,'b03_offline_analysis','exec'),{'__name__':'__main__','__file__':str(root/'source/b03/analyze.py')})
else:
 sys.path.insert(0,str(root/'source/multitask'));m=importlib.import_module('run');m.OUT=target
 for name in ['analyze.py','audit_propagation.py']:
  code=(root/'source/multitask'/name).read_text();exec(compile(code,name,'exec'),{'__name__':'__main__','__file__':str(root/'source/multitask'/name)})
