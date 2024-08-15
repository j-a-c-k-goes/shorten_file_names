import sys
import os
from usage import *
from msg import *
from ftype import *

def CheckArgs():
   try:
      arg_check_passed = bool()
      if len(sys.argv) < 4:
         Msg('error', 'Not enough arguments.')
         arg_check_passed = False   
         Usage()
      else:
         Msg('update', 'Args present. Checking for correctness.')
         param_dry_run  = sys.argv[1]
         param_path     = sys.argv[2]
         param_ext      = sys.argv[3]
         DRY_RUN_ON     = param_dry_run.lower() == 'dry-run-on'
         DRY_RUN_OFF    = param_dry_run.lower() == 'dry-run-off'
         valid_mode     = (DRY_RUN_ON) or (DRY_RUN_OFF)
         valid_path     = os.path.exists(param_path)
         valid_ext      = param_ext in file_types
         if (valid_mode and valid_path and valid_ext):
            arg_check_passed = True
            return { 
               'status': arg_check_passed, 
               'mode':  param_dry_run, 
               'path':  param_path,
               'ext':   param_ext
            }
         else:
            if (valid_mode == False):
               Msg('error', f'Invalid mode "{param_dry_run}".')
            if (valid_path == False):
               Msg('error', f'Non-existing path "{param_path}".')
            if (valid_ext == False):
               Msg('error', f'{param_ext} a recognized file type in this context..')
            arg_check_passed = False
            Usage()
      return { 
         'status': arg_check_passed, 
         'mode': None, 
         'path': None,
         'ext': None
      }
   except FileNotFoundError as exception:
      Msg('exception', f'{sys.argv[2]} is not a vaild path')
      Msg('details', exception)
   except Exception as exception:
      Msg('exception','See exception message.')
      Msg('details', exception)