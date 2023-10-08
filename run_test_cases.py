# -*- encoding: utf-8 -*-

import sys
import pytest

from config.conf import ROOT_DIR, REPORT_NAME_WITH_ABSOLUTE_PATH



def main():
    if ROOT_DIR not in sys.path:
        sys.path.append(ROOT_DIR)
    
    args = ['--reruns', '0', '--html={}'.format(REPORT_NAME_WITH_ABSOLUTE_PATH), '--self-contained-html', '-s']
    pytest.main(args)
    # print(args)


if __name__ == '__main__':
    main()
