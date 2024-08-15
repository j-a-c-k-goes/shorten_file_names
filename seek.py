import os
from wlog import *
from tstamp import *
def Seek(path, mode:str, file_extension):
   try:
      tmp_log_statements = list()
      Msg('[mode]', mode)
      if (not os.path.exists(path) ):
         Msg('error', f'Cannot walk non-existing path ({path})')
         exit(-1)
      else:
         files_inspected            = 0
         files_in_violation         = 0
         files_renamed              = 0
         invalid_renaming_attempts  = 0
         files_skipped              = 0
         print(f'Preparing to walk from "{path}"\n')
         for root, directories, files in os.walk(f'{path}', topdown=True, followlinks=True):
            for file in files:
               filename_too_long = (len(file) > 8)
               if file.endswith(file_extension):
                  if filename_too_long:
                     files_in_violation += 1
                     Msg('warning', f'{file} is over 8 characters long.')
                     prompt_update  = str(input('Shorten file name (y/n)? '))
                     if prompt_update.lower() == 'y' or prompt_update.lower() == 'yes':
                        prompt_filename = str(input('New filename? ')) 
                        if len(prompt_filename) > 8:
                           Msg('invalid', f'New filename "{prompt_filename}" too long')
                           log_statement  = f'Cannot rename {file} -> {prompt_filename}'
                           invalid_renaming_attempts += 1
                        if (prompt_filename.endswith(file_extension) == False):
                           Msg('invalid', 'Renaming with different extension not allowed.')
                           log_statement = f'Blocking renaming {file} with divergent extension.'
                           invalid_renaming_attempts += 1
                        else:
                           Msg('valid', f'Can update {file} -> {prompt_filename}')
                           log_statement  = f'Renamed {file} -> {prompt_filename}'
                           files_renamed += 1
                     else:
                        Msg('update', 'Skipping renaming.')
                        log_statement  = (f'Skipping renaming {file}')
                        files_skipped  += 1
                     if (mode == 'dry-run-on'):
                        print(log_statement)
                     elif (mode =='dry-run-off'):
                        os.system(f'mv {root}/{file} -> {root}/{prompt_filename}')
                        tmp_log_statements.append(log_statement)
                  files_inspected += 1 # only counting file with mathcing extension, not entire walk
         Msg('inspections', files_inspected)
         Msg('violations', files_in_violation)
         Msg('renamings', files_renamed)
         Msg('invalid attempts', invalid_renaming_attempts)
         Msg('skips', files_skipped)
         Msg('total', (files_inspected+files_in_violation+files_renamed+invalid_renaming_attempts+files_skipped))
         WriteLog(f'/tmp/{year}{month}{day}{hour}{minute}-log-files-shortened.log', mode, tmp_log_statements)
   except Exception as error:
      print(error)
      return -1