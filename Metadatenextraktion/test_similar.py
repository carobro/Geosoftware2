import pytest
import math
import similar

#Deutschland - Polen
def test_answer():
    bbox1 = [5.8663155, 47.270111, 15.041932 , 55.099159]
    bbox2 = [14.122971, 49.002048, 24.145782, 55.033695]
    assert similar.aehnlickeit(bbox1, bbox2) == 0.052537198756258265

# Muenster - Greven
def test_answer1():
    bbox1 = [7.473785, 51.840145, 7.774364, 52.060024]
    bbox2 = [7.5234, 52.0326, 7.7556, 52.152]
    assert similar.aehnlickeit(bbox1, bbox2) == 0.0006267747993827629

# Deutschland - Muenster
def test_answer2():
    bbox1 = [5.8663155, 47.270111, 15.041932 , 55.099159]
    bbox2 = [7.5234, 52.0326, 7.7556, 52.152]
    assert similar.aehnlickeit(bbox1, bbox2) == 0.19316458780635867

# Deutschland - Mexico
def test_answer3():
    bbox1 = [5.8663155, 47.270111, 15.041932 , 55.099159]
    bbox2 = [-118.6, 14.39, -86.49, 32.72]
    assert similar.aehnlickeit(bbox1, bbox2) == 0.6488100389180073