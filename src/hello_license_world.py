#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: Copyright (c) 2021 LG Electronics Inc.
# SPDX-License-Identifier: Apache-2.0
from __future__ import print_function
import webbrowser
import git

def main():
    print("Hello License Text World!")
    url='http://oss.lge.com/'
    webbrowser.open(url)

if __name__ == "__main__":
    main()
