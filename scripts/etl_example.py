# Notebook de ejemplo para ETL Runner

import pandas as pd
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', type=str, required=False)
parser.add_argument('--output_path', type=str, required=True)
parser.add_argument('--selector', type=str, required=False)
args = parser.parse_args()

# Simulación de procesamiento
if args.url:
    df = pd.DataFrame({'data': [1,2,3], 'source': [args.url]*3})
    df.to_csv(args.output_path, index=False)
    print(f"Archivo generado: {args.output_path}")
elif args.selector:
    with open(args.output_path, 'w') as f:
        f.write('{"selector": "%s", "values": [42, 43]}\n' % args.selector)
    print(f"Archivo generado: {args.output_path}")
else:
    print("No se especificó fuente válida.")
