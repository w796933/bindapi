# -*- coding: utf-8 -*-
# author: itimor

from datetime import timedelta


def diff_times_in_seconds(t1, t2):
    h1, m1, s1 = t1.hour, t1.minute, t1.second
    h2, m2, s2 = t2.hour, t2.minute, t2.second
    t1_secs = s1 + 60 * (m1 + 60 * h1)
    t2_secs = s2 + 60 * (m2 + 60 * h2)
    tc = str(timedelta(seconds=(t2_secs - t1_secs)))
    return tc
