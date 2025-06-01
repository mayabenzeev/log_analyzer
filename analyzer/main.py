# main CLI implementation goes here
import argparse

from analyzer.analyzer import LogAnalyzer

def main():
    parser = argparse.ArgumentParser()
        
    parser.add_argument('--input', 
                                 type=str, 
                                 required=True, 
                                 help='Path to the log file')
    parser.add_argument('--report', 
                                 type=str, 
                                 required=True, 
                                 choices=['summary', 'top-user', 'common-error'],
                                 help='Type of report to generate')
        
    args = parser.parse_args()

    analyzer = LogAnalyzer(args.input, args.report)
    analyzer.generate_report()
    
    
if __name__ == '__main__':
    main()