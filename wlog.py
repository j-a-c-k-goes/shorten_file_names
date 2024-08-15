import sys
from tstamp import *
from msg import *

def WriteLog(file_name, mode, log_statements:list):
   try:
      with open(file_name, 'w') as source_file:
         source_file.write('---\n')
         source_file.write(f'TIMESTAMP {year}/{month}/{day} @ {hour}:{minute}\n')
         source_file.write(f'ran {sys.argv[0]} with {mode}\n'.upper())
         source_file.write(f'TARGET: {sys.argv[3]} files\n'.upper())
         source_file.write(f'PATH: {sys.argv[2]} \n'.upper())
         source_file.write('---\n')
         if len(log_statements) < 1:
            source_file.write('No log statements to report.\n')
         if (mode == 'dry-run-on'):
            source_file.write('There is no logging when DRY-RUN-ON\n')
         else:
            for index, log_statement in enumerate(log_statements):
               source_file.write(f'[{index}]    {log_statement}\n')
         print(f'Done writing {file_name}')
   except FileNotFoundError as fnf_exception:
      Msg('exception', f'{file_name} not found. Check path or spelling.')
      Msg('context', fnf_exception)
   except Exception as general_exception:
      Msg('exception', 'Consult error message below for details.')
      Msg('context', general_exception)