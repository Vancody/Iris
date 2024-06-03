import sys
import os

# Добавляем директорию проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import main

if __name__ == "__main__":
    main()
