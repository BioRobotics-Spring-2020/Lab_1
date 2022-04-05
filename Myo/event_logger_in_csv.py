import os
import argparse
import pandas as pd

parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
parser.add_argument('-f', '--output', default = 'events.csv',
                    help='Output file path if outputting to file')
args = parser.parse_args()

def main():
    print('Event Logging Initiated')
    try:
        while True:
            event = input()
            current_time = pd.Timestamp(0).now()
            print(current_time, event)
            if event:
                df = pd.DataFrame(columns=['Event'])
                df.at[current_time] = event
                hdr = False if os.path.isfile(args.output) else True
                df.to_csv(args.output, mode='a', index_label='Timestamp', header=hdr)
    except KeyboardInterrupt:
        print("\nQuitting")
    except EOFError:
        pass
    print("Closing Event Logger")
if __name__ == '__main__':
    main()