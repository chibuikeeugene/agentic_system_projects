import os
from pathlib import Path


package_root  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_dir = os.path.join(package_root, 'models')
