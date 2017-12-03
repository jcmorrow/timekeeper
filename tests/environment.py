from os.path import abspath, dirname, join
TIMEKEEPER_PATH = abspath(join(dirname(__file__), '../timekeeper'))
import sys
sys.path.insert(0, TIMEKEEPER_PATH)
