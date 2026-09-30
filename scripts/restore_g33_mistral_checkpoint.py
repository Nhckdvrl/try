"""Restore the exact historical Mistral revision into an isolated local cache.

Run on the inference host with HF_HUB_DISABLE_XET=1. No checkpoint substitution.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from huggingface_hub import hf_hub_download
REPO='mistralai/Mistral-Small-24B-Instruct-2501'
REVISION='9527884be6e5616bdd54de542f9ae13384489724'
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--cache',default='/var/tmp/g33_mistral_hf_cache');a=ap.parse_args()
 files=['config.json','generation_config.json','special_tokens_map.json','tokenizer.json','tokenizer_config.json','model.safetensors.index.json']+[f'model-{i:05d}-of-00010.safetensors' for i in range(1,11)]
 def job(f):
  p=hf_hub_download(REPO,f,revision=REVISION,cache_dir=a.cache);print(f,Path(p).stat().st_size,flush=True)
 with ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(job,files))
 print('Checkpoint:',Path(a.cache)/('models--'+REPO.replace('/','--'))/'snapshots'/REVISION)
if __name__=='__main__':main()
