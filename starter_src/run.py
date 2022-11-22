https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Entry point for PA2

Feel free to change/restructure the entire project if you wish
"""
import time


def display_exec_time(begin: float, msg_prefix: str = ""):
  """Displays the script's execution time

  Args:
    begin (float): time stamp for beginning of execution
    msg_prefix (str): display message prefix
  """
  exec_time = time.time() - begin

  msg_header = "Execution Time:"
  if msg_prefix:
    msg_header = msg_prefix.rstrip() + " " + msg_header

  if exec_time > 60:
    et_m, et_s = int(exec_time / 60), int(exec_time % 60)
    print("%s %dm %ds" % (msg_header, et_m, et_s))
  else:
    print("%s %.2fs" % (msg_header, exec_time))

def run_scorer(preds_file: str):
  """Automatically runs `scorer.py` on model predictions. You don't need to use
  this code if you'd rather run `scorer.py` manually.

  Args:
    preds_file (str): path to model's prediction file
  """
  import sys
  import subprocess

  python = 'python3' # TODO: change this to your python command
  scorer = './scorer.py'
  gold = './data/test.json'
  auto = preds_file
  command = "{} {} {} {}".format(python, scorer, gold, auto)

  print("Running scorer with command:", command)
  proc = subprocess.Popen(
    command, stdout=sys.stdout, stderr=sys.stderr, shell=True,
    universal_newlines=True
  )
  proc.wait()

def run():
  begin = time.time()

  # TODO:
  #   1. Load data and create data iterators
  #   2. Initialize Logistic Regression Model
  #   3. Define Loss Function and Optimizer
  #   4. Write a training loop
  #   5. Make predictions on test set and export them as JSON
  #   6. Run `scorer.py` using exported JSON from Step 5

  display_exec_time(begin)

if __name__ == '__main__':
  run()
