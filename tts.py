#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class say:
    def this(self, text_to_say):
        import os
        os.system("say "+text_to_say)
