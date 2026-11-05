import argparse,pathlib,sys,runpy,os
p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();r=pathlib.Path(__file__).resolve().parent;d=r/'source/multitask';sys.path.insert(0,str(d))
# Keep exact archived core; only redirect its top-level output constant for a fresh replication.
source=(d/'run.py').read_text();old="OUT=BASE/'multitask_main_v4_results'";assert old in source
output=pathlib.Path(a.output).resolve();assert not output.exists(),'Refusing to overwrite existing results'
source=source.replace(old,'OUT=pathlib.Path('+repr(str(output))+')',1)
exec(compile(source,str(d/'run.py'),'exec'),{'__name__':'__main__','__file__':str(d/'run.py')})
